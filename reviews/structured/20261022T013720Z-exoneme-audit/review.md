# Exoneme identity, source scope and claim review

- Review: 20261022T013720Z-exoneme-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:18:46Z
- Finished UTC: 2026-10-22T01:37:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding resolves the exact SUB1 family while preserving the qualified PMX mechanism.

## Scope And Provenance

Whole single target with native identity/taxon checks, all component/formation claims, evidence placement, function and graph audit; source reading scopes enumerated per evidence row.

Selection: Target 8 of batch twenty-eight in strict uncovered path order; fresh f97b1abe initial native inspection/schema/strict gates passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044311 | data/structures/membrane_organelle/exoneme.yaml | maintained | exoneme |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0044311 | Focused validator passed. |
| Focused native strict | passed | True | GO:0044311 | Focused validator passed. |
| Focused native verify | passed | True | GO:0044311 | Focused native checks passed; scientific source/identity limits are assessed independently. |
| Focused native causal-graphs | passed | True | GO:0044311 | Focused native checks passed; scientific source/identity limits are assessed independently. |
| Expression-module applicability | not_applicable | False | GO:0044311 | No expression-module membership or regulatory transcriptomic claim is used in this record review. |
| Claim-level scientific review | passed | True | GO:0044311 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0044311 | 13 of 14 collected target identifiers returned OK. PMID:9722575: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9722575, DOI10.1074/jbc.273.36.23398 and A subtilisin-like protein in secretory organelles of Plasmodium falciparum merozoites. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0044311 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0044311 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0044311 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0044311 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0044311 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exoneme organelle and apical-complex relation

identity: supported. Targets: GO:0044311.

The native class/parent/parthood match. The maintained functions correctly describe discharge of soluble protease cargo into PV rather than assuming an entire stable organelle is released intact; full-record interpretation preserves this distinction.

### P. falciparum blood-stage evidence

scope: supported. Targets: GO:0044311.

The directly evidenced species, schizont/merozoite stages and canonical discharge/egress example match the primary abstract and later primary main text. COMMON is qualitative occurrence, not a counted frequency or all-apicomplexan claim. The record explicitly narrowed broader historical taxonomy.

### SUB1 and PMX components versus representative identity metadata

grounding: supported. Targets: GO:0044311.

Primary literature supports PfSUB1 exoneme cargo and PMX localization/dependence. Native examples and graph xrefs identify the exact species/isolate proteins and SERA5/MSP1 exemplars; xrefs do not equate the entire substrate cohort with just those two proteins. Native by-similarity annotations and historical dense-granule descriptions are not counted as independent direct exoneme experiments.

### Resolvable SUB1 family and unresolved exact PMX family

grounding: concern. Targets: GO:0044311.

IPR017314 is a verified whole-SUB1 family and O61142 directly carries it. The component’s unresolved-family rationale is stale for SUB1. IPR034204 is a domain and IPR001461 is broader than PMX, so neither is forced as an exact substitute for the remaining component.

### Protease activity requirement versus organelle formation

grounding: unknown. Targets: GO:0044311.

The studies establish important protease maturation, egress and invasion effects, but do not establish that loss of each cargo enzyme prevents formation of the exoneme compartment. Both UNKNOWN assembly-necessity entries are appropriate; catalytic essentiality is not silently converted to organelle-assembly necessity.

### Eight qualified egress pathway edges

graph: supported. Targets: GO:0044311.

Localization/storage, discharge into PV, PMX-supported SUB1 processing, downstream SERA/MSP processing and contributions to egress/invasion are supported at the stated evidence tiers. Nasamu directly supports the dependence, while its in-vivo direct-cleavage uncertainty is preserved by “supports maturation.” Withers provides reviewed background for discharge and substrate processing inside a primary structural paper, not an independent new discharge experiment. This graph represents a causal proteolytic sequence and its MECHANISTIC classification is justified within those limits.

### Full maintained record and bounded scientific coverage

completeness: supported. Targets: GO:0044311.

Every maintained claim, graph edge and discussion was inspected. No quantitative physical-property field, maintained image/licence asset or verbatim evidence snippet is present. Existing PROPOSED status and history remain unchanged. No finding is invented from optional unresolved molecular inventory or unavailable full-text routes alone.

## Findings

### F1: Resolve the verified SUB1 family instead of retaining an unresolved-family rationale

minor / open / confirmed; issue key: exoneme-sub1-family-grounding-gap.

The PfSUB1 component and shared TODO say no exact source-neutral family was resolved. Native IPR017314 is a Plasmodium SUB1 protein family and is directly linked by the exact O61142 example, so SUB1 can now be grounded without inferring localization from the family. Domain-only IPR034204 and broad PMX-family candidates do not resolve the other component.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation change, ground SUB1 to the verified IPR017314 family and narrow the TODO to unresolved PMX or other genuinely open identity questions; retain primary membership evidence and UNKNOWN assembly necessity.

- Verify the exact family ID/label pair against current native InterPro and run product/schema/strict checks.
- Keep the existing accession/taxon pairing and primary membership evidence; a family mapping alone does not prove exoneme localization.
- Do not replace PMX with a broad A1 family or use a catalytic domain as whole-protein identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/exoneme.yaml; Entire maintained YAML, all fields, evidence notes, discussions, history and graph edges | context_only | The whole single target was read without editing scientific content or promoting its native status. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, essentiality, ProteinExample, xrefs and graph contracts; frozen local review rubric | context_only | Structure identity, molecular family, domain and individual protein are distinct. Assembly necessity is separate from observed membership and catalytic requirement. A whole bilayer material is not an individual lipid species. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Primary-evidence requirement for mechanistic claims and prohibition on inferring causality from association | context_only | A descriptive constituent/topological relation does not by itself establish a molecular causal mechanism; mechanistic scope is assessed separately from biological correctness of the constituent relations. |
| exoneme-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044311,GO:0043231,GO:0020007; All three exact identifiers, definitions, active flags and relevant child relations | supports | Active GO0044311 matches the exoneme definition; GO0043231 lists it as an is_a child and GO0020007 lists it as part_of the apical complex. |
| exoneme-agent-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies tax5833 as Plasmodium falciparum, species. |
| exoneme-agent-tax36329 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies tax36329 as Plasmodium falciparum3D7, isolate rank. |
| exoneme-agent-yeoh2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2007.10.049; Exact bibliographic identity and complete primary abstractText | supports | Native MED identifies Subcellular discharge of a serine protease mediates release of invasive malaria parasites from host erythrocytes. by Yeoh S, O'Donnell RA, Koussis K, Dluzewski AR, Ansell KH, Osborne SA, Hackett F, Withers-Martinez C, Mitchell GH, Bannister LH, Bryans JS, Kettleborough CA, Blackman MJ. (2007), DOI10.1016/j.cell.2007.10.049, PMID18083098. The complete primary abstract reports PfSUB1 discharge from newly identified exonemes into PV just before egress, SERA maturation, blockade of egress and reduced invasive capacity. No full body is claimed. |
| exoneme-agent-blackman1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9722575%20AND%20SRC%3AMED; Exact bibliographic identity and complete primary abstractText | supports | Native MED identifies A subtilisin-like protein in secretory organelles of Plasmodium falciparum merozoites. by Blackman MJ, Fujioka H, Stafford WH, Sajid M, Clough B, Fleck SL, Aikawa M, Grainger M, Hackett F. (1998), DOI10.1074/jbc.273.36.23398, PMID9722575. The complete primary abstract identifies pfsub-1, secretory transport and mature protease in apical dense granules. Its historical secretion interpretation is not used to override the later exoneme/PV work. |
| exoneme-agent-blackman2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/j.1462-5822.2008.01176.x; Exact bibliographic identity; detailed claims use the separately inspected body | supports | Native MED identifies Malarial proteases and host cell egress: an 'emerging' cascade. by Blackman MJ. (2008), DOI10.1111/j.1462-5822.2008.01176.x, PMID18503638.  |
| exoneme-agent-withers2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms4726; Exact bibliographic identity; detailed claims use the separately inspected body | supports | Native MED identifies The malaria parasite egress protease SUB1 is a calcium-dependent redox switch subtilisin. by Withers-Martinez C, Strath M, Hackett F, Haire LF, Howell SA, Walker PA, Christodoulou E, Dodson GG, Blackman MJ. (2014), DOI10.1038/ncomms4726, PMID24785947.  |
| exoneme-agent-nasamu2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.aan1478; Exact bibliographic identity; detailed claims use the separately inspected body | supports | Native MED identifies Plasmepsins IX and X are essential and druggable mediators of malaria parasite egress and invasion. by Nasamu AS, Glushakova S, Russo I, Vaupel B, Oksman A, Kim AS, Fremont DH, Tolia N, Beck JR, Meyers MJ, Niles JC, Zimmerberg J, Goldberg DE. (2017), DOI10.1126/science.aan1478, PMID29074774.  |
| exoneme-agent-blackman2008-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2610400/fullTextXML; Complete subsection “SERA processing by SUB1: an activation event?” within Candidate proteases; surrounding candidate-section portions were consulted, not all review body independently certified. | supports | This review summarizes Yeoh2007 exoneme localization, release of soluble PfSUB1 into PV before egress and SERA processing. Proposed SERA activation and other downstream interpretations are retained as review-level interpretations, not new experiments. |
| exoneme-agent-withers2014-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4024747/fullTextXML; All five pre-Results introductory paragraphs and complete Discussion sec5. Results, detailed Methods, figure pixels and supplement not independently inspected for this review. | supports | The primary structural paper Introduction describes SUB1 exoneme storage and release into PV minutes before egress, with cleavage of surface/PV substrates. The complete Discussion interprets an in-vitro redox switch and explicitly makes exoneme reducing conditions hypothetical. The maintained record uses the discharge context, not that unproven in-vivo redox model. |
| exoneme-agent-nasamu2017-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5928414/fullTextXML; Entire scientific main body (all paragraphs) and Fig1–4 captions; primary figure pixels and separate Supplementary Materials/Methods not inspected. Fig4 caption identifies parental NF54; no uninspected strain-specific experiment is recast as3D7. | supports | Complete primary main text reports PMX exoneme localization by immuno-EM/colocalization, knockdown and catalytic-mutant effects on final SUB1 maturation, SERA5/MSP1 processing and egress/invasion. Recombinant cleavage occurs in vitro, but the discussion explicitly leaves direct final cleavage versus indirect prodomain relief in vivo unresolved. The maintained “supports maturation” wording respects this uncertainty. |
| exoneme-agent-O61142 | https://rest.uniprot.org/uniprotkb/O61142.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry O61142 is Subtilisin-like protease 1, taxon5833; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. Secreted localization cites PMID9722575 with ECO0000269; PV lumen is by similarity to Q8I0V0. IPR017314 is a native family cross-reference. |
| exoneme-agent-Q8IAS0 | https://rest.uniprot.org/uniprotkb/Q8IAS0.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q8IAS0 is Plasmepsin X, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. Secretory-vesicle localization is by similarity to W7JWW5, not an additional direct experiment in this metadata. |
| exoneme-agent-Q9TY95 | https://rest.uniprot.org/uniprotkb/Q9TY95.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q9TY95 is Serine-repeat antigen protein 5, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. |
| exoneme-agent-Q8I0U8 | https://rest.uniprot.org/uniprotkb/Q8I0U8.json; Accession, reviewed status, recommended name, gene/ORF tokens, organism and relevant localization evidence/InterPro cross-references | supports | Native reviewed entry Q8I0U8 is Merozoite surface protein 1, taxon36329; exact gene/ORF tokens and entry status match the maintained example or graph cross-reference. |
| exoneme-agent-sub1-query | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asub1%29%20AND%20%28taxonomy_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact query and all three returned reviewed accession/taxon/gene rows | supports | The returned reviewed SUB1 entries are O61142 at species5833, Q8I0V0 at3D7/36329 and W7K9M0 atNF54/5843. Exactly one result is at the maintained species taxon; descendant-isolate entries are not falsely excluded. |
| exoneme-agent-pmx-query | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apmx%29%20AND%20%28taxonomy_id%3A36329%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact query and complete single returned accession/taxon/gene row | supports | The exact reviewed PMX query for3D7 returns Q8IAS0, supporting the record’s uniqueness note at that taxon. |
| exoneme-agent-IPR017314 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017314/; metadata accession, type=family, name and complete non-LLM description | supports | InterPro explicitly types IPR017314 as a protein family for Plasmodium subtilisin-like peptidase1/SUB1. This matches the complete SUB1 molecular identity represented by the component; it is not merely an exoneme-location ontology term. |
| exoneme-agent-IPR034204 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034204/; metadata accession, type=domain, name, description and listed scope | supports | IPR034204 is a catalytic domain, including related non-Plasmodium proteins, and is not an exact whole-SUB1 family substitute. |
| exoneme-agent-IPR001461 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001461/; metadata accession, family name/type and description | supports | IPR001461 is the broad pepsin/A1 family; its scope is wider than the exact PMX component. No exact PMX-family grounding is established by this candidate. |
| exoneme-agent-yeoh2007-citeseer | https://citeseerx.ist.psu.edu/document?doi=9056f004262f006f094611bf9092a37860ed0f11&amp;repid=rep1&amp;type=pdf; Actual access response; not an inspected scientific body | context_only | Citeseer request redirected to a historical archive and returnedHTTP404 HTML, not a usable PDF. |
| exoneme-agent-yeoh2007-cell-pdf | https://www.cell.com/cell/pdf/S0092-8674(07)01403-1.pdf; Actual access response; not an inspected scientific body | context_only | Publisher PDF request returnedHTTP403 HTML; Yeoh primary-body access remains unavailable. |
| exoneme-agent-blackman1998-jbc-pdf | https://www.jbc.org/article/S0021925819750030/pdf; Actual access response; not an inspected scientific body | context_only | Publisher PDF request returnedHTTP403 HTML; the exact native abstract and UniProt localization evidence are the inspected scopes. |
| schema-result | just validate data/structures/membrane_organelle/exoneme.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/exoneme.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/exoneme.yaml --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/exoneme.yaml --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/exoneme.yaml; Complete native focused output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/exoneme.yaml; Complete native focused output | supports | data/structures/membrane_organelle/exoneme.yaml  (GO:0044311)<br>  pmx_sub1_exoneme_egress	plasmepsin_x_exoneme_protease	COVERED	-&gt;plasmepsin_x_exoneme_protease (UniProtKB:Q8IAS0)<br>  pmx_sub1_exoneme_egress	pfsub1_exoneme_protease	COVERED	-&gt;pfsub1_exoneme_protease (UniProtKB:O61142)<br>  pmx_sub1_exoneme_egress	sera_msp_substrates	UNANCHORED_WITH_UNIPROT	SERA and MSP substrates (UniProtKB:Q9TY95, UniProtKB:Q8I0U8)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/exoneme.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 14 collected target identifiers returned OK. PMID:9722575: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9722575, DOI10.1074/jbc.273.36.23398 and A subtilisin-like protein in secretory organelles of Plasmodium falciparum merozoites. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Yeoh2007 and Blackman1998 are inspected as complete native primary abstracts, not full bodies; actual publisher403 and Citeseer404 responses are retained. Other full primary/review sources provide independently read support for the maintained claims.
- Blackman2008 is review-tier evidence. Withers2014 was read for all introductory paragraphs and complete Discussion, not every experimental section. Nasamu2017 complete scientific main text and captions were read, but figure pixels, raw data and separate supplementary Methods were not independently inspected.
- The primary PMX experiments include NF54, while Q8IAS0 is a3D7 representative and native secretory localization uses by-similarity evidence. Exact accession/taxon identity is verified; this review does not relabel NF54 experiments as direct3D7 instance measurements.
- The SERA/MSP node links representative proteins, not an exhaustive substrate inventory. Direct in-vivo PMX cleavage mechanism and individual exoneme-formation requirements remain unresolved.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requires a validated review for every uncovered target, including an honest clean review; no issue is invented to satisfy the local issue-only rule.
- All remote snapshots retain actual original URL, UTC access timestamp and raw SHA256. No maintained record or publication was modified.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013720Z-exoneme-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Exoneme identity, source scope and claim review
started_at: '2026-10-22T01:18:46Z'
finished_at: '2026-10-22T01:37:20Z'
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
summary: One minor finding resolves the exact SUB1 family while preserving the qualified
  PMX mechanism.
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
  - path: data/structures/membrane_organelle/exoneme.yaml
    sha256: 2e32d7ca2f38ab39d5e1eb57cf683833fed5fdf18337191a3302689058d3b4b4
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
- target_id: GO:0044311
  path: data/structures/membrane_organelle/exoneme.yaml
  label: exoneme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
scope:
  description: Whole single target with native identity/taxon checks, all component/formation
    claims, evidence placement, function and graph audit; source reading scopes enumerated
    per evidence row.
  selection: Target 8 of batch twenty-eight in strict uncovered path order; fresh
    f97b1abe initial native inspection/schema/strict gates passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0044311
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate data/structures/membrane_organelle/exoneme.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate-strict data/structures/membrane_organelle/exoneme.yaml --out
    /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/exoneme.yaml
  exit_code: 0
  summary: Focused native checks passed; scientific source/identity limits are assessed
    independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/exoneme.yaml
  exit_code: 0
  summary: Focused native checks passed; scientific source/identity limits are assessed
    independently.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0044311
  summary: No expression-module membership or regulatory transcriptomic claim is used
    in this record review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0044311
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - exoneme-agent-go
  - exoneme-agent-tax5833
  - exoneme-agent-tax36329
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-blackman1998-meta
  - exoneme-agent-blackman2008-meta
  - exoneme-agent-withers2014-meta
  - exoneme-agent-nasamu2017-meta
  - exoneme-agent-blackman2008-jats
  - exoneme-agent-withers2014-jats
  - exoneme-agent-nasamu2017-jats
  - exoneme-agent-O61142
  - exoneme-agent-Q8IAS0
  - exoneme-agent-Q9TY95
  - exoneme-agent-Q8I0U8
  - exoneme-agent-sub1-query
  - exoneme-agent-pmx-query
  - exoneme-agent-IPR017314
  - exoneme-agent-IPR034204
  - exoneme-agent-IPR001461
  - exoneme-agent-yeoh2007-citeseer
  - exoneme-agent-yeoh2007-cell-pdf
  - exoneme-agent-blackman1998-jbc-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0044311
  summary: '13 of 14 collected target identifiers returned OK. PMID:9722575: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9722575, DOI10.1074/jbc.273.36.23398 and A subtilisin-like protein
    in secretory organelles of Plasmodium falciparum merozoites. Bibliographic identity
    is resolved; scientific scope remains restricted to the separately documented
    abstract/body inspections. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - exoneme-agent-blackman1998-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0044311
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0044311
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
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/exoneme.yaml
  locator: Entire maintained YAML, all fields, evidence notes, discussions, history
    and graph edges
  accessed_at: '2026-10-22T01:30:24Z'
  support: context_only
  summary: The whole single target was read without editing scientific content or
    promoting its native status.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, essentiality, ProteinExample, xrefs and graph contracts;
    frozen local review rubric
  accessed_at: '2026-10-22T01:30:24Z'
  support: context_only
  summary: Structure identity, molecular family, domain and individual protein are
    distinct. Assembly necessity is separate from observed membership and catalytic
    requirement. A whole bilayer material is not an individual lipid species.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Primary-evidence requirement for mechanistic claims and prohibition on
    inferring causality from association
  accessed_at: '2026-10-22T01:30:24Z'
  support: context_only
  summary: A descriptive constituent/topological relation does not by itself establish
    a molecular causal mechanism; mechanistic scope is assessed separately from biological
    correctness of the constituent relations.
- evidence_id: exoneme-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044311,GO:0043231,GO:0020007
  locator: All three exact identifiers, definitions, active flags and relevant child
    relations
  accessed_at: '2026-10-22T01:21:53.019244Z'
  support: supports
  summary: Active GO0044311 matches the exoneme definition; GO0043231 lists it as
    an is_a child and GO0020007 lists it as part_of the apical complex.
  snapshot_sha256: 0755406ae14f6287bd46e603298ec29a1dda850cb8aaee3f7251b9198b85cc33
- evidence_id: exoneme-agent-tax5833
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:21:53.019556Z'
  support: supports
  summary: ENA identifies tax5833 as Plasmodium falciparum, species.
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
- evidence_id: exoneme-agent-tax36329
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:21:53.734776Z'
  support: supports
  summary: ENA identifies tax36329 as Plasmodium falciparum3D7, isolate rank.
  snapshot_sha256: 6d1389e6a3af3a09ef4bf23157b95ec8d94dac9b395b8f8ccf0d1952beddc306
- evidence_id: exoneme-agent-yeoh2007-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2007.10.049
  locator: Exact bibliographic identity and complete primary abstractText
  accessed_at: '2026-10-22T01:21:55.379019Z'
  support: supports
  summary: Native MED identifies Subcellular discharge of a serine protease mediates
    release of invasive malaria parasites from host erythrocytes. by Yeoh S, O'Donnell
    RA, Koussis K, Dluzewski AR, Ansell KH, Osborne SA, Hackett F, Withers-Martinez
    C, Mitchell GH, Bannister LH, Bryans JS, Kettleborough CA, Blackman MJ. (2007),
    DOI10.1016/j.cell.2007.10.049, PMID18083098. The complete primary abstract reports
    PfSUB1 discharge from newly identified exonemes into PV just before egress, SERA
    maturation, blockade of egress and reduced invasive capacity. No full body is
    claimed.
  snapshot_sha256: 2dca392ec8fc4c79b9b6aad4415eb0fd226ea8c40d15159aa992a3ef96792da0
- evidence_id: exoneme-agent-blackman1998-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9722575%20AND%20SRC%3AMED
  locator: Exact bibliographic identity and complete primary abstractText
  accessed_at: '2026-10-22T01:21:56.034434Z'
  support: supports
  summary: Native MED identifies A subtilisin-like protein in secretory organelles
    of Plasmodium falciparum merozoites. by Blackman MJ, Fujioka H, Stafford WH, Sajid
    M, Clough B, Fleck SL, Aikawa M, Grainger M, Hackett F. (1998), DOI10.1074/jbc.273.36.23398,
    PMID9722575. The complete primary abstract identifies pfsub-1, secretory transport
    and mature protease in apical dense granules. Its historical secretion interpretation
    is not used to override the later exoneme/PV work.
  snapshot_sha256: bd0d1f644f4060fb485d21b9b59b0d4d4e7d8abceb94bc74c76ecc50115d8d57
- evidence_id: exoneme-agent-blackman2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/j.1462-5822.2008.01176.x
  locator: Exact bibliographic identity; detailed claims use the separately inspected
    body
  accessed_at: '2026-10-22T01:21:55.404144Z'
  support: supports
  summary: 'Native MED identifies Malarial proteases and host cell egress: an ''emerging''
    cascade. by Blackman MJ. (2008), DOI10.1111/j.1462-5822.2008.01176.x, PMID18503638. '
  snapshot_sha256: fa821c52c129539f222294f4a681162c43fc6eadbb5fa608cbe48485cb9929bb
- evidence_id: exoneme-agent-withers2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms4726
  locator: Exact bibliographic identity; detailed claims use the separately inspected
    body
  accessed_at: '2026-10-22T01:21:55.531491Z'
  support: supports
  summary: 'Native MED identifies The malaria parasite egress protease SUB1 is a calcium-dependent
    redox switch subtilisin. by Withers-Martinez C, Strath M, Hackett F, Haire LF,
    Howell SA, Walker PA, Christodoulou E, Dodson GG, Blackman MJ. (2014), DOI10.1038/ncomms4726,
    PMID24785947. '
  snapshot_sha256: 211dfd6bb92adff1ba446a93338a123f6f260fd8d0332959eac41d7ccac6160e
- evidence_id: exoneme-agent-nasamu2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.aan1478
  locator: Exact bibliographic identity; detailed claims use the separately inspected
    body
  accessed_at: '2026-10-22T01:21:55.859455Z'
  support: supports
  summary: 'Native MED identifies Plasmepsins IX and X are essential and druggable
    mediators of malaria parasite egress and invasion. by Nasamu AS, Glushakova S,
    Russo I, Vaupel B, Oksman A, Kim AS, Fremont DH, Tolia N, Beck JR, Meyers MJ,
    Niles JC, Zimmerberg J, Goldberg DE. (2017), DOI10.1126/science.aan1478, PMID29074774. '
  snapshot_sha256: caaee89580068dd014c1ed51c05c6a6f5693ce5073fa8f89073ec58d5e488e59
- evidence_id: exoneme-agent-blackman2008-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2610400/fullTextXML
  locator: 'Complete subsection “SERA processing by SUB1: an activation event?” within
    Candidate proteases; surrounding candidate-section portions were consulted, not
    all review body independently certified.'
  accessed_at: '2026-10-22T01:22:20.827015Z'
  support: supports
  summary: This review summarizes Yeoh2007 exoneme localization, release of soluble
    PfSUB1 into PV before egress and SERA processing. Proposed SERA activation and
    other downstream interpretations are retained as review-level interpretations,
    not new experiments.
  snapshot_sha256: 899e36096d2da3dd306f447032b906fb28679042b098c4fbbc4f3b158508b496
- evidence_id: exoneme-agent-withers2014-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4024747/fullTextXML
  locator: All five pre-Results introductory paragraphs and complete Discussion sec5.
    Results, detailed Methods, figure pixels and supplement not independently inspected
    for this review.
  accessed_at: '2026-10-22T01:22:20.827149Z'
  support: supports
  summary: The primary structural paper Introduction describes SUB1 exoneme storage
    and release into PV minutes before egress, with cleavage of surface/PV substrates.
    The complete Discussion interprets an in-vitro redox switch and explicitly makes
    exoneme reducing conditions hypothetical. The maintained record uses the discharge
    context, not that unproven in-vivo redox model.
  snapshot_sha256: 1ce1e42f1c39c9a38ff32c749e6376a1f6053c91a6cd64f0163e2088197fc06f
- evidence_id: exoneme-agent-nasamu2017-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5928414/fullTextXML
  locator: Entire scientific main body (all paragraphs) and Fig1–4 captions; primary
    figure pixels and separate Supplementary Materials/Methods not inspected. Fig4
    caption identifies parental NF54; no uninspected strain-specific experiment is
    recast as3D7.
  accessed_at: '2026-10-22T01:22:20.827311Z'
  support: supports
  summary: Complete primary main text reports PMX exoneme localization by immuno-EM/colocalization,
    knockdown and catalytic-mutant effects on final SUB1 maturation, SERA5/MSP1 processing
    and egress/invasion. Recombinant cleavage occurs in vitro, but the discussion
    explicitly leaves direct final cleavage versus indirect prodomain relief in vivo
    unresolved. The maintained “supports maturation” wording respects this uncertainty.
  snapshot_sha256: 563825583d6aea2dffda29e592f303e3a4d5c9302b79dd4d321e5c12e65f898b
- evidence_id: exoneme-agent-O61142
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O61142.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-10-22T01:21:53.745641Z'
  support: supports
  summary: Native reviewed entry O61142 is Subtilisin-like protease 1, taxon5833;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
    Secreted localization cites PMID9722575 with ECO0000269; PV lumen is by similarity
    to Q8I0V0. IPR017314 is a native family cross-reference.
  snapshot_sha256: fa8b17256b77645b179d2c7dc6153036699ddff8481bba0b2e070982d9d84424
- evidence_id: exoneme-agent-Q8IAS0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8IAS0.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-10-22T01:21:53.768067Z'
  support: supports
  summary: Native reviewed entry Q8IAS0 is Plasmepsin X, taxon36329; exact gene/ORF
    tokens and entry status match the maintained example or graph cross-reference.
    Secretory-vesicle localization is by similarity to W7JWW5, not an additional direct
    experiment in this metadata.
  snapshot_sha256: b63747f066b55dcfb3a4884cb8647fa390225373879da2a2ba107cc7da15101f
- evidence_id: exoneme-agent-Q9TY95
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9TY95.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-10-22T01:21:53.790787Z'
  support: supports
  summary: Native reviewed entry Q9TY95 is Serine-repeat antigen protein 5, taxon36329;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
  snapshot_sha256: 09588e9def043b90658a1a3517fdca2750c2e2fb538a23b20d97eea0ef9b6471
- evidence_id: exoneme-agent-Q8I0U8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8I0U8.json
  locator: Accession, reviewed status, recommended name, gene/ORF tokens, organism
    and relevant localization evidence/InterPro cross-references
  accessed_at: '2026-10-22T01:21:54.337358Z'
  support: supports
  summary: Native reviewed entry Q8I0U8 is Merozoite surface protein 1, taxon36329;
    exact gene/ORF tokens and entry status match the maintained example or graph cross-reference.
  snapshot_sha256: 40831b7d4689247dc2f789bdb59dd82111e28978e9495d5a477c7d8816e8f6e2
- evidence_id: exoneme-agent-sub1-query
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asub1%29%20AND%20%28taxonomy_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact query and all three returned reviewed accession/taxon/gene rows
  accessed_at: '2026-10-22T01:22:22.855252Z'
  support: supports
  summary: The returned reviewed SUB1 entries are O61142 at species5833, Q8I0V0 at3D7/36329
    and W7K9M0 atNF54/5843. Exactly one result is at the maintained species taxon;
    descendant-isolate entries are not falsely excluded.
  snapshot_sha256: 74f4dbfe3b78df7a5201dd97636e6d959cbe6fd510342ddc9adcc02397ec02e4
- evidence_id: exoneme-agent-pmx-query
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apmx%29%20AND%20%28taxonomy_id%3A36329%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact query and complete single returned accession/taxon/gene row
  accessed_at: '2026-10-22T01:22:22.926919Z'
  support: supports
  summary: The exact reviewed PMX query for3D7 returns Q8IAS0, supporting the record’s
    uniqueness note at that taxon.
  snapshot_sha256: 6a076771ec70cab9b0e882587c6ff30d9b5ead4bec9c34531bb21710d396d4f1
- evidence_id: exoneme-agent-IPR017314
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017314/
  locator: metadata accession, type=family, name and complete non-LLM description
  accessed_at: '2026-10-22T01:22:57.075883Z'
  support: supports
  summary: InterPro explicitly types IPR017314 as a protein family for Plasmodium
    subtilisin-like peptidase1/SUB1. This matches the complete SUB1 molecular identity
    represented by the component; it is not merely an exoneme-location ontology term.
  snapshot_sha256: 00de8b05b5da0a21adef9fd1db82c9c36b0bed42093f921563b3a7733a91ba68
- evidence_id: exoneme-agent-IPR034204
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034204/
  locator: metadata accession, type=domain, name, description and listed scope
  accessed_at: '2026-10-22T01:22:57.075835Z'
  support: supports
  summary: IPR034204 is a catalytic domain, including related non-Plasmodium proteins,
    and is not an exact whole-SUB1 family substitute.
  snapshot_sha256: 21b4d4ef4ab3318beff2031ec322b95f1468565b12628cec1c9d98652815a7c8
- evidence_id: exoneme-agent-IPR001461
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001461/
  locator: metadata accession, family name/type and description
  accessed_at: '2026-10-22T01:22:57.963514Z'
  support: supports
  summary: IPR001461 is the broad pepsin/A1 family; its scope is wider than the exact
    PMX component. No exact PMX-family grounding is established by this candidate.
  snapshot_sha256: 7919edb7b7f8dd8968ee8b4babe8743c81eae2e921932e1372a14a8d6f77bd09
- evidence_id: exoneme-agent-yeoh2007-citeseer
  kind: authority
  reference: https://citeseerx.ist.psu.edu/document?doi=9056f004262f006f094611bf9092a37860ed0f11&repid=rep1&type=pdf
  locator: Actual access response; not an inspected scientific body
  accessed_at: '2026-10-22T01:22:22.573864Z'
  support: context_only
  summary: Citeseer request redirected to a historical archive and returnedHTTP404
    HTML, not a usable PDF.
  snapshot_sha256: d08ee3aff262931847baf01164908eeb6b821c3e3241ccbf3e89e26c89da42e7
- evidence_id: exoneme-agent-yeoh2007-cell-pdf
  kind: authority
  reference: https://www.cell.com/cell/pdf/S0092-8674(07)01403-1.pdf
  locator: Actual access response; not an inspected scientific body
  accessed_at: '2026-10-22T01:28:24.287094Z'
  support: context_only
  summary: Publisher PDF request returnedHTTP403 HTML; Yeoh primary-body access remains
    unavailable.
  snapshot_sha256: 7b5ba9f24d0392801f435fe7c397b99fa641ed4587744abd4a8f81149b7ecca5
- evidence_id: exoneme-agent-blackman1998-jbc-pdf
  kind: authority
  reference: https://www.jbc.org/article/S0021925819750030/pdf
  locator: Actual access response; not an inspected scientific body
  accessed_at: '2026-10-22T01:28:24.287569Z'
  support: context_only
  summary: Publisher PDF request returnedHTTP403 HTML; the exact native abstract and
    UniProt localization evidence are the inspected scopes.
  snapshot_sha256: 8c923ad15f709322be4b83aa44db1370f6752caee54d7bd194320aa2863ed6ce
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/exoneme.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:18:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/exoneme.yaml'
  snapshot_sha256: c804d1d84e67cee55e28e04e50f2f9b900bbd4e0d9aa0b037ac7518d95b65131
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/exoneme.yaml
    --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:18:49Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/exoneme.yaml\
    \ --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/exoneme-strict.tsv"
  snapshot_sha256: 2cbf3a3a24301389a187c4ff9dae2a4a83b054a88cbabd779a40a9a2efa86afd
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/exoneme.yaml
  locator: Complete native focused output
  accessed_at: '2026-10-22T01:24:08.211801Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/exoneme.yaml
  locator: Complete native focused output
  accessed_at: '2026-10-22T01:24:08.790390Z'
  support: supports
  summary: "data/structures/membrane_organelle/exoneme.yaml  (GO:0044311)\n  pmx_sub1_exoneme_egress\t\
    plasmepsin_x_exoneme_protease\tCOVERED\t->plasmepsin_x_exoneme_protease (UniProtKB:Q8IAS0)\n\
    \  pmx_sub1_exoneme_egress\tpfsub1_exoneme_protease\tCOVERED\t->pfsub1_exoneme_protease\
    \ (UniProtKB:O61142)\n  pmx_sub1_exoneme_egress\tsera_msp_substrates\tUNANCHORED_WITH_UNIPROT\t\
    SERA and MSP substrates (UniProtKB:Q9TY95, UniProtKB:Q8I0U8)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     1  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ PARTIAL_EXAMPLES          component_ref target holds protein_examples but has\
    \ unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target\
    \ declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: 511b80633418ceaf902b70422e104017ea024ac612753acc164a8ceed3612398
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/exoneme.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 14 collected target identifiers returned OK. PMID:9722575: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9722575, DOI10.1074/jbc.273.36.23398 and A subtilisin-like protein
    in secretory organelles of Plasmodium falciparum merozoites. Bibliographic identity
    is resolved; scientific scope remains restricted to the separately documented
    abstract/body inspections. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: Exoneme organelle and apical-complex relation
  outcome: supported
  target_ids:
  - GO:0044311
  summary: The native class/parent/parthood match. The maintained functions correctly
    describe discharge of soluble protease cargo into PV rather than assuming an entire
    stable organelle is released intact; full-record interpretation preserves this
    distinction.
  evidence_ids:
  - record
  - exoneme-agent-go
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-blackman2008-jats
  - exoneme-agent-nasamu2017-jats
- assessment_id: scope
  area: scope
  topic: P. falciparum blood-stage evidence
  outcome: supported
  target_ids:
  - GO:0044311
  summary: The directly evidenced species, schizont/merozoite stages and canonical
    discharge/egress example match the primary abstract and later primary main text.
    COMMON is qualitative occurrence, not a counted frequency or all-apicomplexan
    claim. The record explicitly narrowed broader historical taxonomy.
  evidence_ids:
  - record
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-nasamu2017-jats
  - exoneme-agent-tax5833
  - exoneme-agent-tax36329
- assessment_id: membership
  area: grounding
  topic: SUB1 and PMX components versus representative identity metadata
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Primary literature supports PfSUB1 exoneme cargo and PMX localization/dependence.
    Native examples and graph xrefs identify the exact species/isolate proteins and
    SERA5/MSP1 exemplars; xrefs do not equate the entire substrate cohort with just
    those two proteins. Native by-similarity annotations and historical dense-granule
    descriptions are not counted as independent direct exoneme experiments.
  evidence_ids:
  - record
  - policy
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-blackman1998-meta
  - exoneme-agent-blackman2008-jats
  - exoneme-agent-nasamu2017-jats
  - exoneme-agent-O61142
  - exoneme-agent-Q8IAS0
  - exoneme-agent-Q9TY95
  - exoneme-agent-Q8I0U8
  - exoneme-agent-sub1-query
  - exoneme-agent-pmx-query
- assessment_id: family
  area: grounding
  topic: Resolvable SUB1 family and unresolved exact PMX family
  outcome: concern
  target_ids:
  - GO:0044311
  summary: IPR017314 is a verified whole-SUB1 family and O61142 directly carries it.
    The component’s unresolved-family rationale is stale for SUB1. IPR034204 is a
    domain and IPR001461 is broader than PMX, so neither is forced as an exact substitute
    for the remaining component.
  evidence_ids:
  - record
  - policy
  - exoneme-agent-IPR017314
  - exoneme-agent-IPR034204
  - exoneme-agent-IPR001461
  - exoneme-agent-O61142
  - exoneme-agent-Q8IAS0
- assessment_id: necessity
  area: grounding
  topic: Protease activity requirement versus organelle formation
  outcome: unknown
  target_ids:
  - GO:0044311
  summary: The studies establish important protease maturation, egress and invasion
    effects, but do not establish that loss of each cargo enzyme prevents formation
    of the exoneme compartment. Both UNKNOWN assembly-necessity entries are appropriate;
    catalytic essentiality is not silently converted to organelle-assembly necessity.
  evidence_ids:
  - record
  - policy
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-nasamu2017-jats
- assessment_id: function-graph
  area: graph
  topic: Eight qualified egress pathway edges
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Localization/storage, discharge into PV, PMX-supported SUB1 processing,
    downstream SERA/MSP processing and contributions to egress/invasion are supported
    at the stated evidence tiers. Nasamu directly supports the dependence, while its
    in-vivo direct-cleavage uncertainty is preserved by “supports maturation.” Withers
    provides reviewed background for discharge and substrate processing inside a primary
    structural paper, not an independent new discharge experiment. This graph represents
    a causal proteolytic sequence and its MECHANISTIC classification is justified
    within those limits.
  evidence_ids:
  - record
  - exoneme-agent-yeoh2007-meta
  - exoneme-agent-blackman2008-jats
  - exoneme-agent-withers2014-jats
  - exoneme-agent-nasamu2017-jats
  - exoneme-agent-Q9TY95
  - exoneme-agent-Q8I0U8
- assessment_id: coverage
  area: completeness
  topic: Full maintained record and bounded scientific coverage
  outcome: supported
  target_ids:
  - GO:0044311
  summary: Every maintained claim, graph edge and discussion was inspected. No quantitative
    physical-property field, maintained image/licence asset or verbatim evidence snippet
    is present. Existing PROPOSED status and history remain unchanged. No finding
    is invented from optional unresolved molecular inventory or unavailable full-text
    routes alone.
  evidence_ids:
  - record
  - policy
findings:
- finding_id: F1
  issue_key: exoneme-sub1-family-grounding-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the verified SUB1 family instead of retaining an unresolved-family
    rationale
  description: The PfSUB1 component and shared TODO say no exact source-neutral family
    was resolved. Native IPR017314 is a Plasmodium SUB1 protein family and is directly
    linked by the exact O61142 example, so SUB1 can now be grounded without inferring
    localization from the family. Domain-only IPR034204 and broad PMX-family candidates
    do not resolve the other component.
  target_ids:
  - GO:0044311
  field_paths:
  - components#pfsub1_exoneme_protease.grounding_status
  - components#pfsub1_exoneme_protease.grounding_notes
  - discussions#ground_exoneme_proteases
  evidence_ids:
  - record
  - policy
  - exoneme-agent-IPR017314
  - exoneme-agent-IPR034204
  - exoneme-agent-O61142
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence and minor
    weak-wording/provenance rubric
  native_severity: minor
  normalization_reason: 'Minor grounding/provenance gap: the protein identity, membership
    and mechanism remain correct; a now-resolved family has been left label-only.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0044311
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/exoneme.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, ground SUB1 to the verified
    IPR017314 family and narrow the TODO to unresolved PMX or other genuinely open
    identity questions; retain primary membership evidence and UNKNOWN assembly necessity.
  acceptance_checks:
  - Verify the exact family ID/label pair against current native InterPro and run
    product/schema/strict checks.
  - Keep the existing accession/taxon pairing and primary membership evidence; a family
    mapping alone does not prove exoneme localization.
  - Do not replace PMX with a broad A1 family or use a catalytic domain as whole-protein
    identity.
limitations:
- Yeoh2007 and Blackman1998 are inspected as complete native primary abstracts, not
  full bodies; actual publisher403 and Citeseer404 responses are retained. Other full
  primary/review sources provide independently read support for the maintained claims.
- Blackman2008 is review-tier evidence. Withers2014 was read for all introductory
  paragraphs and complete Discussion, not every experimental section. Nasamu2017 complete
  scientific main text and captions were read, but figure pixels, raw data and separate
  supplementary Methods were not independently inspected.
- The primary PMX experiments include NF54, while Q8IAS0 is a3D7 representative and
  native secretory localization uses by-similarity evidence. Exact accession/taxon
  identity is verified; this review does not relabel NF54 experiments as direct3D7
  instance measurements.
- The SERA/MSP node links representative proteins, not an exhaustive substrate inventory.
  Direct in-vivo PMX cleavage mechanism and individual exoneme-formation requirements
  remain unresolved.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requires a validated review for every uncovered target, including
  an honest clean review; no issue is invented to satisfy the local issue-only rule.
- All remote snapshots retain actual original URL, UTC access timestamp and raw SHA256.
  No maintained record or publication was modified.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
