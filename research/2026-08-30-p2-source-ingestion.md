# P2 source ingestion design and live measurements (2026-08-30)

This note records the evidence behind the `complex_portal`, `emdb_empiar` and
`pmc_oa` adapters. Counts are dated observations, not timeless claims.

## Complex Portal

The exact accession endpoint returned:

- `CPX-3802`, *30S small ribosomal subunit*, *Escherichia coli* K-12
  (`NCBITaxon:83333`): 22 participants (21 proteins plus 16S rRNA), each at
  stoichiometry 1, evidence `ECO:0005547` (inferred by curator).
- `CPX-3807`, *50S large ribosomal subunit*, the matching large-subunit entry.
- `CPX-4022`, *ATP synthase complex*: c10, b2, delta1, alpha3, beta3, gamma1,
  epsilon1 and a1. A text search also returned the unrelated flagellar export
  complex because one participant is named "flagellum-specific ATP synthase";
  search hits therefore cannot be treated as identity.

Complex Portal's 2022 resource paper states that all data, including web
pages/services, are CC0. The earlier queue value `ATTRIBUTION` confused the
paper's CC BY licence with the database content licence and was corrected.

Design consequence: source participants are taxon-specific instances, while
the repository's canonical `components` are families/classes. The new
`complex_compositions` assertion preserves the exact source taxon, CPX id,
participants and stoichiometry. Applying an entry requires an exact accession,
an already asserted taxon and a curator scope note; it never creates an
equivalence `xrefs` value.

## EMPIAR linked to EMDB

EMPIAR entry JSON provides its DOI, authors, imaging-set metadata and EMDB
cross-references, but no organism/taxid. EMDB supplies NCBI taxids under
`natural_source`. EMDB policy requires a depositor-supplied representative
figure that is not subject to copyright restrictions, and released EMDB data
and metadata are distributed without restriction. EMPIAR policy makes the raw
archive CC0 and likewise requires a restriction-free thumbnail.

Live keyword-cohort measurement using
`/emdb/api/empiar/search/<query>?rows=10000`:

| EMPIAR query | Released entries | With at least one EMDB xref | Fraction | Scale values |
|---|---:|---:|---:|---|
| `bacteria` | 93 | 87 | 93.5% | 61 molecule, 7 cell, 2 tissue, 2 virus, 21 unspecified |
| `archaea` | 4 | 4 | 100% | 3 molecule, 1 unspecified |

These are full-text keyword cohorts, not authoritative taxonomic sets: that
limitation is precisely why the adapter resolves and verifies a chosen EMDB
entry rather than inferring a taxon from the EMPIAR title.

The adapter records the raw EMPIAR object as a `Dataset` and the linked,
lightweight EMDB depositor PNG as a `StructureImage`. A live Thermus canary
correctly refused import: EMDB asserted strain `NCBITaxon:300852`, while the
record only named species `NCBITaxon:274`. Imaging resolution is retained in
image notes; it is not a biological structure dimension and is never written
to `physical_properties`.

## PMC Open Access on AWS

PMC's August 2026 transition retires the OA Web Service and legacy distribution
prefixes. The adapter uses only the new versioned objects:

- `metadata/PMC….<version>.json` for the licence family, DOI/PMID and md5-bearing
  XML/media URLs;
- the versioned JATS XML for the exact Creative Commons version, `fig/@id`,
  caption and author attribution;
- the versioned media object, whose bytes must match the metadata md5.

Only exact `CC BY` or `CC0` metadata values are hostable, and a recognized JATS
licence URL must specify the version and agree with that metadata family. A bare
`CC BY` value is never guessed to mean 4.0. PMC supplies no taxon, so the curator
provides one that must already occur on the target record.
Figures whose captions look multi-panel require explicit acknowledgement.
`PMC1872035` remains absent from the current S3 dataset and is reported as
unavailable rather than fetched by scraping the article website.

Figure-level coverage sampled the top 25 relevance-sorted CC BY Entrez hits per
current structure query. A candidate is a JATS figure whose caption says
micrograph or electron-microscopy image; counts do not imply that every panel
is suitable for hosting.

| Query | Total CC BY article hits | Current S3 articles scanned | Articles with candidates | Candidate figures |
|---|---:|---:|---:|---:|
| `carboxysome[Title/Abstract]` | 104 | 24/25 (1 unavailable) | 8 | 14 |
| `"S-layer"[Title/Abstract] AND (bacterium OR archaea)` | 315 | 24/25 (1 unavailable) | 4 | 6 |
| `"bacterial flagellum"[Title/Abstract]` | 102 | 25/25 | 7 | 12 |
| `"bacterial ribosome"[Title/Abstract]` | 132 | 25/25 | 1 | 1 |

This establishes that the pool is productive, while also quantifying its
manual-review burden. For example, the leading carboxysome candidates were
valid CC BY figures but mixed microscopy, diagrams and plots in one composite;
the importer rejected silent single-modality treatment.

## Primary sources

- Complex Portal [documentation](https://www.ebi.ac.uk/complexportal/documentation),
  [downloads](https://www.ebi.ac.uk/complexportal/download), and
  [2022 data-licensing statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC8689886/)
- EMPIAR [REST API](https://www.ebi.ac.uk/empiar/api/documentation/),
  [policies](https://www.ebi.ac.uk/empiar/policies/)
- EMDB [REST API](https://www.ebi.ac.uk/emdb/api/) and
  [policies](https://www.ebi.ac.uk/emdb/policies.html)
- PMC [Article Datasets on AWS](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/)
