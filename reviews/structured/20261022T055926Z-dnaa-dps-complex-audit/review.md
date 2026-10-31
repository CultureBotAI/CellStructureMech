# Dnaa dps complex scientific review

- Review: 20261022T055926Z-dnaa-dps-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:46Z
- Finished UTC: 2026-10-22T05:59:26Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DnaA-Dps identity, correct K12 examples and qualified negative-initiation graph are supported. One grouped minor supplies the exact available DnaA and Dps families.

## Scope And Provenance

Exactly one complete maintained record, native frozen guidance and actual source passages identified per evidence locator; no other maintained scientific record used as evidence.

Selection: Target 10 of batch51, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990084 | data/structures/other/dnaa_dps_complex.yaml | maintained | DnaA-Dps complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990084 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990084 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990084 | Native focused check passed; scientific support separately assessed. |
| Native verify | passed | True | GO:1990084 | Native focused check passed; scientific support separately assessed. |
| Expression-module applicability | not_applicable | False | GO:1990084 | No expression-module claim requires this resource. |
| Claim-level scientific review | passed | True | GO:1990084 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990084 | 10 of 14 collected target identifiers returned OK. PMID:18284581: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:9478970: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990084 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990084 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990084 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990084 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990084 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### DnaA-Dps protein complex and RIDA boundary

identity: supported. Targets: GO:1990084.

Native identity/parent and direct two-protein association support the MULTIPROTEIN scope. DNA can contribute to the inhibition assay but is not required to define the separately demonstrated protein interaction. Hda/beta-clamp RIDA complexes remain distinct, as the target states.

### Correct examples and exact families

grounding: concern. Targets: GO:1990084.

Reviewed P03004 and P0ABT2 correctly identify DnaA and Dps. Exact IPR001957 and IPR002177 are available for these generic classes; the narrower Dps subgroup need not replace the full family. Current label-only deferral is therefore resolvable.

### Conditional negative initiation regulation

graph: supported. Targets: GO:1990084.

Direct binding and origin-opening inhibition support the coarse NONMECHANISTIC graph. Its scope excludes Dps oligomer transitions and adaptive-mutation consequences; the definition retains thought-to qualification for oxidative stress. Strong inhibition is assay-dependent and is not claimed under allMg concentrations or every physiological condition.

### Constitution versus experimental formation necessity

grounding: unknown. Targets: GO:1990084.

The sources demonstrate interaction and inhibition, not a universal loss-of-complex requirement for each constituent or a fixed DnaA:Dps stoichiometry. Defining membership and Dps viability phenotypes do not independently establish formation enums; UNKNOWN is retained at that scope.

### Species prevalence and experimental context

scope: supported. Targets: GO:1990084.

Species562 and reference strain83333 are correct. COMMON retains the schema meaning present in most members, losses the exception; the source-supported E.coli system provides qualitative biological context, not a measured strain-prevalence census. Specific mutant/recombinant preparations do not redefine the native taxon. Localization-paper abstracts and native annotations only verify their stated provenance; no whole-complex localization experiment is inferred.

### Full record and maintained boundaries

completeness: supported. Targets: GO:1990084.

All target fields, evidence, discussions and historical entries were read, including adjacent-complex exclusions. Historical reviewer conclusions are not biological evidence. No optional inventory or uninspected detailed mechanism is forced.

## Findings

### F1: Ground DnaA and Dps with their exact families

minor / open / confirmed; issue key: dnaa-dps-exact-families.

The existing DnaA/Dps components remain REVIEWED_LABEL_ONLY despite exact full-protein IPR001957 and IPR002177 family identities and independent reviewed-example membership.

## Recommended Actions And Acceptance Checks

### A1

Use the exact DnaA and Dps families and align current grounding notes/TODO while preserving correct examples and the qualified oxidative-stress model.

- Do not substitute broad AAAATPase/ferritin folds or force a narrower gammaproteobacterial subgroup.
- Do not infer direct DnaA binding for every Dps-family member.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnaa_dps_complex.yaml; Entire target, including all components/examples, graph, evidence, discussions and history | context_only | The full maintained record was read. Historical curation notes are not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC graph scope | context_only | Family identity is separate from a taxon-specific example. Assembly necessity differs from composition, catalytic requirement and viability. |
| curation | docs/CURATION.md; Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160 | context_only | Reviewed label-only status requires an unresolved exact mapping, rather than simply deferring a verified available family. |
| replication51-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006270,GO:0009330,GO:0009340,GO:0032297,GO:0032991,GO:1990077,GO:1990078,GO:1990083,GO:1990084,GO:1990085,GO:1990099,GO:1990100,GO:1990101,GO:1990102,GO:1990125,GO:1990157; Complete relevant definitions, synonyms, active status and typed child links within the17-term response; unrelated children are not promoted | supports | GO1990084 defines the DnaA-Dps complex and qualifies its oxidative-stress role as thought to be involved. GO1990078 lists it as an is-a child; GO1990083/1990085 are distinct Hda/RIDA complexes, and GO0032297 identifies negative initiation regulation. |
| replication51-agent-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxon response | supports | ENA taxon562 is Escherichia coli, rank species; native names and lineage distinguish species from reference strain. |
| replication51-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxon response | supports | ENA taxon83333 is Escherichia coli K-12, rank strain; native names and lineage distinguish species from reference strain. |
| replication51-agent-protein-P03004 | https://rest.uniprot.org/uniprotkb/P03004.json; Accession/status/name/genes/organism; complete relevant comments, localization evidence references and InterPro xrefs | supports | Reviewed P03004 is the declared dnaA protein in E.coli K12 taxon83333. Native identity, gene names, function/subunit/similarity annotations and family xrefs were read. DnaA localization citations are annotation provenance, not independent evidence for every complex. |
| replication51-agent-gene-dnaA-exact-organism83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identities, organism and gene aliases | supports | Exact reviewed gene dnaA in the stated K12 organism83333 returns one entry, P03004; the current single-entry note is supported where asserted. |
| replication51-agent-protein-P0ABT2 | https://rest.uniprot.org/uniprotkb/P0ABT2.json; Accession/status/name/genes/organism; complete relevant comments, localization evidence references and InterPro xrefs | supports | Reviewed P0ABT2 is the declared dps protein in E.coli K12 taxon83333. Native identity, gene names, function/subunit/similarity annotations and family xrefs were read. |
| replication51-agent-gene-dps-exact-organism83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identities, organism and gene aliases | supports | Exact reviewed gene dps in the stated K12 organism83333 returns one entry, P0ABT2; the current single-entry note is supported where asserted. |
| replication51-agent-pmid-18284581 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18284581+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED18284581: Escherichia coli Dps interacts with DnaA protein to impede initiation: a model of adaptive mutation. Authors Chodavarapu S, Gomez R, Vicente M, Kaguni JM.; DOI 10.1111/j.1365-2958.2008.06127.x. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-pmid-22574163 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED22574163: Association of the chromosome replication initiator DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding. Authors Regev T, Myers N, Zarivach R, Fishov I.; DOI 10.1371/journal.pone.0036441. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-pmid-28166228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED28166228: Rapid turnover of DnaA at replication origin regions contributes to initiation control of DNA replication. Authors Schenk K, Hervás AB, Rösch TC, Eisemann M, Schmitt BA, Dahlke S, Kleine-Borgmann L, Murray SM, Graumann PL.; DOI 10.1371/journal.pgen.1006561. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-pmid-9478970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED9478970: Membrane-mediated release of nucleotide from an initiator of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct region of the protein into the lipid bilayer. Authors Garner J, Durrer P, Kitchen J, Brunner J, Crooke E.; DOI 10.1074/jbc.273.9.5167. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-ipr-IPR001957 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR001957 is the full DnaA replication-initiation protein family, supported by DnaA-specific HAMAPMF00377/NCBIfamTIGR00362 and distinguished from the broader DnaA/Hda hierarchy. This source row establishes family metadata; example membership is separately evidenced by native UniProt. |
| replication51-agent-ipr-IPR002177 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002177/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR002177 is the Dps full-protein family, distinguished from the general ferritin fold. Its family description is not proof that every member directly binds DnaA. |
| replication51-agent-ipr-IPR023067 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023067/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR023067 is a narrower gammaproteobacterial Dps subgroup, unnecessary for grounding the generic Dps protein class. |
| replication51-agent-chodavarapu2008-indexed | https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x; Only the first exact-DOI publisher result: Summary; available Introduction paragraphs; Results affinity/ELISA, Mg-dependent replication/DNA-binding, oriC-unwinding, colony-size and synchronized-cell passages plus Fig2/6 captions; Discussion Mg-concentration paragraph and next subsection opening. Discontinuous indexed excerpts; later unrelated search hits excluded. No complete Methods/body/pixels claim. | supports | Indexed genuine publisher Results directly support DnaA-Dps association by affinity chromatography and ELISA, plus condition-dependent inhibition of origin opening. At10mMMg inhibition is marginal;0.1mMMg supports the origin-unwinding assay. In-vivo induction experiments intentionally avoid H2O2 pleiotropy, and the oxidative-stress checkpoint/adaptive-mutation explanation remains a model. |
| replication51-agent-chodavarapu2008-publisher | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06127.x; Retained publisher access response | context_only | Publisher fulltext request returned HTTP403; no primary body was obtained from this route. |
| schema-result | just validate data/structures/other/dnaa_dps_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnaa_dps_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnaa_dps_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnaa_dps_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/dnaa_dps_complex.yaml  (GO:1990084)<br>  dnaa_dps_inhibition	dnaa_initiator	COVERED	-&gt;dnaa_initiator (UniProtKB:P03004)<br>  dnaa_dps_inhibition	dps_protein	COVERED	-&gt;dps_protein (UniProtKB:P0ABT2)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnaa_dps_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 14 collected target identifiers returned OK. PMID:18284581: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:9478970: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignment or deposited coordinate geometry was independently reanalyzed. Actual text/caption and native-response scopes are specified per evidence row.
- Native complete primary abstract and genuine indexed publisher excerpts were read; direct publisher fulltext returned403. The actual excerpt includes gaps and unrelated later search hits, which are excluded. No full-paper or complete Methods reading is claimed.
- The oxidative-stress checkpoint and adaptive-mutation extension remain proposed interpretations. The experiment elevates Dps without directly using H2O2 in its synchronized-cell assay.
- Exact organism83333 reviewed-gene queries support the stated single-entry notes where present. Broader taxonomy83333 queries also return descendantK12 strains and cannot be interpreted as multiple entries for the identical organism.
- COMMON is a majority-occurrence assertion under the schema; no population census was measured in the inspected studies. Generic E.coli scope is retained as qualitative synthesis, not converted to mere occurrence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055926Z-dnaa-dps-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dnaa dps complex scientific review
started_at: '2026-10-22T05:37:46Z'
finished_at: '2026-10-22T05:59:26Z'
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
summary: DnaA-Dps identity, correct K12 examples and qualified negative-initiation
  graph are supported. One grouped minor supplies the exact available DnaA and Dps
  families.
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
  - path: data/structures/other/dnaa_dps_complex.yaml
    sha256: 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87
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
- target_id: GO:1990084
  path: data/structures/other/dnaa_dps_complex.yaml
  label: DnaA-Dps complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record, native frozen guidance and
    actual source passages identified per evidence locator; no other maintained scientific
    record used as evidence.
  selection: Target 10 of batch51, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990084
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate data/structures/other/dnaa_dps_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate-strict data/structures/other/dnaa_dps_complex.yaml --out
    /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific support separately assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific support separately assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990084
  summary: No expression-module claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990084
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - replication51-agent-go
  - replication51-agent-tax562
  - replication51-agent-tax83333
  - replication51-agent-protein-P03004
  - replication51-agent-gene-dnaA-exact-organism83333
  - replication51-agent-protein-P0ABT2
  - replication51-agent-gene-dps-exact-organism83333
  - replication51-agent-pmid-18284581
  - replication51-agent-pmid-22574163
  - replication51-agent-pmid-28166228
  - replication51-agent-pmid-9478970
  - replication51-agent-ipr-IPR001957
  - replication51-agent-ipr-IPR002177
  - replication51-agent-ipr-IPR023067
  - replication51-agent-chodavarapu2008-indexed
  - replication51-agent-chodavarapu2008-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990084
  summary: '10 of 14 collected target identifiers returned OK. PMID:18284581: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC
    MED identifier, title and DOI independently inspected after the bulk eutils414
    transport failure. Identifier resolution does not certify all biological claims;
    declared primary-body and abstract reading limits remain in force.; PMID:9478970:
    UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently
    inspected after the bulk eutils414 transport failure. Identifier resolution does
    not certify all biological claims; declared primary-body and abstract reading
    limits remain in force. Native source checks are separately scoped; skipped or
    unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - replication51-agent-pmid-18284581
  - replication51-agent-pmid-22574163
  - replication51-agent-pmid-28166228
  - replication51-agent-pmid-9478970
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990084
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
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dnaa_dps_complex.yaml
  locator: Entire target, including all components/examples, graph, evidence, discussions
    and history
  accessed_at: '2026-10-22T05:49:58Z'
  support: context_only
  summary: The full maintained record was read. Historical curation notes are not
    independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T05:49:58Z'
  support: context_only
  summary: Family identity is separate from a taxon-specific example. Assembly necessity
    differs from composition, catalytic requirement and viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160
  accessed_at: '2026-10-22T05:49:58Z'
  support: context_only
  summary: Reviewed label-only status requires an unresolved exact mapping, rather
    than simply deferring a verified available family.
- evidence_id: replication51-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006270,GO:0009330,GO:0009340,GO:0032297,GO:0032991,GO:1990077,GO:1990078,GO:1990083,GO:1990084,GO:1990085,GO:1990099,GO:1990100,GO:1990101,GO:1990102,GO:1990125,GO:1990157
  locator: Complete relevant definitions, synonyms, active status and typed child
    links within the17-term response; unrelated children are not promoted
  accessed_at: '2026-10-22T05:42:45.973692Z'
  support: supports
  summary: GO1990084 defines the DnaA-Dps complex and qualifies its oxidative-stress
    role as thought to be involved. GO1990078 lists it as an is-a child; GO1990083/1990085
    are distinct Hda/RIDA complexes, and GO0032297 identifies negative initiation
    regulation.
  snapshot_sha256: 20acc6fb4f33b15254c0883eb10baca7a549febfef3948d31b5eafda0771038b
- evidence_id: replication51-agent-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:42:45.974189Z'
  support: supports
  summary: ENA taxon562 is Escherichia coli, rank species; native names and lineage
    distinguish species from reference strain.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: replication51-agent-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:42:45.974327Z'
  support: supports
  summary: ENA taxon83333 is Escherichia coli K-12, rank strain; native names and
    lineage distinguish species from reference strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: replication51-agent-protein-P03004
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P03004.json
  locator: Accession/status/name/genes/organism; complete relevant comments, localization
    evidence references and InterPro xrefs
  accessed_at: '2026-10-22T05:42:45.974560Z'
  support: supports
  summary: Reviewed P03004 is the declared dnaA protein in E.coli K12 taxon83333.
    Native identity, gene names, function/subunit/similarity annotations and family
    xrefs were read. DnaA localization citations are annotation provenance, not independent
    evidence for every complex.
  snapshot_sha256: 20b9ed0385942a0aebc3645f0f499a77e9aab0741218e2327ee80b6ae7590dca
- evidence_id: replication51-agent-gene-dnaA-exact-organism83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identities, organism and gene aliases
  accessed_at: '2026-10-22T05:43:54.622927Z'
  support: supports
  summary: Exact reviewed gene dnaA in the stated K12 organism83333 returns one entry,
    P03004; the current single-entry note is supported where asserted.
  snapshot_sha256: 3db63cf0e2bda46f5e0d2292b32f98621aa2da23fba568a428d8ad2f1fb148a0
  search_scope: UniProt gene_exact:dnaA, reviewed:true, organism_id:83333; size500;
    complete returned identities read. Descendant-strain search results are not used
    to falsify an exact-organism claim.
- evidence_id: replication51-agent-protein-P0ABT2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABT2.json
  locator: Accession/status/name/genes/organism; complete relevant comments, localization
    evidence references and InterPro xrefs
  accessed_at: '2026-10-22T05:42:45.974730Z'
  support: supports
  summary: Reviewed P0ABT2 is the declared dps protein in E.coli K12 taxon83333. Native
    identity, gene names, function/subunit/similarity annotations and family xrefs
    were read.
  snapshot_sha256: 5bc26c2d3491d422d27034cfa9f4afb128bbe8403d8b097b9e36bf810df038dc
- evidence_id: replication51-agent-gene-dps-exact-organism83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identities, organism and gene aliases
  accessed_at: '2026-10-22T05:43:54.081597Z'
  support: supports
  summary: Exact reviewed gene dps in the stated K12 organism83333 returns one entry,
    P0ABT2; the current single-entry note is supported where asserted.
  snapshot_sha256: 55916ff15491526e1713c2c33dd025ca4d012ffc4a8ed2f8a596f6dcad3c0619
  search_scope: UniProt gene_exact:dps, reviewed:true, organism_id:83333; size500;
    complete returned identities read. Descendant-strain search results are not used
    to falsify an exact-organism claim.
- evidence_id: replication51-agent-pmid-18284581
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18284581+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:48.712884Z'
  support: supports
  summary: 'Native MED18284581: Escherichia coli Dps interacts with DnaA protein to
    impede initiation: a model of adaptive mutation. Authors Chodavarapu S, Gomez
    R, Vicente M, Kaguni JM.; DOI 10.1111/j.1365-2958.2008.06127.x. Complete abstract
    read at primary-study abstract tier; metadata is not a claim of full-body access.'
  snapshot_sha256: 713570c7841039811bfffefc5ddd5fd2cb7335185d618418fc971135be321ffc
- evidence_id: replication51-agent-pmid-22574163
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:48.808029Z'
  support: supports
  summary: 'Native MED22574163: Association of the chromosome replication initiator
    DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding.
    Authors Regev T, Myers N, Zarivach R, Fishov I.; DOI 10.1371/journal.pone.0036441.
    Complete abstract read at primary-study abstract tier; metadata is not a claim
    of full-body access.'
  snapshot_sha256: 606182e9806d23b9bf7730d38e83960a8b1336283390495aabe7d55367902d79
- evidence_id: replication51-agent-pmid-28166228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:49.183588Z'
  support: supports
  summary: 'Native MED28166228: Rapid turnover of DnaA at replication origin regions
    contributes to initiation control of DNA replication. Authors Schenk K, Hervás
    AB, Rösch TC, Eisemann M, Schmitt BA, Dahlke S, Kleine-Borgmann L, Murray SM,
    Graumann PL.; DOI 10.1371/journal.pgen.1006561. Complete abstract read at primary-study
    abstract tier; metadata is not a claim of full-body access.'
  snapshot_sha256: 62b379003572dabe10f78cc8b7642794dc900df5ca5799cd0f29217cbf4c1bc3
- evidence_id: replication51-agent-pmid-9478970
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:49.417893Z'
  support: supports
  summary: 'Native MED9478970: Membrane-mediated release of nucleotide from an initiator
    of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a
    distinct region of the protein into the lipid bilayer. Authors Garner J, Durrer
    P, Kitchen J, Brunner J, Crooke E.; DOI 10.1074/jbc.273.9.5167. Complete abstract
    read at primary-study abstract tier; metadata is not a claim of full-body access.'
  snapshot_sha256: 46d168668e549dce45c86e1638c9d1bed0b4ae65a45b00090e1150e5de2a19bf
- evidence_id: replication51-agent-ipr-IPR001957
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:42:51.162827Z'
  support: supports
  summary: IPR001957 is the full DnaA replication-initiation protein family, supported
    by DnaA-specific HAMAPMF00377/NCBIfamTIGR00362 and distinguished from the broader
    DnaA/Hda hierarchy. This source row establishes family metadata; example membership
    is separately evidenced by native UniProt.
  snapshot_sha256: 364ea5ab4304d290b099574c7f9527e5577eefec2872f8fc2adde34de7eb2fc2
- evidence_id: replication51-agent-ipr-IPR002177
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002177/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:43:53.004044Z'
  support: supports
  summary: IPR002177 is the Dps full-protein family, distinguished from the general
    ferritin fold. Its family description is not proof that every member directly
    binds DnaA.
  snapshot_sha256: 6b6fa5016c1c5e5c3eff6fadd9b113bf86cd6b1de554c8e2d485546ef95617a7
- evidence_id: replication51-agent-ipr-IPR023067
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023067/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:43:53.003638Z'
  support: supports
  summary: IPR023067 is a narrower gammaproteobacterial Dps subgroup, unnecessary
    for grounding the generic Dps protein class.
  snapshot_sha256: 8848f2f85ac40734a20161f6f98d0234b381b9e3e4c8d7d4411dc588ca3b7ca5
- evidence_id: replication51-agent-chodavarapu2008-indexed
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x
  locator: 'Only the first exact-DOI publisher result: Summary; available Introduction
    paragraphs; Results affinity/ELISA, Mg-dependent replication/DNA-binding, oriC-unwinding,
    colony-size and synchronized-cell passages plus Fig2/6 captions; Discussion Mg-concentration
    paragraph and next subsection opening. Discontinuous indexed excerpts; later unrelated
    search hits excluded. No complete Methods/body/pixels claim.'
  accessed_at: '2026-10-22T05:45:16Z'
  support: supports
  summary: Indexed genuine publisher Results directly support DnaA-Dps association
    by affinity chromatography and ELISA, plus condition-dependent inhibition of origin
    opening. At10mMMg inhibition is marginal;0.1mMMg supports the origin-unwinding
    assay. In-vivo induction experiments intentionally avoid H2O2 pleiotropy, and
    the oxidative-stress checkpoint/adaptive-mutation explanation remains a model.
  snapshot_sha256: a05ea424a1bd7b768759dc96359462be3e856f83d9e980b04074a103020bdcf2
- evidence_id: replication51-agent-chodavarapu2008-publisher
  kind: database
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06127.x
  locator: Retained publisher access response
  accessed_at: '2026-10-22T05:43:16.589100Z'
  support: context_only
  summary: Publisher fulltext request returned HTTP403; no primary body was obtained
    from this route.
  snapshot_sha256: 642d8d8f811c382ca3b937b715e0110c74ae36df8f9e4156873923a1e910e850
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnaa_dps_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnaa_dps_complex.yaml'
  snapshot_sha256: 3179fcd74b57064c176ccd2e55b7d880ef79bcf2b1379391faadd6a24cb3fd41
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnaa_dps_complex.yaml --out
    /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:51Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnaa_dps_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dnaa_dps_complex-strict.tsv"
  snapshot_sha256: f295d73f303e33e6e37d8853eefe3d6539ba071ea46d07941c2fa60b87cacca2
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:42:57.093585Z'
  support: supports
  summary: "data/structures/other/dnaa_dps_complex.yaml  (GO:1990084)\n  dnaa_dps_inhibition\t\
    dnaa_initiator\tCOVERED\t->dnaa_initiator (UniProtKB:P03004)\n  dnaa_dps_inhibition\t\
    dps_protein\tCOVERED\t->dps_protein (UniProtKB:P0ABT2)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 9c32ad64b248777c65ff4967c2fceec4a6976c91d56e141e5cc47ff0cdbbe226
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:42:58.566045Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnaa_dps_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 14 collected target identifiers returned OK. PMID:18284581: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC
    MED identifier, title and DOI independently inspected after the bulk eutils414
    transport failure. Identifier resolution does not certify all biological claims;
    declared primary-body and abstract reading limits remain in force.; PMID:9478970:
    UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently
    inspected after the bulk eutils414 transport failure. Identifier resolution does
    not certify all biological claims; declared primary-body and abstract reading
    limits remain in force. Native source checks are separately scoped; skipped or
    unreachable identifiers are not silently counted as resolved.'
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
  topic: DnaA-Dps protein complex and RIDA boundary
  outcome: supported
  target_ids:
  - GO:1990084
  summary: Native identity/parent and direct two-protein association support the MULTIPROTEIN
    scope. DNA can contribute to the inhibition assay but is not required to define
    the separately demonstrated protein interaction. Hda/beta-clamp RIDA complexes
    remain distinct, as the target states.
  evidence_ids:
  - record
  - replication51-agent-go
  - replication51-agent-chodavarapu2008-indexed
  - replication51-agent-pmid-18284581
- assessment_id: grounding
  area: grounding
  topic: Correct examples and exact families
  outcome: concern
  target_ids:
  - GO:1990084
  summary: Reviewed P03004 and P0ABT2 correctly identify DnaA and Dps. Exact IPR001957
    and IPR002177 are available for these generic classes; the narrower Dps subgroup
    need not replace the full family. Current label-only deferral is therefore resolvable.
  evidence_ids:
  - record
  - curation
  - replication51-agent-ipr-IPR001957
  - replication51-agent-ipr-IPR002177
  - replication51-agent-ipr-IPR023067
  - replication51-agent-protein-P03004
  - replication51-agent-protein-P0ABT2
  - replication51-agent-gene-dnaA-exact-organism83333
  - replication51-agent-gene-dps-exact-organism83333
- assessment_id: graph
  area: graph
  topic: Conditional negative initiation regulation
  outcome: supported
  target_ids:
  - GO:1990084
  summary: Direct binding and origin-opening inhibition support the coarse NONMECHANISTIC
    graph. Its scope excludes Dps oligomer transitions and adaptive-mutation consequences;
    the definition retains thought-to qualification for oxidative stress. Strong inhibition
    is assay-dependent and is not claimed under allMg concentrations or every physiological
    condition.
  evidence_ids:
  - record
  - schema
  - replication51-agent-go
  - replication51-agent-chodavarapu2008-indexed
  - replication51-agent-pmid-18284581
- assessment_id: formation
  area: grounding
  topic: Constitution versus experimental formation necessity
  outcome: unknown
  target_ids:
  - GO:1990084
  summary: The sources demonstrate interaction and inhibition, not a universal loss-of-complex
    requirement for each constituent or a fixed DnaA:Dps stoichiometry. Defining membership
    and Dps viability phenotypes do not independently establish formation enums; UNKNOWN
    is retained at that scope.
  evidence_ids:
  - record
  - schema
  - replication51-agent-chodavarapu2008-indexed
- assessment_id: scope
  area: scope
  topic: Species prevalence and experimental context
  outcome: supported
  target_ids:
  - GO:1990084
  summary: Species562 and reference strain83333 are correct. COMMON retains the schema
    meaning present in most members, losses the exception; the source-supported E.coli
    system provides qualitative biological context, not a measured strain-prevalence
    census. Specific mutant/recombinant preparations do not redefine the native taxon.
    Localization-paper abstracts and native annotations only verify their stated provenance;
    no whole-complex localization experiment is inferred.
  evidence_ids:
  - record
  - schema
  - replication51-agent-chodavarapu2008-indexed
  - replication51-agent-go
  - replication51-agent-tax562
  - replication51-agent-tax83333
  - replication51-agent-protein-P03004
  - replication51-agent-protein-P0ABT2
  - replication51-agent-pmid-18284581
  - replication51-agent-pmid-22574163
  - replication51-agent-pmid-28166228
  - replication51-agent-pmid-9478970
- assessment_id: coverage
  area: completeness
  topic: Full record and maintained boundaries
  outcome: supported
  target_ids:
  - GO:1990084
  summary: All target fields, evidence, discussions and historical entries were read,
    including adjacent-complex exclusions. Historical reviewer conclusions are not
    biological evidence. No optional inventory or uninspected detailed mechanism is
    forced.
  evidence_ids:
  - record
  - schema
  - curation
  - replication51-agent-go
findings:
- finding_id: F1
  issue_key: dnaa-dps-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DnaA and Dps with their exact families
  description: The existing DnaA/Dps components remain REVIEWED_LABEL_ONLY despite
    exact full-protein IPR001957 and IPR002177 family identities and independent reviewed-example
    membership.
  target_ids:
  - GO:1990084
  field_paths:
  - components#dnaa_initiator.grounding_status
  - components#dps_protein.grounding_status
  - discussions#resolve_dnaa_dps_component_groundings
  evidence_ids:
  - record
  - curation
  - replication51-agent-ipr-IPR001957
  - replication51-agent-ipr-IPR002177
  - replication51-agent-protein-P03004
  - replication51-agent-protein-P0ABT2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990084
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
  description: Use the exact DnaA and Dps families and align current grounding notes/TODO
    while preserving correct examples and the qualified oxidative-stress model.
  acceptance_checks:
  - Do not substitute broad AAAATPase/ferritin folds or force a narrower gammaproteobacterial
    subgroup.
  - Do not infer direct DnaA binding for every Dps-family member.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignment or deposited
  coordinate geometry was independently reanalyzed. Actual text/caption and native-response
  scopes are specified per evidence row.
- Native complete primary abstract and genuine indexed publisher excerpts were read;
  direct publisher fulltext returned403. The actual excerpt includes gaps and unrelated
  later search hits, which are excluded. No full-paper or complete Methods reading
  is claimed.
- The oxidative-stress checkpoint and adaptive-mutation extension remain proposed
  interpretations. The experiment elevates Dps without directly using H2O2 in its
  synchronized-cell assay.
- Exact organism83333 reviewed-gene queries support the stated single-entry notes
  where present. Broader taxonomy83333 queries also return descendantK12 strains and
  cannot be interpreted as multiple entries for the identical organism.
- COMMON is a majority-occurrence assertion under the schema; no population census
  was measured in the inspected studies. Generic E.coli scope is retained as qualitative
  synthesis, not converted to mere occurrence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
