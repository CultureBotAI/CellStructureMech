# Glycine reductase complex scientific review

- Review: 20261022T072028Z-glycine-reductase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:48Z
- Finished UTC: 2026-10-22T07:20:28Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Glycine-reductase identity, named components, native examples and reaction direction are supported. Two minors correct the C-chain family rationale and the1988 sequencing-source attribution without forcing a single-chain identifier onto protein C.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Source-read extents are enumerated per evidence row; no maintained neighboring record supplies biological evidence.

Selection: Target 7 of batch56, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030700 | data/structures/other/glycine_reductase_complex.yaml | maintained | glycine reductase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030700 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030700 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0030700 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:0030700 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030700 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:0030700 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030700 | 14 of 18 collected target identifiers returned OK. PMID:11271425: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:1429431: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:2018775: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:2963330: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030700 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030700 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030700 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030700 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030700 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Three named components and the two-chain C boundary

identity: supported. Targets: GO:0030700.

GO identity, parent and function agree. The A/B/C naming convention is compatible with two distinct C-chain genes; the grouped C component is not equated to either accession alone. Reviewed A and explicitly unreviewed B/C examples retain their native identity/status.

### Exact C-chain families versus whole C-complex mapping

grounding: concern. Targets: GO:0030700.

The maintained statement that verified C matches are only broader CoA-transferase signatures is inaccurate. Specific reductase-C alpha/beta chain families exist across glycine, sarcosine and betaine systems and match the separate native proteins. Neither one alone grounds the retained PROTEIN_COMPLEX row; label-only can remain pending a whole-complex identifier or justified subunit split.

### Clostridial source and current strain taxonomy

scope: supported. Targets: GO:0030700.

Native499177 is Acetoanaerobium sticklandii DSM519, with Clostridium sticklandii DSM519 as synonym. The proteins independently carry that strain identity; the inspected2001 abstract establishes C.sticklandii operon membership but its full strain Methods were unavailable. The1988 study is a C.sticklandii purified-protein experiment.

### Catalytic transfer supported separately from the mislabeled sequencing source

graph: concern. Targets: GO:0030700.

Arkowitz1991 available abstract supports generation of Se-carboxymethyl protein A, acetyl protein C and phosphate exchange; the native A annotation independently supports the transfer pathway. The1988 sequencing study instead chemically carboxamidomethylates protein A for analysis and reports analytical carboxymethyl derivatives in its amino-acid tables. The maintained edge note says residue, not intermediate; placing that sequencing citation under catalytic transfer does not demonstrate the transfer. The separately supported reaction is retained.

### Catalytic competence is distinct from complex formation

grounding: unknown. Targets: GO:0030700.

The inspected catalytic, sequence and operon evidence does not independently establish universal physical formation necessity of each named component. UNKNOWN is retained without converting activity into assembly requirement.

### Complete maintained target and bounded evidence coverage

completeness: supported. Targets: GO:0030700.

Every maintained field, evidence note, graph statement and discussion was inspected at the declared source extents. Optional inventories and unmeasured formation requirements are not invented from native validation.

## Findings

### F1: Correct the protein C family-grounding rationale

minor / open / confirmed; issue key: glycine-c-family-rationale.

The current C grounding note says its verified matches are only broad CoA-transferase signatures. Native IPR017236 and IPR012116 identify specific beta and alpha protein C chains shared across glycine/sarcosine/betaine reductase systems. They are not glycine-exclusive families. The grouped-complex boundary still prevents substituting either single-chain family as the whole C identifier.

### F2: Distinguish chemical labeling from the catalytic intermediate

minor / open / confirmed; issue key: glycine-sequencing-source-attribution.

The first transfer edge attributes characterization of the carboxymethylated selenocysteine residue to PMID2963330. The actual study chemically carboxamidomethylates purified protein A with iodoacetamide for peptide sequencing, reports analytical derivatives, and leaves its precise catalytic function unresolved. The note says residue rather than intermediate; its placement under catalytic transfer does not establish that reaction. Separate evidence supports the catalytic model.

## Recommended Actions And Acceptance Checks

### A1

Replace the inaccurate broad-signature rationale with the verified two-chain families and their shared glycine/sarcosine/betaine scope; retain label-only for the combined complex unless a source-backed split or exact complex identifier is chosen.

- Keep E3PXS0/grdC beta and E3PXS1/grdD alpha distinct.
- Do not force a single family onto the whole protein C complex.
- Preserve supported identities and source scope; pass applicable native gates.

### A2

Correct the1988 note to its protein-sequencing/chemical-labeling scope and use a directly relevant catalytic source for the transfer edge, retaining supported reaction direction.

- Distinguish the chemical labeling/sequence analysis and analytical derivatives from evidence demonstrating catalytic carboxymethyl transfer.
- Keep PMID2963330 as sequence evidence where appropriate; preserve the independently supported catalytic model.
- Preserve supported identities and source scope; pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/glycine_reductase_complex.yaml; Entire maintained record, including all evidence, examples, graphs, history and discussions | context_only | The entire maintained target was read. Dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, essentiality, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from activity or viability. COMMON means present in most members, with losses the exception; VARIABLE means patchy lineage- or strain-level presence. Neither enum is redefined as merely observed occurrence. |
| curation | docs/CURATION.md; Component grounding, including REVIEWED_LABEL_ONLY at159–160 | context_only | A verified exact full-protein family is distinct from a shared domain or a broader class. Label-only does not mean simply that an available exact mapping was not curated this pass. |
| complex56-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700,GO:1990204,GO:0030699,GO:0042765,GO:0032991,GO:0005789,GO:0016255,GO:1990220,GO:0016465,GO:0006457,GO:1990131,GO:0038202,GO:0000329,GO:0071986,GO:1990130,GO:0061700; Complete target-relevant definitions/synonyms and typed relationships in combined response; no unrelated child or definition attributed to this target | supports | GO0030700 identifies the glycine reductase complex, usually comprising named A, B and C components; GO1990204 defines its oxidoreductase-complex parent and GO0030699 its glycine-reductase activity. The usual three named components do not assert that protein C is a single polypeptide. |
| complex56-agent-GO0030700-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only ancestor response contains the maintained parent class. It does not establish parthood or taxonomic frequency. |
| complex56-agent-tax-499177 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/499177; Complete ENA taxonomy identity, names and lineage | supports | Taxon499177 is Acetoanaerobium sticklandii DSM 519, rank strain; the native names and lineage identify this exact organism. |
| complex56-agent-protein-E3PXR9 | https://rest.uniprot.org/uniprotkb/E3PXR9.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): E3PXR9, Glycine reductase component B (47 kDa, subunit gamma); primary genes grdB, synonyms none, taxon499177. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-protein-E3PXS0 | https://rest.uniprot.org/uniprotkb/E3PXS0.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): E3PXS0, Glycine reductase component C subunit beta; primary genes grdC, synonyms none, taxon499177. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-protein-E3PXS1 | https://rest.uniprot.org/uniprotkb/E3PXS1.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): E3PXS1, Glycine reductase component C subunit alpha; primary genes grdD, synonyms none, taxon499177. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-protein-P26971 | https://rest.uniprot.org/uniprotkb/P26971.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P26971, Glycine/sarcosine/betaine reductase complex component A; primary genes grdA, synonyms none, taxon499177. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-pmid-11271425 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11271425+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and available abstract | supports | MED11271425: Molecular analysis of the grd operon coding for genes of the glycine reductase and of the thioredoxin system from Clostridium sticklandii. Graentzdoerffer A, Pich A, Andreesen JR. (2001), DOI10.1007/s002030000232. Exact metadata and the entire available native abstract read; primary-body access is not implied. |
| complex56-agent-pmid-1429431 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1429431+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and available abstract | supports | MED1429431: Clostridium sticklandii glycine reductase selenoprotein A gene: cloning, sequencing, and expression in Escherichia coli. Garcia GE, Stadtman TC. (1992), DOI10.1128/jb.174.22.7080-7089.1992. Exact metadata and the entire available native abstract read; primary-body access is not implied. |
| complex56-agent-pmid-2018775 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2018775+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and available abstract | supports | MED2018775: Mechanism of action of clostridial glycine reductase: isolation and characterization of a covalent acetyl enzyme intermediate. Arkowitz RA, Abeles RH. (1991), DOI10.1021/bi00230a039. Exact metadata and the entire available native abstract read; primary-body access is not implied. The native abstract is explicitly truncated at250 words. |
| complex56-agent-pmid-2963330 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2963330+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and available abstract | supports | MED2963330: Selenoprotein A of the clostridial glycine reductase complex: purification and amino acid sequence of the selenocysteine-containing peptide. Sliwkowski MX, Stadtman TC. (1988), DOI10.1073/pnas.85.2.368. Exact metadata and the entire available native abstract read; primary-body access is not implied. |
| complex56-agent-ipr-IPR006812 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006812/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR006812 is the glycine/sarcosine/betaine reductase component A family; its shared substrate-system scope does not invalidate the named A class. |
| complex56-agent-ipr-IPR010186 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010186/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR010186 is the glycine-reductase selenoprotein B family, distinct from other substrate-specific B classes. |
| complex56-agent-ipr-IPR017236 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017236/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR017236 is the component C beta-subunit family shared across glycine, sarcosine and betaine reductase systems, rather than merely a broad CoA-transferase signature. |
| complex56-agent-ipr-IPR012116 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012116/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR012116 is the component C alpha-subunit family shared across glycine, sarcosine and betaine reductase systems. It does not denote the complete two-chain protein C complex. |
| complex56-agent-sliwkowski1988-page-368 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/7a27be3b71d9/pnas00254-0077.png; Printed p368: Title/abstract, Introduction, Methods through amino-acid analysis. Genuine native page scan visually read. | supports | The title/abstract identify a protein-sequencing study; Methods chemically carboxamidomethylate purified protein A with iodoacetamide before peptide analysis. |
| complex56-agent-sliwkowski1988-page-369 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/e7b84131f11c/pnas00254-0078.png; Printed p369: Methods continuation, Results opening and Fig1 pixels/caption. Genuine native page scan visually read. | supports | Protease digestion, chromatographic purification and sequencing methods and initial Results analyze chemically labeled selenium-containing peptides. |
| complex56-agent-sliwkowski1988-page-370 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/8298cc39c8af/pnas00254-0079.png; Printed p370: Complete Results page, Tables1/2 and Fig2 pixels/caption. Genuine native page scan visually read. | supports | Results sequence the labeled selenium-containing peptides, with amino-acid compositions and purification chromatograms. Tables and Fig2 concern carboxamidomethylated protein A preparations. |
| complex56-agent-sliwkowski1988-page-371 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/fcddb6b45c63/pnas00254-0080.png; Printed p371: Complete Discussion; reference list inspected only for context. Genuine native page scan visually read. | supports | Discussion explicitly leaves the precise catalytic function of protein A unresolved and proposes a redox-center interpretation. This is not a demonstration of the catalytic carboxymethyl transfer intermediate. |
| schema-result | just validate data/structures/other/glycine_reductase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/glycine_reductase_complex.yaml |
| strict-result | just validate-strict data/structures/other/glycine_reductase_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/glycine_reductase_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/glycine_reductase_complex.yaml  (GO:0030700)<br>  glycine_reductase_catalytic_transfer	grdb_selenoprotein_b	COVERED	-&gt;grdb_selenoprotein_b (UniProtKB:E3PXR9)<br>  glycine_reductase_catalytic_transfer	grda_selenoprotein_a	COVERED	-&gt;grda_selenoprotein_a (UniProtKB:P26971)<br>  glycine_reductase_catalytic_transfer	grdc_protein_c	COVERED	-&gt;grdc_protein_c (UniProtKB:E3PXS0, UniProtKB:E3PXS1)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/glycine_reductase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 18 collected target identifiers returned OK. PMID:11271425: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:1429431: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:2018775: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:2963330: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified. The sparse B56 checkout was not used to claim a new full-site QC run.
- No supplements or atomic coordinates were independently analyzed. Actual source reading is limited to the exact locators below.
- Arkowitz1991 publisher returned403; its native abstract is truncated at250 words. Graentzdoerffer2001 publisher returned200 ClientChallenge. Garcia1992 modern PMC exposes abstract/page assets but its full scanned body was not read.
- Sliwkowski1988 legacy route returned200 CAPTCHA, but four genuine separately hashed native scans368–371 were visually read in full. Its Discussion is not promoted into later catalytic proof.
- The2001 full Methods strain designation was not independently inspected; DSM519 identity is separately supported by native proteins/taxonomy.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072028Z-glycine-reductase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Glycine reductase complex scientific review
started_at: '2026-10-22T06:59:48Z'
finished_at: '2026-10-22T07:20:28Z'
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
summary: Glycine-reductase identity, named components, native examples and reaction
  direction are supported. Two minors correct the C-chain family rationale and the1988
  sequencing-source attribution without forcing a single-chain identifier onto protein
  C.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/glycine_reductase_complex.yaml
    sha256: 7df61164fbbf00d11b56de5cf7e21e2bcc813413167c4cdafba4becb74002cd6
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
- target_id: GO:0030700
  path: data/structures/other/glycine_reductase_complex.yaml
  label: glycine reductase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_reductase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Source-read extents are enumerated per evidence row; no maintained neighboring
    record supplies biological evidence.
  selection: Target 7 of batch56, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030700
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030700
  command: just validate data/structures/other/glycine_reductase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030700
  command: just validate-strict data/structures/other/glycine_reductase_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030700
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0030700
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030700
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030700
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex56-agent-go
  - complex56-agent-GO0030700-ancestors
  - complex56-agent-tax-499177
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  - complex56-agent-pmid-11271425
  - complex56-agent-pmid-1429431
  - complex56-agent-pmid-2018775
  - complex56-agent-pmid-2963330
  - complex56-agent-ipr-IPR006812
  - complex56-agent-ipr-IPR010186
  - complex56-agent-ipr-IPR017236
  - complex56-agent-ipr-IPR012116
  - complex56-agent-sliwkowski1988-page-368
  - complex56-agent-sliwkowski1988-page-369
  - complex56-agent-sliwkowski1988-page-370
  - complex56-agent-sliwkowski1988-page-371
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030700
  summary: '14 of 18 collected target identifiers returned OK. PMID:11271425: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:1429431: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:2018775: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:2963330: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex56-agent-pmid-11271425
  - complex56-agent-pmid-1429431
  - complex56-agent-pmid-2018775
  - complex56-agent-pmid-2963330
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030700
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
  - GO:0030700
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
  - GO:0030700
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
  - GO:0030700
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
  - GO:0030700
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
  reference: data/structures/other/glycine_reductase_complex.yaml
  locator: Entire maintained record, including all evidence, examples, graphs, history
    and discussions
  accessed_at: '2026-10-22T07:10:59Z'
  support: context_only
  summary: The entire maintained target was read. Dated curation history is not independent
    biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, essentiality, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T07:10:59Z'
  support: context_only
  summary: Formation necessity differs from activity or viability. COMMON means present
    in most members, with losses the exception; VARIABLE means patchy lineage- or
    strain-level presence. Neither enum is redefined as merely observed occurrence.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, including REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T07:10:59Z'
  support: context_only
  summary: A verified exact full-protein family is distinct from a shared domain or
    a broader class. Label-only does not mean simply that an available exact mapping
    was not curated this pass.
- evidence_id: complex56-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700,GO:1990204,GO:0030699,GO:0042765,GO:0032991,GO:0005789,GO:0016255,GO:1990220,GO:0016465,GO:0006457,GO:1990131,GO:0038202,GO:0000329,GO:0071986,GO:1990130,GO:0061700
  locator: Complete target-relevant definitions/synonyms and typed relationships in
    combined response; no unrelated child or definition attributed to this target
  accessed_at: '2026-10-22T06:56:23.574147Z'
  support: supports
  summary: GO0030700 identifies the glycine reductase complex, usually comprising
    named A, B and C components; GO1990204 defines its oxidoreductase-complex parent
    and GO0030699 its glycine-reductase activity. The usual three named components
    do not assert that protein C is a single polypeptide.
  snapshot_sha256: 47442ac474d759525b8a001d355e3e4db9a53b9c5c0389770a0b1f4a3bd9cd6c
- evidence_id: complex56-agent-GO0030700-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:04:03.646930Z'
  support: supports
  summary: The is_a-only ancestor response contains the maintained parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: 0f232137582404ff823a93310d4e12e100e1d9267a581305ca8e5edd43bb7d54
- evidence_id: complex56-agent-tax-499177
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/499177
  locator: Complete ENA taxonomy identity, names and lineage
  accessed_at: '2026-10-22T06:56:31.468195Z'
  support: supports
  summary: Taxon499177 is Acetoanaerobium sticklandii DSM 519, rank strain; the native
    names and lineage identify this exact organism.
  snapshot_sha256: 24fb41515b348f17ffcf7f91dbb74dd491f8e4e231f4c5e33b7e6891c2efffaf
- evidence_id: complex56-agent-protein-E3PXR9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/E3PXR9.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:23.574620Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): E3PXR9, Glycine reductase component B (47
    kDa, subunit gamma); primary genes grdB, synonyms none, taxon499177. Native annotation
    evidence distinguishes measured and inferred claims. This protein response independently
    supplies its own family cross-references.'
  snapshot_sha256: ede0019dc81068398aed18cb6e108e36b5b4df623d886a4fa3b788a9f5f0e3ae
- evidence_id: complex56-agent-protein-E3PXS0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/E3PXS0.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:24.300124Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): E3PXS0, Glycine reductase component C subunit
    beta; primary genes grdC, synonyms none, taxon499177. Native annotation evidence
    distinguishes measured and inferred claims. This protein response independently
    supplies its own family cross-references.'
  snapshot_sha256: 0fca09878d1c4d29762c5a0396ad6495a770045746af205c7bb7889ebcb55478
- evidence_id: complex56-agent-protein-E3PXS1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/E3PXS1.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:24.321707Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): E3PXS1, Glycine reductase component C subunit
    alpha; primary genes grdD, synonyms none, taxon499177. Native annotation evidence
    distinguishes measured and inferred claims. This protein response independently
    supplies its own family cross-references.'
  snapshot_sha256: 35a3b4be164761ced4f8e06b131f409d92d51f864c5cd5d3dfa549129b0d681c
- evidence_id: complex56-agent-protein-P26971
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P26971.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:23.574493Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P26971, Glycine/sarcosine/betaine reductase
    complex component A; primary genes grdA, synonyms none, taxon499177. Native annotation
    evidence distinguishes measured and inferred claims. This protein response independently
    supplies its own family cross-references.'
  snapshot_sha256: 473459705324f26bc1cafb09431d13d8f18f6653d2562f399f4a16172ab533c0
- evidence_id: complex56-agent-pmid-11271425
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11271425+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and available abstract
  accessed_at: '2026-10-22T06:56:28.127191Z'
  support: supports
  summary: 'MED11271425: Molecular analysis of the grd operon coding for genes of
    the glycine reductase and of the thioredoxin system from Clostridium sticklandii.
    Graentzdoerffer A, Pich A, Andreesen JR. (2001), DOI10.1007/s002030000232. Exact
    metadata and the entire available native abstract read; primary-body access is
    not implied.'
  snapshot_sha256: 114e949dc8f471c3b53f1a17bb6bcc52d0e9f2562a1c004ea3816ee869e3d169
- evidence_id: complex56-agent-pmid-1429431
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1429431+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and available abstract
  accessed_at: '2026-10-22T06:56:28.130117Z'
  support: supports
  summary: 'MED1429431: Clostridium sticklandii glycine reductase selenoprotein A
    gene: cloning, sequencing, and expression in Escherichia coli. Garcia GE, Stadtman
    TC. (1992), DOI10.1128/jb.174.22.7080-7089.1992. Exact metadata and the entire
    available native abstract read; primary-body access is not implied.'
  snapshot_sha256: 79c4c38fe097a83f94bca633b65846a214b6f0358759ac38ea5a23fc63e5fff6
- evidence_id: complex56-agent-pmid-2018775
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2018775+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and available abstract
  accessed_at: '2026-10-22T06:56:27.956233Z'
  support: supports
  summary: 'MED2018775: Mechanism of action of clostridial glycine reductase: isolation
    and characterization of a covalent acetyl enzyme intermediate. Arkowitz RA, Abeles
    RH. (1991), DOI10.1021/bi00230a039. Exact metadata and the entire available native
    abstract read; primary-body access is not implied. The native abstract is explicitly
    truncated at250 words.'
  snapshot_sha256: af48a5081bd6b75355b6d245ff521ede3f66a49fbfcb20ad2f11177377861406
- evidence_id: complex56-agent-pmid-2963330
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A2963330+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and available abstract
  accessed_at: '2026-10-22T06:56:28.552478Z'
  support: supports
  summary: 'MED2963330: Selenoprotein A of the clostridial glycine reductase complex:
    purification and amino acid sequence of the selenocysteine-containing peptide.
    Sliwkowski MX, Stadtman TC. (1988), DOI10.1073/pnas.85.2.368. Exact metadata and
    the entire available native abstract read; primary-body access is not implied.'
  snapshot_sha256: 9672e152b33e73beac75cb3f5f90b0b795d2d13280f3fe36095c356c8f0e019b
- evidence_id: complex56-agent-ipr-IPR006812
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006812/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:56:26.866276Z'
  support: supports
  summary: IPR006812 is the glycine/sarcosine/betaine reductase component A family;
    its shared substrate-system scope does not invalidate the named A class.
  snapshot_sha256: e54ac2b01f90a53874a397af16443f0adea917750ea717e7bd828f2cb4daf35f
- evidence_id: complex56-agent-ipr-IPR010186
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010186/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:56:27.128205Z'
  support: supports
  summary: IPR010186 is the glycine-reductase selenoprotein B family, distinct from
    other substrate-specific B classes.
  snapshot_sha256: 0d78a74573c0ff9cd66c1cc1b37088888b95dc9ac76f71f3985b3be96ffb0db8
- evidence_id: complex56-agent-ipr-IPR017236
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017236/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:57:15.363853Z'
  support: supports
  summary: IPR017236 is the component C beta-subunit family shared across glycine,
    sarcosine and betaine reductase systems, rather than merely a broad CoA-transferase
    signature.
  snapshot_sha256: 243ce8caa83fe8e192f0fc42fbf858e610259cc9cdf56233c36f2a4a1b6a19c9
- evidence_id: complex56-agent-ipr-IPR012116
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012116/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:57:15.373213Z'
  support: supports
  summary: IPR012116 is the component C alpha-subunit family shared across glycine,
    sarcosine and betaine reductase systems. It does not denote the complete two-chain
    protein C complex.
  snapshot_sha256: 82358ac585c15752350b416e4736a392e7d4682ff1a77a35dc2482c40a9dab98
- evidence_id: complex56-agent-sliwkowski1988-page-368
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/7a27be3b71d9/pnas00254-0077.png
  locator: 'Printed p368: Title/abstract, Introduction, Methods through amino-acid
    analysis. Genuine native page scan visually read.'
  accessed_at: '2026-10-22T07:04:04.345936Z'
  support: supports
  summary: The title/abstract identify a protein-sequencing study; Methods chemically
    carboxamidomethylate purified protein A with iodoacetamide before peptide analysis.
  snapshot_sha256: 641030711ec8d4bf21aed9ee1dee6928ad7deccb4690cd1f848eb00bb454a0a2
- evidence_id: complex56-agent-sliwkowski1988-page-369
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/e7b84131f11c/pnas00254-0078.png
  locator: 'Printed p369: Methods continuation, Results opening and Fig1 pixels/caption.
    Genuine native page scan visually read.'
  accessed_at: '2026-10-22T07:04:04.346040Z'
  support: supports
  summary: Protease digestion, chromatographic purification and sequencing methods
    and initial Results analyze chemically labeled selenium-containing peptides.
  snapshot_sha256: 2158916ea4a554684c437bb06bdbd5b15223472643f394207316e6ae97620b35
- evidence_id: complex56-agent-sliwkowski1988-page-370
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/8298cc39c8af/pnas00254-0079.png
  locator: 'Printed p370: Complete Results page, Tables1/2 and Fig2 pixels/caption.
    Genuine native page scan visually read.'
  accessed_at: '2026-10-22T07:04:04.521743Z'
  support: supports
  summary: Results sequence the labeled selenium-containing peptides, with amino-acid
    compositions and purification chromatograms. Tables and Fig2 concern carboxamidomethylated
    protein A preparations.
  snapshot_sha256: 7da277e12eae22c608d43f17b448d1ee2d9ec5778b5684cc69ac0fcfb8488fcd
- evidence_id: complex56-agent-sliwkowski1988-page-371
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3362/279549/fcddb6b45c63/pnas00254-0080.png
  locator: 'Printed p371: Complete Discussion; reference list inspected only for context.
    Genuine native page scan visually read.'
  accessed_at: '2026-10-22T07:04:04.615345Z'
  support: supports
  summary: Discussion explicitly leaves the precise catalytic function of protein
    A unresolved and proposes a redox-center interpretation. This is not a demonstration
    of the catalytic carboxymethyl transfer intermediate.
  snapshot_sha256: 7fed48d82f3445c0a5f3cc365a55358229ead01932233bfa5a9a85fa2aae3f24
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/glycine_reductase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/glycine_reductase_complex.yaml'
  snapshot_sha256: 271875039195eaeb6437100e2b3ce0a26e8a1a87762ec1ab1ca86a2ed5753167
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/glycine_reductase_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/glycine_reductase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_reductase_complex-strict.tsv"
  snapshot_sha256: 1a424ca84beb8168c5ad80e7144472a56ec2750c97823df7d2b87f0c219b10d6
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:03:35.646959Z'
  support: supports
  summary: "data/structures/other/glycine_reductase_complex.yaml  (GO:0030700)\n \
    \ glycine_reductase_catalytic_transfer\tgrdb_selenoprotein_b\tCOVERED\t->grdb_selenoprotein_b\
    \ (UniProtKB:E3PXR9)\n  glycine_reductase_catalytic_transfer\tgrda_selenoprotein_a\t\
    COVERED\t->grda_selenoprotein_a (UniProtKB:P26971)\n  glycine_reductase_catalytic_transfer\t\
    grdc_protein_c\tCOVERED\t->grdc_protein_c (UniProtKB:E3PXS0, UniProtKB:E3PXS1)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 159237b036cf599c932eb3d688f6d3332796e5571b4571cf833337285154118b
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_reductase_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:03:37.031169Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/glycine_reductase_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 18 collected target identifiers returned OK. PMID:11271425: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:1429431: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:2018775: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:2963330: UNREACHABLE;
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
  topic: Three named components and the two-chain C boundary
  outcome: supported
  target_ids:
  - GO:0030700
  summary: GO identity, parent and function agree. The A/B/C naming convention is
    compatible with two distinct C-chain genes; the grouped C component is not equated
    to either accession alone. Reviewed A and explicitly unreviewed B/C examples retain
    their native identity/status.
  evidence_ids:
  - record
  - complex56-agent-go
  - complex56-agent-GO0030700-ancestors
  - complex56-agent-pmid-11271425
  - complex56-agent-pmid-1429431
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  - complex56-agent-ipr-IPR006812
  - complex56-agent-ipr-IPR010186
  - complex56-agent-ipr-IPR017236
  - complex56-agent-ipr-IPR012116
- assessment_id: grounding
  area: grounding
  topic: Exact C-chain families versus whole C-complex mapping
  outcome: concern
  target_ids:
  - GO:0030700
  summary: The maintained statement that verified C matches are only broader CoA-transferase
    signatures is inaccurate. Specific reductase-C alpha/beta chain families exist
    across glycine, sarcosine and betaine systems and match the separate native proteins.
    Neither one alone grounds the retained PROTEIN_COMPLEX row; label-only can remain
    pending a whole-complex identifier or justified subunit split.
  evidence_ids:
  - record
  - curation
  - complex56-agent-ipr-IPR006812
  - complex56-agent-ipr-IPR010186
  - complex56-agent-ipr-IPR017236
  - complex56-agent-ipr-IPR012116
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
- assessment_id: scope
  area: scope
  topic: Clostridial source and current strain taxonomy
  outcome: supported
  target_ids:
  - GO:0030700
  summary: Native499177 is Acetoanaerobium sticklandii DSM519, with Clostridium sticklandii
    DSM519 as synonym. The proteins independently carry that strain identity; the
    inspected2001 abstract establishes C.sticklandii operon membership but its full
    strain Methods were unavailable. The1988 study is a C.sticklandii purified-protein
    experiment.
  evidence_ids:
  - record
  - complex56-agent-pmid-11271425
  - complex56-agent-tax-499177
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  - complex56-agent-sliwkowski1988-page-368
  - complex56-agent-sliwkowski1988-page-369
  - complex56-agent-sliwkowski1988-page-370
  - complex56-agent-sliwkowski1988-page-371
- assessment_id: graph
  area: graph
  topic: Catalytic transfer supported separately from the mislabeled sequencing source
  outcome: concern
  target_ids:
  - GO:0030700
  summary: Arkowitz1991 available abstract supports generation of Se-carboxymethyl
    protein A, acetyl protein C and phosphate exchange; the native A annotation independently
    supports the transfer pathway. The1988 sequencing study instead chemically carboxamidomethylates
    protein A for analysis and reports analytical carboxymethyl derivatives in its
    amino-acid tables. The maintained edge note says residue, not intermediate; placing
    that sequencing citation under catalytic transfer does not demonstrate the transfer.
    The separately supported reaction is retained.
  evidence_ids:
  - record
  - complex56-agent-go
  - complex56-agent-pmid-2018775
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  - complex56-agent-sliwkowski1988-page-368
  - complex56-agent-sliwkowski1988-page-369
  - complex56-agent-sliwkowski1988-page-370
  - complex56-agent-sliwkowski1988-page-371
- assessment_id: formation
  area: grounding
  topic: Catalytic competence is distinct from complex formation
  outcome: unknown
  target_ids:
  - GO:0030700
  summary: The inspected catalytic, sequence and operon evidence does not independently
    establish universal physical formation necessity of each named component. UNKNOWN
    is retained without converting activity into assembly requirement.
  evidence_ids:
  - record
  - schema
  - complex56-agent-pmid-2018775
  - complex56-agent-pmid-11271425
  - complex56-agent-sliwkowski1988-page-368
  - complex56-agent-sliwkowski1988-page-369
  - complex56-agent-sliwkowski1988-page-370
  - complex56-agent-sliwkowski1988-page-371
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded evidence coverage
  outcome: supported
  target_ids:
  - GO:0030700
  summary: Every maintained field, evidence note, graph statement and discussion was
    inspected at the declared source extents. Optional inventories and unmeasured
    formation requirements are not invented from native validation.
  evidence_ids:
  - record
  - schema
  - curation
  - complex56-agent-go
findings:
- finding_id: F1
  issue_key: glycine-c-family-rationale
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the protein C family-grounding rationale
  description: The current C grounding note says its verified matches are only broad
    CoA-transferase signatures. Native IPR017236 and IPR012116 identify specific beta
    and alpha protein C chains shared across glycine/sarcosine/betaine reductase systems.
    They are not glycine-exclusive families. The grouped-complex boundary still prevents
    substituting either single-chain family as the whole C identifier.
  target_ids:
  - GO:0030700
  field_paths:
  - components#grdc_protein_c.grounding_notes
  - discussions#resolve_grdc_grounding
  evidence_ids:
  - record
  - curation
  - complex56-agent-ipr-IPR006812
  - complex56-agent-ipr-IPR010186
  - complex56-agent-ipr-IPR017236
  - complex56-agent-ipr-IPR012116
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_reductase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding and source-backed completeness
  native_severity: minor
  normalization_reason: The complex identity and constituent roles remain correct;
    the issue is a bounded existing grounding deferral, not a changed biological class.
- finding_id: F2
  issue_key: glycine-sequencing-source-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish chemical labeling from the catalytic intermediate
  description: The first transfer edge attributes characterization of the carboxymethylated
    selenocysteine residue to PMID2963330. The actual study chemically carboxamidomethylates
    purified protein A with iodoacetamide for peptide sequencing, reports analytical
    derivatives, and leaves its precise catalytic function unresolved. The note says
    residue rather than intermediate; its placement under catalytic transfer does
    not establish that reaction. Separate evidence supports the catalytic model.
  target_ids:
  - GO:0030700
  field_paths:
  - causal_graphs#glycine_reductase_catalytic_transfer.edges[0].evidence
  evidence_ids:
  - record
  - complex56-agent-pmid-2018775
  - complex56-agent-sliwkowski1988-page-368
  - complex56-agent-sliwkowski1988-page-369
  - complex56-agent-sliwkowski1988-page-370
  - complex56-agent-sliwkowski1988-page-371
  - complex56-agent-protein-E3PXR9
  - complex56-agent-protein-E3PXS0
  - complex56-agent-protein-E3PXS1
  - complex56-agent-protein-P26971
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_reductase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding and source-backed completeness
  native_severity: minor
  normalization_reason: The reaction and complex identity remain supported. This is
    a bounded citation-note/source-placement error, not evidence that the catalytic
    pathway is false.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030700
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_reductase_complex.yaml
    role: maintained scientific record
  description: Replace the inaccurate broad-signature rationale with the verified
    two-chain families and their shared glycine/sarcosine/betaine scope; retain label-only
    for the combined complex unless a source-backed split or exact complex identifier
    is chosen.
  acceptance_checks:
  - Keep E3PXS0/grdC beta and E3PXS1/grdD alpha distinct.
  - Do not force a single family onto the whole protein C complex.
  - Preserve supported identities and source scope; pass applicable native gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0030700
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_reductase_complex.yaml
    role: maintained scientific record
  description: Correct the1988 note to its protein-sequencing/chemical-labeling scope
    and use a directly relevant catalytic source for the transfer edge, retaining
    supported reaction direction.
  acceptance_checks:
  - Distinguish the chemical labeling/sequence analysis and analytical derivatives
    from evidence demonstrating catalytic carboxymethyl transfer.
  - Keep PMID2963330 as sequence evidence where appropriate; preserve the independently
    supported catalytic model.
  - Preserve supported identities and source scope; pass applicable native gates.
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified. The sparse B56 checkout was not used to claim a new full-site QC
  run.
- No supplements or atomic coordinates were independently analyzed. Actual source
  reading is limited to the exact locators below.
- Arkowitz1991 publisher returned403; its native abstract is truncated at250 words.
  Graentzdoerffer2001 publisher returned200 ClientChallenge. Garcia1992 modern PMC
  exposes abstract/page assets but its full scanned body was not read.
- Sliwkowski1988 legacy route returned200 CAPTCHA, but four genuine separately hashed
  native scans368–371 were visually read in full. Its Discussion is not promoted into
  later catalytic proof.
- The2001 full Methods strain designation was not independently inspected; DSM519
  identity is separately supported by native proteins/taxonomy.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
