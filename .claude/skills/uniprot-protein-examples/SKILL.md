---
name: uniprot-protein-examples
description: "Review CellStructureMech YAML records and add verified, taxon-paired UniProtKB protein_examples to components and causal_graphs GENE_OR_PROTEIN elements. Use when auditing or enriching protein examples, resolving missing gene symbols on structural components or causal-graph nodes, or verifying UniProt accessions, entry statuses, and NCBI taxon labels."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate and verify UniProt `protein_examples` across components and `causal_graphs`

Every `PROTEIN` component — and every `PROTEIN_COMPLEX` component with named
subunit genes — can carry taxon-paired `protein_examples` linking the abstract
structural component to concrete, reviewed `UniProtKB:<accession>` entries in the
organisms named by the record's `canonical_examples`.

In `causal_graphs`, nodes with `node_type: GENE_OR_PROTEIN` rely on this
grounding through two complementary routes:

1. **Structural components (`component_ref`)**: When a `GENE_OR_PROTEIN` node is
   part of the record's structure, it links to `components[].component_id` via
   `component_ref`, and the target component carries `gene_symbols` and
   taxon-paired `protein_examples`.
2. **External regulators, chaperones, or substrates (`CausalNode.xrefs`)**: When
   a `GENE_OR_PROTEIN` causal node is an external actor (for example, the
   chemotaxis response regulator `CheY-P` acting on the flagellar C-ring, or an
   assembly chaperone/usher not retained in the mature structure), it should not
   be fabricated as a structural component; instead, its verified
   `UniProtKB:<accession>` in the record's canonical taxon is recorded in the
   node's own `xrefs` list.

`scripts/uniprot_genes.py` and `scripts/uniprot_sl.py` are the deterministic
adapters. This skill is the curation judgement around them.

## Modes and commands

```bash
# 1. Audit causal_graphs GENE_OR_PROTEIN nodes and their protein_examples coverage
uv run python scripts/uniprot_genes.py --causal-graphs
uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/<cat>/<rec>.yaml

# 2. Dry-run and apply gene-symbol seeding on PROTEIN components
uv run python scripts/uniprot_genes.py --record data/structures/<cat>/<rec>.yaml
uv run python scripts/uniprot_genes.py --record data/structures/<cat>/<rec>.yaml --apply

# 3. Include PROTEIN_COMPLEX components that declare subunit gene_symbols
uv run python scripts/uniprot_genes.py --include-complexes --record data/structures/<cat>/<rec>.yaml --apply

# 4. Inspect remaining gaps and why each symbol could not be auto-seeded
uv run python scripts/uniprot_genes.py --gaps
uv run python scripts/uniprot_genes.py --gaps --include-complexes

# 5. Seed from UniProt Subcellular Location (SL) where the record's GO CC maps to SL
uv run python scripts/uniprot_sl.py proteins --record data/structures/<cat>/<rec>.yaml

# 6. Verify all existing protein_examples and CausalNode UniProtKB xrefs against live UniProt/NCBI
uv run python scripts/uniprot_genes.py --verify
```

## Non-negotiable rules

1. **The "exactly one" rule for automatic seeding.**
   `(gene_exact:<symbol>) AND (taxonomy_id:<taxon>) AND (reviewed:true)` is safe
   only when it resolves to a single reviewed Swiss-Prot entry (or a single
   entry at the exact taxon node named on the record when sub-strains duplicate
   the protein). When a symbol returns multiple reviewed paralogs/alleles in a
   taxon (e.g. `pilA` in *P. aeruginosa*), automatic seeding skips it; a curator
   must inspect the literature cited on the record before choosing an accession.
2. **Re-check the entry's own gene names.**
   UniProt's search index is looser than case-insensitive equality. Always check
   that the returned entry's primary `geneName` or `synonyms` actually match the
   declared symbol before accepting it.
3. **`taxon_id` and `taxon_label` must match the entry and NCBI Taxonomy (#270).**
   - Record the entry's own `organism.taxonId` as `NCBITaxon:<id>`, because a
     record often names a species (*Pseudomonas aeruginosa*, `NCBITaxon:287`)
     while the reviewed UniProt entry sits on a sequenced strain node below it
     (*Pseudomonas aeruginosa PAO1*, `NCBITaxon:208964`).
   - Never copy UniProt's house `organism.scientificName` string (such as
     `"Escherichia coli (strain K12)"`), which fails NCBI correspondence.
   - If the entry's taxon is named in the record's `canonical_examples`, reuse
     the record's `taxon_label` so one taxon ID never carries two labels in the
     corpus; otherwise use NCBI's official scientific name via
     `cellstructuremech.ingest.ncbi_taxon_names`.
4. **Read `entry_status` off the entry (#262, #271).**
   Map `"UniProtKB reviewed (Swiss-Prot)"` to `REVIEWED` and
   `"UniProtKB unreviewed (TrEMBL)"` to `UNREVIEWED`. Never assert `REVIEWED`
   without checking `entryType`. Prefer `REVIEWED` entries; use an `UNREVIEWED`
   TrEMBL entry only when a non-model organism has no Swiss-Prot entry for that
   gene and the literature on the record unambiguously identifies the protein.
5. **State honestly what the accession proves.**
   - When seeded by gene symbol (`uniprot_genes.py`), the `role` must state that
     the accession is the reviewed UniProtKB entry for the declared gene symbol
     in that taxon and is not itself independent evidence of structure
     membership.
   - Carry over `ECO:0000269` experimental PubMed evidence from UniProt's
     `SUBCELLULAR LOCATION` comment only for the location UniProt itself names
     (prefixed with the PubMed author/year/title/journal citation). When no
     experimental localisation citation exists on the entry, cite the UniProt
     entry URL (`https://www.uniprot.org/uniprotkb/<acc>`) with an identity-only
     note.

## Workflow for reviewing a record (or the corpus)

### Step 1: Audit `causal_graphs` `GENE_OR_PROTEIN` elements

Run `uv run python scripts/uniprot_genes.py --causal-graphs` (with `--record` for
a single record). Every `GENE_OR_PROTEIN` causal node falls into one of four
states:

1. **Anchored (`component_ref` set) and target component has `protein_examples`**:
   Verify that every declared subunit symbol on the component is represented,
   not just the first symbol (#261, #298).
2. **Anchored (`component_ref` set), target component has `gene_symbols` but no
   `protein_examples`**:
   Run `scripts/uniprot_genes.py` (with `--include-complexes` if the target
   component has `component_type: PROTEIN_COMPLEX`) to resolve each declared
   symbol against the record's `canonical_examples` taxa.
3. **Anchored (`component_ref` set), target component has no `gene_symbols`**:
   Inspect the component's `component_id`, `label`, `description`, `evidence`,
   and the causal node's `label` and `description`.
   - If the component represents a specific protein or a complex of specific
     named subunits (e.g. `act1_swr1c_subunit` -> `ACT1`, `ku70_subunit` ->
     `YKU70`, `dinitrogenase` -> `nifD`, `nifK`, `c_ring` -> `fliG`, `fliM`,
     `fliN`), add the verified `gene_symbols` to the component and then resolve
     its `protein_examples`.
   - Do **not** change `components[].label` or `components[].role` when adding
     `gene_symbols` or `protein_examples` unless correcting an actual scientific
     error, because `label` and `role` are hashed by
     `scripts/build_text_embedding_map.py`.
4. **Unanchored (`component_ref` absent)**:
   - First check whether the node actually denotes one of the record's existing
     `components` (for example, node `mature_lpp` matching component
     `outer_membrane_lipoprotein_links`, or node `prearchaellin` matching
     `archaellins`). If so, set `component_ref` to that `component_id` and ensure
     the component has `gene_symbols` and `protein_examples`.
   - If the node is a genuine external protein (e.g. a kinase, response
     regulator, chaperone, protease, or assembly factor that acts on the
     structure without being a structural component), resolve its gene symbol in
     the record's `canonical_examples` taxa using `resolve_symbol()` and add
     `UniProtKB:<accession>` to the `CausalNode`'s `xrefs` list.

### Step 2: Seed and curate `components[].protein_examples`

1. Run `uv run python scripts/uniprot_genes.py --include-complexes --apply` (on
   the target record or corpus).
2. Run `uv run python scripts/uniprot_genes.py --gaps --include-complexes` to
   inspect remaining gaps by category:
   - `NO_GENE_SYMBOL`: Add `gene_symbols` where the component names a specific
     protein or subunit; leave generic class components (e.g. `"ribosomal
     proteins"`, `"peptidoglycan hydrolases"`, `"cargo proteins"`) without gene
     symbols.
   - `NO_EXACT_GENE_MATCH`: Check whether the record uses a species-specific
     synonym, locus tag, or capitalization variant that UniProt lists under
     another primary symbol (e.g. *S. cerevisiae* `YKU70`/`HDF1`, *H. sapiens*
     `WASHC1`/`WASH1`, *S. pombe* `nda3`). Add the canonical UniProt gene symbol
     to `gene_symbols` and re-run.
   - `AMBIGUOUS_SYMBOL`: Inspect the candidate accessions printed by `--gaps`. If
     the ambiguity comes from multiple reviewed entries across sub-strains or
     paralogs and the record's cited literature identifies which gene/protein is
     meant, curate the specific `protein_example` or disambiguating synonym. If
     the literature does not distinguish between alleles, leave it unseeded.
   - `NO_REVIEWED_ENTRY`: Check whether the record's canonical example uses a
     species taxon where the reviewed Swiss-Prot entry sits on a sibling
     reference strain (e.g. *E. coli* `NCBITaxon:562` vs *E. coli* K-12
     `NCBITaxon:83333`, or *B. subtilis* `NCBITaxon:1423` vs 168
     `NCBITaxon:224308` — note that `taxonomy_id:` searches descendants
     automatically, so species -> strain works out of the box, whereas a record
     pinned to an unreviewed strain will miss a reviewed entry on the parent
     species or reference strain).

### Step 3: Write through the validation gate and verify

All modifications to structure YAML records must:

- Record a `CurationEvent` via
  `cellstructuremech.curate.curation_event.record_curation_event`;
- Write through
  `cellstructuremech.validation.write_validated.write_validated_structure`;
- Create a repository history entry via `just new-history` when performing a
  curation pass;
- Regenerate derived pages and README stats when records change:

```bash
uv run python scripts/uniprot_genes.py --verify
uv run python scripts/check_curies.py --check
just render
just docs-stats
just qc
```

## Related

- `scripts/uniprot_genes.py` — gene-symbol seeding, gap reporting, causal-graph
  audit, and live verification.
- `scripts/uniprot_sl.py` — UniProt Subcellular Location (`SL-NNNN`) xrefs and
  location-based `protein_examples` seeding.
- `scripts/interpro_groundings.py` — downstream InterPro family grounding, which
  consumes `components[].protein_examples`.
- `scripts/check_curies.py` — live CURIE resolution gate (`build/curie_cache.json`).
