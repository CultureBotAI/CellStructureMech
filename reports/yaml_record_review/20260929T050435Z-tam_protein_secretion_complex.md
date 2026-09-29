# YAML Record Review: tam_protein_secretion_complex

- PR: #1762
- Issue: #1763
- Record: `data/structures/secretion_system/tam_protein_secretion_complex.yaml`
- Reviewed at: 2026-09-29T05:04:35Z
- Result: changes requested

## Scope

Adversarial review of the new `GO:0097347` TAM protein secretion complex
record, its append-only history entry, and regenerated CellStructureMech pages,
docs, and embedding artifacts in PR #1762.

The review compared the new record with the live QuickGO `GO:0097347`
cellular-component term, its `GO:0032991` ancestor, the NCBI and Europe PMC
metadata for the GO definition paper PMID:22466966 / DOI:10.1038/nsmb.2261,
and adjacent secretion-system records.

## Findings

### #1763: Selkrig evidence notes do not disclose abstract-only access

Severity: medium

The record uses PMID:22466966 and DOI:10.1038/nsmb.2261 for Selkrig et al.
2012, the paper GO cites in the `GO:0097347` definition. NCBI and Europe PMC
verify that this is the TAM discovery paper, and the public abstract directly
supports the record's TamA/TamB composition claim.

Europe PMC also reports the paper is not open access, is not in PMC, and has no
PDF route there. Because the current PMID-backed notes do not say they are
bounded to the PubMed/Europe PMC abstract, they can read as if the
subscription-only full text was opened. The fix should keep the PMID/DOI
evidence but explicitly scope the TamA/TamB claim to the abstract-visible text
and leave `snippet` empty.

## Non-Findings

- The PR file list on GitHub matched the expected 14-file local change set.
- `GO:0097347` is an exact cellular-component identifier for the new record.
- `GO:0097347` is current, unrestricted, and has `GO:0032991` as an ancestor.
- Hidden/ignored-inclusive duplicate searches found no pre-existing
  `GO:0097347`, TAM protein secretion complex, translocation and assembly
  module protein complex, PMID:22466966, or DOI:10.1038/nsmb.2261 references
  before the new record.
- The first record leaves TamA/TamB component groundings reviewed-label-only
  rather than guessing InterPro, Pfam, or NCBIfam CURIEs.
