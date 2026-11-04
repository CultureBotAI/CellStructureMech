# Source-backed review of dna replication factor c complex

- Review: 20261022T055923Z-dna-replication-factor-c-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:24Z
- Finished UTC: 2026-10-22T05:59:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor exact RFC1 family grounding gap. Five verified yeast protein examples, composition and clamp-loading function are supported; broader small-subunit families and formation necessity remain unresolved.

## Scope And Provenance

Exactly one complete maintained target and the frozen governing/schema/protein/graph guidance; no scientific conclusion depends on a neighboring maintained record. All scientific fields and source claims are assessed at the explicitly inspected tiers.

Selection: Batch51 fixed strict path order, index 5; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005663 | data/structures/other/dna_replication_factor_c_complex.yaml | maintained | DNA replication factor C complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005663 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005663 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0005663 | Focused check passed; biological scope assessed independently. |
| Focused native verify | failed | False | GO:0005663 | Executed sandbox request failed because UniProt DNS was unavailable; preserved as an optional historical attempt and superseded by the separately retained successful network retry. |
| Focused native verify network retry | passed | True | GO:0005663 | Focused check passed; biological scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0005663 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005663 | 17 of 22 collected target identifiers returned OK. PMID:14614842: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:14646196: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:16172520: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:7651383: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:8559655: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005663 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005663 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005663 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005663 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005663 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Canonical yeast RFC and broader ontology scope

identity: supported. Targets: GO:0005663.

The record distinguishes the generic RFC class from its five named budding-yeast subunits. GO identity, protein-complex hierarchy, replication-fork parthood, clamp-loading function and reference yeast example are supported. Archaeal papers appear as exact GO definition references; they are not used to assert yeast five-subunit experiments.

### Five verified protein instances and RFC1 family gap

grounding: concern. Targets: GO:0005663.

All five reviewed S288C accessions, gene/taxon pairs and current single-hit query notes agree with native entries. Native IPR012178 exactly represents RFC1; IPR050238 and IPR013748 do not justify assigning exact RFC2–5 family identities. Only RFC1 has a confirmed actionable family omission.

### Unknown formation necessity is appropriately retained

grounding: unknown. Targets: GO:0005663.

All five essentialities remain UNKNOWN. Cullmann’s viability results and Gary’s functional restoration establish important biological requirements, but Gary also recovers a four-subunit physical complex. This directly cautions against substituting clamp-loading activity or viability for formation necessity.

### Seven-edge descriptive composition/function graph

graph: supported. Targets: GO:0005663.

Five constituent-to-RFC edges plus clamp-loader and replication function edges are supported at their stated broad scope. The explicit NONMECHANISTIC graph does not overclaim a loading cycle or interfaces.

### Taxon identity, majority semantics and experimental boundaries

scope: supported. Targets: GO:0005663.

The named yeast taxon and canonical system agree with the primary studies; S288C entries are reference examples, not claims that every experiment used that strain. COMMON retains its schema meaning present in most members with exceptional losses. The sources provide qualitative conservation/system support rather than a measured prevalence census; no artificial census requirement is imposed.

### Whole-target coverage with bounded unresolved enrichment

completeness: supported. Targets: GO:0005663.

The complete maintained target, each source claim, graph edge, component state, protein example, discussion and history was assessed. Exact actionable class mappings are distinguished from unresolved broader/domain candidates and optional enrichment. Existing historical access/curation notes are not judged false merely because this review recovered additional sources.

## Findings

### F1: Resolve verified exact subunit family grounding

minor / open / confirmed; issue key: dna-replication-factor-c-complex-exact-family-grounding.

The named RFC1 large-subunit class exactly matches IPR012178, verified from native family metadata/signature and the maintained P38630 UniProt cross-reference. The current REVIEWED_LABEL_ONLY row and OPEN task leave this resolvable match unrepresented. No exact RFC2–5 mapping is established by broad IPR050238 or C-terminal IPR013748. Historical statements about what was curated in an earlier pass are preserved as history, not declared fabricated.

## Recommended Actions And Acceptance Checks

### A1

Ground the verified class RFC1 to IPR012178 with source-backed family evidence and update the corresponding open task/status. Preserve unresolved classes and historical provenance; keep organism accessions as examples.

- Each added family denotes the existing whole-protein class rather than a domain, broader homolog group or species accession.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_replication_factor_c_complex.yaml; Entire maintained target, all component/protein evidence, graph nodes/edges, discussion and history | context_only | All current claims were read in full; no neighboring record judgment is imported. |
| curation | docs/CURATION.md; Components: class grounding, REVIEWED_LABEL_ONLY and formation necessity | context_only | An exact family grounds a protein class, whereas a species accession is an example. REVIEWED_LABEL_ONLY means no exact term exists after review. Essentiality concerns formation of the structure, not viability or catalytic function. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | COMMON means present in most taxon members with exceptional losses; it is not merely an occurrence label. UNKNOWN preserves unestablished formation necessity. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Topology versus mechanism and edge-level evidence | context_only | Membership, compartment placement and generic process membership do not themselves encode an experimentally supported assembly mechanism. |
| micro51-go-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0032991,GO:0032993,GO:0005654,GO:0005657,GO:0003689,GO:0003697,GO:0006260,GO:0042555,GO:0000811; Thirteen-term response: exact target definition/xrefs/status/synonyms, relevant parent/compartment typed children and declared function/component terms. Unrelated child inventory is not treated as biological evidence. | supports | Active GO0005663 defines the PCNA clamp loader and eukaryotic five-polypeptide form. GO0032991 parent and GO0005657 part_of context are corroborated by relevant typed child links. GO0003689/0006260 identify clamp-loader activity and DNA replication. Definition xrefs14614842/14646196/16172520 are bibliographically verified separately. |
| micro51-GO0005663-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/ancestors?relations=is_a; Exact target query with relations=is_a; complete ancestor IDs inspected. No part_of relation is inferred from this ancestry list. | supports | The is_a-only native ancestor response confirms the target’s protein-containing-complex hierarchy. |
| micro51-GO0005663-constraints-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/constraints; Exact taxonConstraints array only; inherited annotation blacklist is not used for occurrence or composition. | supports | The exact constraints exclude Bacteria2 and allow cellular organisms131567; archaeal RFC is therefore not treated as a yeast identity error. Taxon restrictions do not establish a prevalence census. |
| micro51-tax4932-network | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId4932 is Saccharomyces cerevisiae, rank species. |
| micro51-tax559292-network | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId559292 is S. cerevisiae S288C, rank strain; reference protein identity is distinct from the strains used in the cited experiments. |
| micro51-pmid-7651383-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7651383%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Cullmann et al.1995, Characterization of the five replication factor C genes of Saccharomyces cerevisiae, DOI10.1128/MCB.15.9.4661. Exact title/PMID/DOI and complete abstract agree with the maintained bibliography. |
| micro51-pmid-8559655-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8559655%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Gary and Burgers1995, Identification of the fifth subunit of Saccharomyces cerevisiae replication factor C, DOI10.1093/nar/23.24.4986. Complete abstract describes four-subunit inactive complex versus RFC5-dependent activity. The metadata author initials do not override the original page title; the maintained surname attribution is correct. |
| micro51-pmid-14614842-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Kim and MacNeill2003, Genome stability: a new member of the RFC family, DOI10.1016/j.cub.2003.10.048. Complete review abstract concerns conserved RFC and specialized variants; no full main body was inspected. |
| micro51-pmid-14646196-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14646196%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Kitabayashi et al.2003, Analysis of the function of the replication factor C protein from the hyperthermophilic archaeon Pyrococcus kodakaraensis KOD1 in vitro, DOI10.1271/bbb.67.2373. Complete abstract concerns the archaeal large/small-subunit RFC, recombinant expression and PCNA-dependent elongation; it is not a five-yeast-subunit experiment. |
| micro51-pmid-16172520-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16172520%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Nishida et al.2005, Identification of the critical region in replication factor C from Pyrococcus furiosus for the stable complex formation with proliferating cell nuclear antigen and DNA, DOI10.1266/ggs.80.83. Complete abstract distinguishes the stable ternary-complex assay from loading activity. |
| micro51-ipr-IPR012178 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012178/; Complete native metadata name/type/accession/descriptions and member_databases. Background prose is not promoted to new mechanistic evidence. | supports | Native IPR012178 identifies the whole-protein RFC1 large subunit class. Family with PIRSF036578 signature; this is more specific than broad clamp-loader or C-terminal-domain entries. This entry supplies family identity/type/signature evidence; individual protein membership is verified in separate UniProt responses. |
| micro51-protein-P38630-network | https://rest.uniprot.org/uniprotkb/P38630.json; Complete identity/status/gene/taxon/name fields, all InterPro xrefs and full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp retained for reused B48 responses. | supports | Native reviewed P38630 is RFC1 in S. cerevisiae S288C559292. Identity, gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical RFC membership is explicit; IPR012178 independently corroborates the RFC1 whole-protein family. |
| micro51-gene-RFC1-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and query URL; this is bounded reviewed exact-gene uniqueness, not absence of unreviewed homologs. | supports | The exact reviewed gene/taxon559292 query returns one entry, P38630, supporting the maintained current uniqueness note for RFC1. |
| micro51-protein-P40348 | https://rest.uniprot.org/uniprotkb/P40348.json; Complete identity/status/gene/taxon/name fields, all InterPro xrefs and full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp retained for reused B48 responses. | supports | Native reviewed P40348 is RFC2 in S. cerevisiae S288C559292. Identity, gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed for this conclusion. |
| micro51-gene-RFC2-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and query URL; this is bounded reviewed exact-gene uniqueness, not absence of unreviewed homologs. | supports | The exact reviewed gene/taxon559292 query returns one entry, P40348, supporting the maintained current uniqueness note for RFC2. |
| micro51-protein-P38629 | https://rest.uniprot.org/uniprotkb/P38629.json; Complete identity/status/gene/taxon/name fields, all InterPro xrefs and full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp retained for reused B48 responses. | supports | Native reviewed P38629 is RFC3 in S. cerevisiae S288C559292. Identity, gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed for this conclusion. |
| micro51-gene-RFC3-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and query URL; this is bounded reviewed exact-gene uniqueness, not absence of unreviewed homologs. | supports | The exact reviewed gene/taxon559292 query returns one entry, P38629, supporting the maintained current uniqueness note for RFC3. |
| micro51-protein-P40339 | https://rest.uniprot.org/uniprotkb/P40339.json; Complete identity/status/gene/taxon/name fields, all InterPro xrefs and full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp retained for reused B48 responses. | supports | Native reviewed P40339 is RFC4 in S. cerevisiae S288C559292. Identity, gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed for this conclusion. |
| micro51-gene-RFC4-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and query URL; this is bounded reviewed exact-gene uniqueness, not absence of unreviewed homologs. | supports | The exact reviewed gene/taxon559292 query returns one entry, P40339, supporting the maintained current uniqueness note for RFC4. |
| micro51-protein-P38251 | https://rest.uniprot.org/uniprotkb/P38251.json; Complete identity/status/gene/taxon/name fields, all InterPro xrefs and full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp retained for reused B48 responses. | supports | Native reviewed P38251 is RFC5 in S. cerevisiae S288C559292. Identity, gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed for this conclusion. |
| micro51-gene-RFC5-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and query URL; this is bounded reviewed exact-gene uniqueness, not absence of unreviewed homologs. | supports | The exact reviewed gene/taxon559292 query returns one entry, P38251, supporting the maintained current uniqueness note for RFC5. |
| micro51-ipr-IPR050238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Complete metadata name/type/signatures and generated-prose flags; no exact small-subunit mapping inferred. | supports | IPR050238 is a broader clamp-loader-complex family and does not distinguish RFC2/3/4/5. Its generated unchecked description is not an independent primary mechanism source. |
| micro51-ipr-IPR013748 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013748/; Complete native accession/name/type/description and PF08542 signature. | supports | IPR013748 is a C-terminal domain, not an exact whole RFC subunit class. |
| micro51-cullmann1995-cshl-pdf | https://repository.cshl.edu/id/eprint/24950/1/Characterization%20of%20the%20five%20replication%20factor%20C.pdf; Original PDF title/abstract/Introductionp4661; complete Methodsp4662; Results cloning/mappingp4663; p4665 Table1 and viability paragraph; Discussionp4668–4669/Fig8 caption. Sequence-alignment pages not independently read. | supports | The primary paper identifies five RFC genes, with peptide sequences for Rfc1/2/4/5 and Rfc3 supported by homology/prior immunoblot work. RFC2–5 disruption demonstrates viability requirements, not loss of physical complex assembly. Conserved sequence relationships and PCNA interactions are discussed with direct-versus-indirect alternatives retained. |
| micro51-gary1995-page4986 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/c082d190d843/nar00024-0060.png; Original journal page4986 scan: actual pixels and all scientific text/caption content inspected; no quantitative image reanalysis. | supports | Title/abstract, Introduction and beginning Methods establish the five-subunit question, biological context and strain/plasmid setup. |
| micro51-gary1995-page4987 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/a20ddcdc4617/nar00024-0061.png; Original journal page4987 scan: actual pixels and all scientific text/caption content inspected; no quantitative image reanalysis. | supports | Methods and opening Results describe RFC purification, recombinant work and RFC5 cloning; assay conditions and construct distinctions were inspected. |
| micro51-gary1995-page4988 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/2a28a2436cf0/nar00024-0062.png; Original journal page4988 scan: actual pixels and all scientific text/caption content inspected; no quantitative image reanalysis. | supports | Results/Fig1–2 describe Rfc5 sequence and recombinant protein identification; similar gel mobility alone does not identify the subunit unambiguously. |
| micro51-gary1995-page4989 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/893d6e21a8be/nar00024-0063.png; Original journal page4989 scan: actual pixels and all scientific text/caption content inspected; no quantitative image reanalysis. | supports | Results/Fig3 show the four-subunit complex can co-purify and has ATPase activity yet lacks RFC activity; this is not a failure of physical formation. |
| micro51-gary1995-page4990 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/87a02523b583/nar00024-0064.png; Original journal page4990 scan: actual pixels and all scientific text/caption content inspected; no quantitative image reanalysis. | supports | Results/Discussion/Fig4 show RFC5 co-overexpression restores functional RFC activity and discuss fifth-subunit identification. Viability and clamp-loader activity remain distinct from physical assembly. |
| micro51-nishida2005-pdf | https://www.jstage.jst.go.jp/article/ggs/80/2/80_2_83/_pdf/-char/en; PDF title/complete abstract and Introductionpp83–84; beginning Methodsp84 Materials and mutagenesis setup only. Later Results/Discussion not independently read. | supports | The primary abstract and Introduction distinguish archaeal one-large/four-small RFC from eukaryotic five different subunits and describe the stable PCNA–RFC–DNA complex question. Recombinant E. coli expression does not make the archaeal complex bacterial. |
| micro51-kim2003-publisher | https://doi.org/10.1016/j.cub.2003.10.048; Actual native status and inspected response text; no scientific body inferred from successful HTTP status. | context_only | HTTP200 contains a LinkingHub Redirecting locator page, not the article body. |
| micro51-kitabayashi2003-publisher | https://doi.org/10.1271/bbb.67.2373; Actual native status and inspected response text; no scientific body inferred from successful HTTP status. | context_only | HTTP403 challenge response does not supply the article main body. |
| micro51-cullmann1995-pdf | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC230709/pdf/154661.pdf; Actual native status and inspected response text; no scientific body inferred from successful HTTP status. | context_only | HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages; the separately captured CSHL PDF is the genuine body. |
| micro51-gary1995-pdf | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307503/pdf/nar00024-0060.pdf; Actual native status and inspected response text; no scientific body inferred from successful HTTP status. | context_only | HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages; original page scans provide the actually inspected body. |
| schema-result | just validate data/structures/other/dna_replication_factor_c_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_replication_factor_c_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_replication_factor_c_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_replication_factor_c_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml --causal-graphs; Complete focused read-only native causal-graphs report | supports | data/structures/other/dna_replication_factor_c_complex.yaml  (GO:0005663)<br>  rfc_pcna_loading	rfc1_large_subunit	COVERED	-&gt;rfc1_large_subunit (UniProtKB:P38630)<br>  rfc_pcna_loading	rfc2_subunit	COVERED	-&gt;rfc2_subunit (UniProtKB:P40348)<br>  rfc_pcna_loading	rfc3_subunit	COVERED	-&gt;rfc3_subunit (UniProtKB:P38629)<br>  rfc_pcna_loading	rfc4_subunit	COVERED	-&gt;rfc4_subunit (UniProtKB:P40339)<br>  rfc_pcna_loading	rfc5_subunit	COVERED	-&gt;rfc5_subunit (UniProtKB:P38251)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     5  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml --verify; Complete focused read-only native verify report | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| native-verify-network | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml --verify; Complete focused read-only native verify report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dna_replication_factor_c_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 17 of 22 collected target identifiers returned OK. PMID:14614842: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:14646196: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:16172520: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:7651383: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:8559655: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Cullmann1995 was independently read at the selected pages/sections listed, not every sequence alignment. Gary1995 original scans4986–4990 were visually inspected; retained page4991 references were not used. No quantitative figure reanalysis or supplement was performed.
- Kim/MacNeill2003 and Kitabayashi2003 remain complete-abstract-only sources: the former publisher200 is a redirect locator and the latter403. Nishida2005 body inspection is restricted to title/abstract/Introduction and beginning Methods, not later Results.
- The exact RFC1 family is established; bounded family metadata/search inspection did not establish exact RFC2–5 families. This is not an exhaustive absence claim. S288C reference accessions are distinct from the paper’s experimental yeast strains.
- Native initial DNS failures and successful network retries are retained separately. An HTTP200 redirect, download challenge or abstract landing page is never treated as full scientific text.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests one review for every unreviewed record, including qualified clean records.
- Native UniProt/ontology/family adapters directly address these eukaryotic complex claims. No matched iModulonDB organism/dataset is established or used; expression-module evidence would not prove physical assembly.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055923Z-dna-replication-factor-c-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dna replication factor c complex
started_at: '2026-10-22T05:37:24Z'
finished_at: '2026-10-22T05:59:23Z'
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
summary: One minor exact RFC1 family grounding gap. Five verified yeast protein examples,
  composition and clamp-loading function are supported; broader small-subunit families
  and formation necessity remain unresolved.
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
  - path: data/structures/other/dna_replication_factor_c_complex.yaml
    sha256: 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f
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
- target_id: GO:0005663
  path: data/structures/other/dna_replication_factor_c_complex.yaml
  label: DNA replication factor C complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target and the frozen governing/schema/protein/graph
    guidance; no scientific conclusion depends on a neighboring maintained record.
    All scientific fields and source claims are assessed at the explicitly inspected
    tiers.
  selection: Batch51 fixed strict path order, index 5; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005663
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: just validate data/structures/other/dna_replication_factor_c_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: just validate-strict data/structures/other/dna_replication_factor_c_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; biological scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: failed
  required: false
  target_ids:
  - GO:0005663
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --verify
  exit_code: 1
  summary: Executed sandbox request failed because UniProt DNS was unavailable; preserved
    as an optional historical attempt and superseded by the separately retained successful
    network retry.
  evidence_ids:
  - native-verify
- check_id: native-verify-network
  name: Focused native verify network retry
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; biological scope assessed independently.
  evidence_ids:
  - native-verify-network
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005663
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-pmid-7651383-network
  - micro51-pmid-8559655-network
  - micro51-pmid-14614842-network
  - micro51-pmid-14646196-network
  - micro51-pmid-16172520-network
  - micro51-ipr-IPR012178
  - micro51-protein-P38630-network
  - micro51-gene-RFC1-network
  - micro51-protein-P40348
  - micro51-gene-RFC2-network
  - micro51-protein-P38629
  - micro51-gene-RFC3-network
  - micro51-protein-P40339
  - micro51-gene-RFC4-network
  - micro51-protein-P38251
  - micro51-gene-RFC5-network
  - micro51-ipr-IPR050238
  - micro51-ipr-IPR013748
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
  - micro51-kim2003-publisher
  - micro51-kitabayashi2003-publisher
  - micro51-cullmann1995-pdf
  - micro51-gary1995-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005663
  summary: '17 of 22 collected target identifiers returned OK. PMID:14614842: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:14646196: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force.; PMID:16172520: UNREACHABLE; Exact native EuropePMC
    MED identifier, title and DOI independently inspected after the bulk eutils414
    transport failure. Identifier resolution does not certify all biological claims;
    declared primary-body and abstract reading limits remain in force.; PMID:7651383:
    UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently
    inspected after the bulk eutils414 transport failure. Identifier resolution does
    not certify all biological claims; declared primary-body and abstract reading
    limits remain in force.; PMID:8559655: UNREACHABLE; Exact native EuropePMC MED
    identifier, title and DOI independently inspected after the bulk eutils414 transport
    failure. Identifier resolution does not certify all biological claims; declared
    primary-body and abstract reading limits remain in force. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro51-pmid-14614842-network
  - micro51-pmid-14646196-network
  - micro51-pmid-16172520-network
  - micro51-pmid-7651383-network
  - micro51-pmid-8559655-network
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005663
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
  - GO:0005663
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
  - GO:0005663
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
  - GO:0005663
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
  - GO:0005663
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
  reference: data/structures/other/dna_replication_factor_c_complex.yaml
  locator: Entire maintained target, all component/protein evidence, graph nodes/edges,
    discussion and history
  accessed_at: '2026-10-22T05:51:03Z'
  support: context_only
  summary: All current claims were read in full; no neighboring record judgment is
    imported.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: class grounding, REVIEWED_LABEL_ONLY and formation necessity'
  accessed_at: '2026-10-22T05:51:03Z'
  support: context_only
  summary: An exact family grounds a protein class, whereas a species accession is
    an example. REVIEWED_LABEL_ONLY means no exact term exists after review. Essentiality
    concerns formation of the structure, not viability or catalytic function.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T05:51:03Z'
  support: context_only
  summary: COMMON means present in most taxon members with exceptional losses; it
    is not merely an occurrence label. UNKNOWN preserves unestablished formation necessity.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Topology versus mechanism and edge-level evidence
  accessed_at: '2026-10-22T05:51:03Z'
  support: context_only
  summary: Membership, compartment placement and generic process membership do not
    themselves encode an experimentally supported assembly mechanism.
- evidence_id: micro51-go-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0032991,GO:0032993,GO:0005654,GO:0005657,GO:0003689,GO:0003697,GO:0006260,GO:0042555,GO:0000811
  locator: 'Thirteen-term response: exact target definition/xrefs/status/synonyms,
    relevant parent/compartment typed children and declared function/component terms.
    Unrelated child inventory is not treated as biological evidence.'
  accessed_at: '2026-10-22T05:41:53.028093Z'
  support: supports
  summary: Active GO0005663 defines the PCNA clamp loader and eukaryotic five-polypeptide
    form. GO0032991 parent and GO0005657 part_of context are corroborated by relevant
    typed child links. GO0003689/0006260 identify clamp-loader activity and DNA replication.
    Definition xrefs14614842/14646196/16172520 are bibliographically verified separately.
  snapshot_sha256: aa2de8390a1ee6ed65c370de3a77e03161506b64eace1416883667eb013d002e
- evidence_id: micro51-GO0005663-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/ancestors?relations=is_a
  locator: Exact target query with relations=is_a; complete ancestor IDs inspected.
    No part_of relation is inferred from this ancestry list.
  accessed_at: '2026-10-22T05:41:50.543621Z'
  support: supports
  summary: The is_a-only native ancestor response confirms the target’s protein-containing-complex
    hierarchy.
  snapshot_sha256: fe995c767f0fda1a07833fa8f3e7e87d98f431714121494901d8b4a91d38df06
- evidence_id: micro51-GO0005663-constraints-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/constraints
  locator: Exact taxonConstraints array only; inherited annotation blacklist is not
    used for occurrence or composition.
  accessed_at: '2026-10-22T05:41:50.542924Z'
  support: supports
  summary: The exact constraints exclude Bacteria2 and allow cellular organisms131567;
    archaeal RFC is therefore not treated as a yeast identity error. Taxon restrictions
    do not establish a prevalence census.
  snapshot_sha256: df450f113911ee9f69c32deb4a0a02218b21738e4d92ccec2f7891e1efea9931
- evidence_id: micro51-tax4932-network
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:41:56.285243Z'
  support: supports
  summary: ENA taxId4932 is Saccharomyces cerevisiae, rank species.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro51-tax559292-network
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:41:56.502600Z'
  support: supports
  summary: ENA taxId559292 is S. cerevisiae S288C, rank strain; reference protein
    identity is distinct from the strains used in the cited experiments.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro51-pmid-7651383-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7651383%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:54.806262Z'
  support: supports
  summary: Cullmann et al.1995, Characterization of the five replication factor C
    genes of Saccharomyces cerevisiae, DOI10.1128/MCB.15.9.4661. Exact title/PMID/DOI
    and complete abstract agree with the maintained bibliography.
  snapshot_sha256: 02ce864708914c85af569a591795003f6c4a2f4824923b6eb40455a459b561c1
- evidence_id: micro51-pmid-8559655-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8559655%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:55.115128Z'
  support: supports
  summary: Gary and Burgers1995, Identification of the fifth subunit of Saccharomyces
    cerevisiae replication factor C, DOI10.1093/nar/23.24.4986. Complete abstract
    describes four-subunit inactive complex versus RFC5-dependent activity. The metadata
    author initials do not override the original page title; the maintained surname
    attribution is correct.
  snapshot_sha256: 911121994223dd76bc748f3ed41124d155b745e3f3f07452726af351a24c7d60
- evidence_id: micro51-pmid-14614842-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:53.958490Z'
  support: supports
  summary: 'Kim and MacNeill2003, Genome stability: a new member of the RFC family,
    DOI10.1016/j.cub.2003.10.048. Complete review abstract concerns conserved RFC
    and specialized variants; no full main body was inspected.'
  snapshot_sha256: ce96104222d38cccd55e0d12af1caee12799a9263fa40a69bf95b10ac3556041
- evidence_id: micro51-pmid-14646196-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14646196%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:54.490274Z'
  support: supports
  summary: Kitabayashi et al.2003, Analysis of the function of the replication factor
    C protein from the hyperthermophilic archaeon Pyrococcus kodakaraensis KOD1 in
    vitro, DOI10.1271/bbb.67.2373. Complete abstract concerns the archaeal large/small-subunit
    RFC, recombinant expression and PCNA-dependent elongation; it is not a five-yeast-subunit
    experiment.
  snapshot_sha256: 005a39b1088271399b08978b20d2434895c5cfcc1684c354bf14b7b69dd69bbf
- evidence_id: micro51-pmid-16172520-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16172520%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:54.636011Z'
  support: supports
  summary: Nishida et al.2005, Identification of the critical region in replication
    factor C from Pyrococcus furiosus for the stable complex formation with proliferating
    cell nuclear antigen and DNA, DOI10.1266/ggs.80.83. Complete abstract distinguishes
    the stable ternary-complex assay from loading activity.
  snapshot_sha256: 78b88359f656820314700f912656435ce1c4b454383203408293857d5305d7d2
- evidence_id: micro51-ipr-IPR012178
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012178/
  locator: Complete native metadata name/type/accession/descriptions and member_databases.
    Background prose is not promoted to new mechanistic evidence.
  accessed_at: '2026-10-22T05:42:48.760116Z'
  support: supports
  summary: Native IPR012178 identifies the whole-protein RFC1 large subunit class.
    Family with PIRSF036578 signature; this is more specific than broad clamp-loader
    or C-terminal-domain entries. This entry supplies family identity/type/signature
    evidence; individual protein membership is verified in separate UniProt responses.
  snapshot_sha256: e9520dc4e483905f19cbb30aeae7961e8dd49e1c102d88869da21b19b7dcc4e5
- evidence_id: micro51-protein-P38630-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38630.json
  locator: Complete identity/status/gene/taxon/name fields, all InterPro xrefs and
    full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp
    retained for reused B48 responses.
  accessed_at: '2026-10-22T05:41:55.411754Z'
  support: supports
  summary: Native reviewed P38630 is RFC1 in S. cerevisiae S288C559292. Identity,
    gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical
    RFC membership is explicit; IPR012178 independently corroborates the RFC1 whole-protein
    family.
  snapshot_sha256: 455f56fd2d2492ed2be545915de9082d562a479ed379d6de1a161759d46326f4
- evidence_id: micro51-gene-RFC1-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and query URL; this is bounded reviewed
    exact-gene uniqueness, not absence of unreviewed homologs.
  accessed_at: '2026-10-22T05:41:51.508971Z'
  support: supports
  summary: The exact reviewed gene/taxon559292 query returns one entry, P38630, supporting
    the maintained current uniqueness note for RFC1.
  snapshot_sha256: c81cae2d85f5ab0ed99a79f10d8ec002beba901230284d143d22c2314b05b096
- evidence_id: micro51-protein-P40348
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40348.json
  locator: Complete identity/status/gene/taxon/name fields, all InterPro xrefs and
    full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp
    retained for reused B48 responses.
  accessed_at: '2026-10-22T05:04:24.505718Z'
  support: supports
  summary: Native reviewed P40348 is RFC2 in S. cerevisiae S288C559292. Identity,
    gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical
    RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an
    exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed
    for this conclusion.
  snapshot_sha256: cd48db2abc9d05e4a2f8f7736b0aced77e8baa2465fb6a839d4f9e8ed95db94e
- evidence_id: micro51-gene-RFC2-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and query URL; this is bounded reviewed
    exact-gene uniqueness, not absence of unreviewed homologs.
  accessed_at: '2026-10-22T05:41:52.108819Z'
  support: supports
  summary: The exact reviewed gene/taxon559292 query returns one entry, P40348, supporting
    the maintained current uniqueness note for RFC2.
  snapshot_sha256: 5d37684d32d00b6803a2cbe7289849926576cd3f08cc74f6dd6ee2b3c1821068
- evidence_id: micro51-protein-P38629
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38629.json
  locator: Complete identity/status/gene/taxon/name fields, all InterPro xrefs and
    full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp
    retained for reused B48 responses.
  accessed_at: '2026-10-22T05:04:23.969177Z'
  support: supports
  summary: Native reviewed P38629 is RFC3 in S. cerevisiae S288C559292. Identity,
    gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical
    RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an
    exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed
    for this conclusion.
  snapshot_sha256: 057ded2799f8c2aaf4cd34a49b0bd062aae33e6e6aa9ab81ec59b7c7d74937dd
- evidence_id: micro51-gene-RFC3-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and query URL; this is bounded reviewed
    exact-gene uniqueness, not absence of unreviewed homologs.
  accessed_at: '2026-10-22T05:41:52.314449Z'
  support: supports
  summary: The exact reviewed gene/taxon559292 query returns one entry, P38629, supporting
    the maintained current uniqueness note for RFC3.
  snapshot_sha256: a84d7bf13eddb61707649c22403a1d9540d4585cd07d07bb31fcbd5f54cff2c3
- evidence_id: micro51-protein-P40339
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40339.json
  locator: Complete identity/status/gene/taxon/name fields, all InterPro xrefs and
    full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp
    retained for reused B48 responses.
  accessed_at: '2026-10-22T05:04:24.107190Z'
  support: supports
  summary: Native reviewed P40339 is RFC4 in S. cerevisiae S288C559292. Identity,
    gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical
    RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an
    exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed
    for this conclusion.
  snapshot_sha256: 09609fcf78c540ff8073114b66b849691895e1fc7de9e81219d81dc51fcc35d7
- evidence_id: micro51-gene-RFC4-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and query URL; this is bounded reviewed
    exact-gene uniqueness, not absence of unreviewed homologs.
  accessed_at: '2026-10-22T05:41:52.318845Z'
  support: supports
  summary: The exact reviewed gene/taxon559292 query returns one entry, P40339, supporting
    the maintained current uniqueness note for RFC4.
  snapshot_sha256: e4ac27ef43308dc3dd4c47939cb4856e61e23e412f8815e785cfb8d758e80a5c
- evidence_id: micro51-protein-P38251
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38251.json
  locator: Complete identity/status/gene/taxon/name fields, all InterPro xrefs and
    full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments; original access timestamp
    retained for reused B48 responses.
  accessed_at: '2026-10-22T05:04:23.366169Z'
  support: supports
  summary: Native reviewed P38251 is RFC5 in S. cerevisiae S288C559292. Identity,
    gene, InterPro xrefs, FUNCTION/SUBUNIT and location comments were checked. Canonical
    RFC membership is explicit; broad clamp-loader/domain xrefs do not establish an
    exact subunit-specific family. Unrelated RFC-like-complex clauses are not needed
    for this conclusion.
  snapshot_sha256: bebaced0b8314c495257a26b5d1357bde108a903ac25fc337c51d4970294ff06
- evidence_id: micro51-gene-RFC5-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and query URL; this is bounded reviewed
    exact-gene uniqueness, not absence of unreviewed homologs.
  accessed_at: '2026-10-22T05:41:52.377199Z'
  support: supports
  summary: The exact reviewed gene/taxon559292 query returns one entry, P38251, supporting
    the maintained current uniqueness note for RFC5.
  snapshot_sha256: 7cfa80c9ae09adeac609a00eb5e3ddcecb79fc26d7ce7848ce2f6f772cfcaabb
- evidence_id: micro51-ipr-IPR050238
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: Complete metadata name/type/signatures and generated-prose flags; no exact
    small-subunit mapping inferred.
  accessed_at: '2026-10-22T05:42:54.096958Z'
  support: supports
  summary: IPR050238 is a broader clamp-loader-complex family and does not distinguish
    RFC2/3/4/5. Its generated unchecked description is not an independent primary
    mechanism source.
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
- evidence_id: micro51-ipr-IPR013748
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013748/
  locator: Complete native accession/name/type/description and PF08542 signature.
  accessed_at: '2026-10-22T05:42:55.620403Z'
  support: supports
  summary: IPR013748 is a C-terminal domain, not an exact whole RFC subunit class.
  snapshot_sha256: 57bf4734514098173ad40fec18cbe6616de4603df0cd5226f6c97ffb42f339a7
- evidence_id: micro51-cullmann1995-cshl-pdf
  kind: primary_source
  reference: https://repository.cshl.edu/id/eprint/24950/1/Characterization%20of%20the%20five%20replication%20factor%20C.pdf
  locator: Original PDF title/abstract/Introductionp4661; complete Methodsp4662; Results
    cloning/mappingp4663; p4665 Table1 and viability paragraph; Discussionp4668–4669/Fig8
    caption. Sequence-alignment pages not independently read.
  accessed_at: '2026-10-22T05:45:12.830889Z'
  support: supports
  summary: The primary paper identifies five RFC genes, with peptide sequences for
    Rfc1/2/4/5 and Rfc3 supported by homology/prior immunoblot work. RFC2–5 disruption
    demonstrates viability requirements, not loss of physical complex assembly. Conserved
    sequence relationships and PCNA interactions are discussed with direct-versus-indirect
    alternatives retained.
  snapshot_sha256: 87555bf179702af221aec2fb878236eaeebc20821fb52ad62d1e9c2eb1f9253f
- evidence_id: micro51-gary1995-page4986
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/c082d190d843/nar00024-0060.png
  locator: 'Original journal page4986 scan: actual pixels and all scientific text/caption
    content inspected; no quantitative image reanalysis.'
  accessed_at: '2026-10-22T05:44:56.472141Z'
  support: supports
  summary: Title/abstract, Introduction and beginning Methods establish the five-subunit
    question, biological context and strain/plasmid setup.
  snapshot_sha256: cc7818b0c0e5ccddc4306ba8b0b512527a14df0de3c06b321dd103e766b2a59b
- evidence_id: micro51-gary1995-page4987
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/a20ddcdc4617/nar00024-0061.png
  locator: 'Original journal page4987 scan: actual pixels and all scientific text/caption
    content inspected; no quantitative image reanalysis.'
  accessed_at: '2026-10-22T05:44:56.472641Z'
  support: supports
  summary: Methods and opening Results describe RFC purification, recombinant work
    and RFC5 cloning; assay conditions and construct distinctions were inspected.
  snapshot_sha256: 3b341e02fe047f4511cd71e232adfecf08b8517da65591a4176263f012fcd4ac
- evidence_id: micro51-gary1995-page4988
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/2a28a2436cf0/nar00024-0062.png
  locator: 'Original journal page4988 scan: actual pixels and all scientific text/caption
    content inspected; no quantitative image reanalysis.'
  accessed_at: '2026-10-22T05:44:56.472865Z'
  support: supports
  summary: Results/Fig1–2 describe Rfc5 sequence and recombinant protein identification;
    similar gel mobility alone does not identify the subunit unambiguously.
  snapshot_sha256: 9afc541a8314781b4d9fa808c13b0f843718e7ba5166ed93edf1f1332aabd5be
- evidence_id: micro51-gary1995-page4989
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/893d6e21a8be/nar00024-0063.png
  locator: 'Original journal page4989 scan: actual pixels and all scientific text/caption
    content inspected; no quantitative image reanalysis.'
  accessed_at: '2026-10-22T05:44:56.473037Z'
  support: supports
  summary: Results/Fig3 show the four-subunit complex can co-purify and has ATPase
    activity yet lacks RFC activity; this is not a failure of physical formation.
  snapshot_sha256: f3c70dead5328ac15d5b105dd7f1b519682ad3834559f338a93596e888682a05
- evidence_id: micro51-gary1995-page4990
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b702/307503/87a02523b583/nar00024-0064.png
  locator: 'Original journal page4990 scan: actual pixels and all scientific text/caption
    content inspected; no quantitative image reanalysis.'
  accessed_at: '2026-10-22T05:44:56.473216Z'
  support: supports
  summary: Results/Discussion/Fig4 show RFC5 co-overexpression restores functional
    RFC activity and discuss fifth-subunit identification. Viability and clamp-loader
    activity remain distinct from physical assembly.
  snapshot_sha256: cc8f0a8827d890a9aab4ff7002611ddfc96f0753249a0007e367a0c06bf70c53
- evidence_id: micro51-nishida2005-pdf
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/ggs/80/2/80_2_83/_pdf/-char/en
  locator: PDF title/complete abstract and Introductionpp83–84; beginning Methodsp84
    Materials and mutagenesis setup only. Later Results/Discussion not independently
    read.
  accessed_at: '2026-10-22T05:44:56.786207Z'
  support: supports
  summary: The primary abstract and Introduction distinguish archaeal one-large/four-small
    RFC from eukaryotic five different subunits and describe the stable PCNA–RFC–DNA
    complex question. Recombinant E. coli expression does not make the archaeal complex
    bacterial.
  snapshot_sha256: 5b912fbc509dfd093e7356d6f31cac710e9c8bd139bd2054ec107fed8e057c1b
- evidence_id: micro51-kim2003-publisher
  kind: database
  reference: https://doi.org/10.1016/j.cub.2003.10.048
  locator: Actual native status and inspected response text; no scientific body inferred
    from successful HTTP status.
  accessed_at: '2026-10-22T05:42:48.439943Z'
  support: context_only
  summary: HTTP200 contains a LinkingHub Redirecting locator page, not the article
    body.
  snapshot_sha256: 35892ac737a1148299b5602719dc71f7b24628eca283b1e019befde45d6f5911
- evidence_id: micro51-kitabayashi2003-publisher
  kind: database
  reference: https://doi.org/10.1271/bbb.67.2373
  locator: Actual native status and inspected response text; no scientific body inferred
    from successful HTTP status.
  accessed_at: '2026-10-22T05:42:48.634215Z'
  support: context_only
  summary: HTTP403 challenge response does not supply the article main body.
  snapshot_sha256: f5174970bceb22789d2ba517951ddb719092eedd77cb453303ff8c74c6592e73
- evidence_id: micro51-cullmann1995-pdf
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC230709/pdf/154661.pdf
  locator: Actual native status and inspected response text; no scientific body inferred
    from successful HTTP status.
  accessed_at: '2026-10-22T05:44:01.248943Z'
  support: context_only
  summary: HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages;
    the separately captured CSHL PDF is the genuine body.
  snapshot_sha256: cf16e9fdeee914a3db18be8e6daebbba224fbb62b67af4b24cf2e553b6c2c46b
- evidence_id: micro51-gary1995-pdf
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307503/pdf/nar00024-0060.pdf
  locator: Actual native status and inspected response text; no scientific body inferred
    from successful HTTP status.
  accessed_at: '2026-10-22T05:44:01.249493Z'
  support: context_only
  summary: HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages;
    original page scans provide the actually inspected body.
  snapshot_sha256: 9831ae1d0a9d6412e90a59379b4c358a0c6fcc28dd4e260c0798239cb76604d9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_replication_factor_c_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:26Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_replication_factor_c_complex.yaml'
  snapshot_sha256: 1f1e41eb9500052052f77a6fc2259ad0152f7793dbfac5efd771c57055d60993
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_replication_factor_c_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:28Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_replication_factor_c_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_c_complex-strict.tsv"
  snapshot_sha256: 84cfb4866c7fc322faa9fa0750cbd2e47982e580739f89f69949a8fe21608c39
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native causal-graphs report
  accessed_at: '2026-10-22T05:43:03.862110Z'
  support: supports
  summary: "data/structures/other/dna_replication_factor_c_complex.yaml  (GO:0005663)\n\
    \  rfc_pcna_loading\trfc1_large_subunit\tCOVERED\t->rfc1_large_subunit (UniProtKB:P38630)\n\
    \  rfc_pcna_loading\trfc2_subunit\tCOVERED\t->rfc2_subunit (UniProtKB:P40348)\n\
    \  rfc_pcna_loading\trfc3_subunit\tCOVERED\t->rfc3_subunit (UniProtKB:P38629)\n\
    \  rfc_pcna_loading\trfc4_subunit\tCOVERED\t->rfc4_subunit (UniProtKB:P40339)\n\
    \  rfc_pcna_loading\trfc5_subunit\tCOVERED\t->rfc5_subunit (UniProtKB:P38251)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     5  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     5\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 8fe53b9e87565355d70e5600509e38c4dfda6fcd88d47a294b9dfde6859f89f1
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --verify
  locator: Complete focused read-only native verify report
  accessed_at: '2026-10-22T05:43:16.359332Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: 638316eb6d04c49acacf1717010fa10a01d9d9954e01afa43caa919455bb88b3
- evidence_id: native-verify-network
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --verify
  locator: Complete focused read-only native verify report
  accessed_at: '2026-10-22T05:43:49.117728Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_replication_factor_c_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '17 of 22 collected target identifiers returned OK. PMID:14614842: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:14646196: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force.; PMID:16172520: UNREACHABLE; Exact native EuropePMC
    MED identifier, title and DOI independently inspected after the bulk eutils414
    transport failure. Identifier resolution does not certify all biological claims;
    declared primary-body and abstract reading limits remain in force.; PMID:7651383:
    UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently
    inspected after the bulk eutils414 transport failure. Identifier resolution does
    not certify all biological claims; declared primary-body and abstract reading
    limits remain in force.; PMID:8559655: UNREACHABLE; Exact native EuropePMC MED
    identifier, title and DOI independently inspected after the bulk eutils414 transport
    failure. Identifier resolution does not certify all biological claims; declared
    primary-body and abstract reading limits remain in force. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
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
  topic: Canonical yeast RFC and broader ontology scope
  outcome: supported
  target_ids:
  - GO:0005663
  summary: The record distinguishes the generic RFC class from its five named budding-yeast
    subunits. GO identity, protein-complex hierarchy, replication-fork parthood, clamp-loading
    function and reference yeast example are supported. Archaeal papers appear as
    exact GO definition references; they are not used to assert yeast five-subunit
    experiments.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-pmid-7651383-network
  - micro51-pmid-8559655-network
  - micro51-pmid-14614842-network
  - micro51-pmid-14646196-network
  - micro51-pmid-16172520-network
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
- assessment_id: proteins
  area: grounding
  topic: Five verified protein instances and RFC1 family gap
  outcome: concern
  target_ids:
  - GO:0005663
  summary: All five reviewed S288C accessions, gene/taxon pairs and current single-hit
    query notes agree with native entries. Native IPR012178 exactly represents RFC1;
    IPR050238 and IPR013748 do not justify assigning exact RFC2–5 family identities.
    Only RFC1 has a confirmed actionable family omission.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-ipr-IPR012178
  - micro51-protein-P38630-network
  - micro51-gene-RFC1-network
  - micro51-protein-P40348
  - micro51-gene-RFC2-network
  - micro51-protein-P38629
  - micro51-gene-RFC3-network
  - micro51-protein-P40339
  - micro51-gene-RFC4-network
  - micro51-protein-P38251
  - micro51-gene-RFC5-network
  - micro51-ipr-IPR050238
  - micro51-ipr-IPR013748
- assessment_id: formation
  area: grounding
  topic: Unknown formation necessity is appropriately retained
  outcome: unknown
  target_ids:
  - GO:0005663
  summary: All five essentialities remain UNKNOWN. Cullmann’s viability results and
    Gary’s functional restoration establish important biological requirements, but
    Gary also recovers a four-subunit physical complex. This directly cautions against
    substituting clamp-loading activity or viability for formation necessity.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
- assessment_id: topology
  area: graph
  topic: Seven-edge descriptive composition/function graph
  outcome: supported
  target_ids:
  - GO:0005663
  summary: Five constituent-to-RFC edges plus clamp-loader and replication function
    edges are supported at their stated broad scope. The explicit NONMECHANISTIC graph
    does not overclaim a loading cycle or interfaces.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
  - graphs
- assessment_id: taxonomic-scope
  area: scope
  topic: Taxon identity, majority semantics and experimental boundaries
  outcome: supported
  target_ids:
  - GO:0005663
  summary: The named yeast taxon and canonical system agree with the primary studies;
    S288C entries are reference examples, not claims that every experiment used that
    strain. COMMON retains its schema meaning present in most members with exceptional
    losses. The sources provide qualitative conservation/system support rather than
    a measured prevalence census; no artificial census requirement is imposed.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
  - micro51-pmid-7651383-network
  - micro51-pmid-8559655-network
  - micro51-pmid-14614842-network
  - micro51-pmid-14646196-network
  - micro51-pmid-16172520-network
- assessment_id: coverage
  area: completeness
  topic: Whole-target coverage with bounded unresolved enrichment
  outcome: supported
  target_ids:
  - GO:0005663
  summary: The complete maintained target, each source claim, graph edge, component
    state, protein example, discussion and history was assessed. Exact actionable
    class mappings are distinguished from unresolved broader/domain candidates and
    optional enrichment. Existing historical access/curation notes are not judged
    false merely because this review recovered additional sources.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-cullmann1995-cshl-pdf
  - micro51-gary1995-page4986
  - micro51-gary1995-page4987
  - micro51-gary1995-page4988
  - micro51-gary1995-page4989
  - micro51-gary1995-page4990
  - micro51-nishida2005-pdf
  - micro51-ipr-IPR012178
  - micro51-protein-P38630-network
  - micro51-gene-RFC1-network
  - micro51-protein-P40348
  - micro51-gene-RFC2-network
  - micro51-protein-P38629
  - micro51-gene-RFC3-network
  - micro51-protein-P40339
  - micro51-gene-RFC4-network
  - micro51-protein-P38251
  - micro51-gene-RFC5-network
findings:
- finding_id: F1
  issue_key: dna-replication-factor-c-complex-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified exact subunit family grounding
  description: The named RFC1 large-subunit class exactly matches IPR012178, verified
    from native family metadata/signature and the maintained P38630 UniProt cross-reference.
    The current REVIEWED_LABEL_ONLY row and OPEN task leave this resolvable match
    unrepresented. No exact RFC2–5 mapping is established by broad IPR050238 or C-terminal
    IPR013748. Historical statements about what was curated in an earlier pass are
    preserved as history, not declared fabricated.
  target_ids:
  - GO:0005663
  field_paths:
  - components[0].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005663-ancestors-network
  - micro51-GO0005663-constraints-network
  - micro51-tax4932-network
  - micro51-tax559292-network
  - micro51-ipr-IPR012178
  - micro51-protein-P38630-network
  - micro51-gene-RFC1-network
  - micro51-protein-P40348
  - micro51-gene-RFC2-network
  - micro51-protein-P38629
  - micro51-gene-RFC3-network
  - micro51-protein-P40339
  - micro51-gene-RFC4-network
  - micro51-protein-P38251
  - micro51-gene-RFC5-network
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: The biological class, composition and protein identities remain
    correct. This is a bounded actionable class-grounding gap under the explicit REVIEWED_LABEL_ONLY
    contract, not a missing optional example inventory.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005663
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
  description: Ground the verified class RFC1 to IPR012178 with source-backed family
    evidence and update the corresponding open task/status. Preserve unresolved classes
    and historical provenance; keep organism accessions as examples.
  acceptance_checks:
  - Each added family denotes the existing whole-protein class rather than a domain,
    broader homolog group or species accession.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Cullmann1995 was independently read at the selected pages/sections listed, not every
  sequence alignment. Gary1995 original scans4986–4990 were visually inspected; retained
  page4991 references were not used. No quantitative figure reanalysis or supplement
  was performed.
- 'Kim/MacNeill2003 and Kitabayashi2003 remain complete-abstract-only sources: the
  former publisher200 is a redirect locator and the latter403. Nishida2005 body inspection
  is restricted to title/abstract/Introduction and beginning Methods, not later Results.'
- The exact RFC1 family is established; bounded family metadata/search inspection
  did not establish exact RFC2–5 families. This is not an exhaustive absence claim.
  S288C reference accessions are distinct from the paper’s experimental yeast strains.
- Native initial DNS failures and successful network retries are retained separately.
  An HTTP200 redirect, download challenge or abstract landing page is never treated
  as full scientific text.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests one review for every unreviewed record, including qualified clean
  records.
- Native UniProt/ontology/family adapters directly address these eukaryotic complex
  claims. No matched iModulonDB organism/dataset is established or used; expression-module
  evidence would not prove physical assembly.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
