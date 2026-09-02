# SubtiWiki v5 reassessment and narrow ingestion — 2026-09-01

## Outcome

SubtiWiki is adopted only as a **CURATE_ONLY** identifier source. Its live v5
site, API documentation, Swagger document, application bundle and 2025 database
paper still provide no database redistribution licence. The CC BY-NC 4.0 notice
on the Nucleic Acids Research paper governs the article, not the database.

The adapter therefore reads only one exact category and exact per-gene outlink
endpoints. It stores UniProt identifiers and SubtiWiki source links, not source
descriptions, functions, sequences, mutant phenotypes, interactions, structures
or bulk exports. The independently licensed UniProt records supply the protein
label, reviewed status, current primary gene and taxon check.

## Live endpoints exercised

- API specification: <https://www.subtiwiki.uni-goettingen.de/v5/api/swagger.json>
- category 387, `Flagellar proteins`, dot notation `4.1.1.2`:
  <https://www.subtiwiki.uni-goettingen.de/v5/api/gene-category/387>
- exact gene outlink pattern, for example FliF:
  <https://www.subtiwiki.uni-goettingen.de/v5/api/gene/1705/outlinks>
- independent UniProt record, for example FliF/P23447:
  <https://rest.uniprot.org/uniprotkb/P23447.json>
- source paper: <https://doi.org/10.1093/nar/gkae957>

## Canary and reviewed boundary

The bacterial-type flagellum record gains 17 reviewed *Bacillus subtilis*
strain 168 protein examples spanning the filament, MS/C rings, both stator
pairs, basal-body rod and type III export gate. Proteins that assemble or
regulate the structure but are not constituents (including FliI/H/J/K/T/W and
FlgD/N) are deliberately excluded. Gram-negative-only L/P-ring proteins are
also excluded.

The first live dry run exposed meaningful historical-name drift:

- SubtiWiki `flgE` links P23446; UniProt now calls the primary gene `flgG` and
  the product a distal basal-body rod protein. It maps to the rod, not the hook.
- SubtiWiki `motP` and `motS` link P39063 and P39064; UniProt primary symbols
  remain `ytxD` and `ytxE`. Their placement in the sodium-coupled stator is
  independently supported by <https://doi.org/10.1016/j.jmb.2005.07.030>.
- The source category's FliY membership is mapped to the C ring only with
  independent support from <https://doi.org/10.1128/JB.00626-18>, which shows
  that FliY replaces the FliN found in the Gram-negative reference complex.

These are explicit allow-list translations. Every other source symbol must
equal the current UniProt primary symbol. Any category identity, membership,
gene id, accession, reviewed-status or taxon change makes the import fail.

Tracked by issue #116.
