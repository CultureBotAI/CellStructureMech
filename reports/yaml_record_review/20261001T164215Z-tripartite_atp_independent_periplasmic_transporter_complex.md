# YAML Record Review: tripartite ATP-independent periplasmic transporter complex

- PR: #1878
- Record: `data/structures/other/tripartite_atp_independent_periplasmic_transporter_complex.yaml`
- Identifier: `GO:0031317`
- Reviewed at: 2026-10-01T16:42:15Z

## Scope

Adversarial review of the new TRAP transporter complex record, its append-only
history record, and generated README/page/embedding artifacts.

## Checks

- Re-ran a hidden/ignored-inclusive duplicate search for `GO:0031317`, the GO
  label, exact GO synonyms, and the primary/review DOI and PMID values across
  `data/structures`, `history`, `pages`, `reports`, `README.md`, and `docs`.
  Hits are limited to this PR's new record, generated pages/data, and history
  report outputs.
- Verified `GO:0031317` as an active QuickGO cellular-component term with exact
  `TRAP transporter complex` and `TRAP-T transporter complex` synonyms and
  `is_a GO:1990351`.
- Checked the R. capsulatus DctPQM evidence against Forward et al. 1997 via
  PMID:9287004, PMCID:PMC179420, and DOI:10.1128/JB.179.17.5482-5493.1997.
  The abstract supports the DctP receptor, DctQ and DctM membrane-protein
  genes, complementation by `dctPQM`, proton-motive-force coupling, and the
  proposed TRAP name.
- Checked broad component and taxonomic framing against Rabus et al. 1999 and
  Mulligan, Fischer and Thomas 2011 PubMed abstracts. These support the DctP or
  TAXI substrate-binding-protein split, unequal DctQ/DctM integral membrane
  proteins, and presence across prokaryotes including bacteria and archaea.
- Queried InterPro before grounding components. `InterPro:IPR004681` exactly
  names the large DctM membrane family and `InterPro:IPR007387` exactly names
  the small DctQ membrane family; the receptor class remains
  `REVIEWED_LABEL_ONLY` because DctP and TAXI receptors are separate family
  branches.
- Verified NCBI Taxonomy labels for `NCBITaxon:2` Bacteria,
  `NCBITaxon:2157` Archaea, and `NCBITaxon:1061` Rhodobacter capsulatus.
- Verified the record, generated artifacts, and full corpus with the local
  validation suite listed in the PR body, including `scripts/run_qc.py`.

## Findings

No concrete defects found. No review issue filed.

## Residual Risk

- OUP's FEMS Microbiology Reviews article pages for
  DOI:10.1111/j.1574-6976.2010.00236.x were Cloudflare-blocked during review,
  so the review relied on PubMed/Crossref metadata and the PubMed abstract for
  that review article rather than full-text passages.
- The initial receptor grounding is intentionally conservative. A single exact
  source-neutral family covering both DctP and TAXI receptors was not found in
  the InterPro search, so the open `resolve_trap_receptor_grounding` discussion
  should stay open until a curator can prove a narrower or cross-family CURIE.
