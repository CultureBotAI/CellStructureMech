# Adversarial YAML Review: phenylacetyl-CoA 1,2-epoxidase complex

- PR: #1895
- Reviewed head: `1a6a8066`
- Record: `data/structures/other/phenylacetyl_coa_1_2_epoxidase_complex.yaml`
- Report timestamp: `20261002T022038Z`

## Scope

Reviewed the new `GO:0062077` phenylacetyl-CoA 1,2-epoxidase complex record,
its append-only history record, generated embedding JSON, and rendered pages.

## Evidence And Identity

- QuickGO resolved `GO:0062077` as an active cellular-component term named
  `phenylacetyl-CoA 1,2-epoxidase complex`, with `paaABCE complex` synonymy.
- QuickGO listed `GO:0062077` as an `is_a` child of `GO:1990204`
  `oxidoreductase complex`.
- QuickGO resolved `GO:0097266` as active `phenylacetyl-CoA 1,2-epoxidase
  activity`.
- Local OAK GO resolved both `GO:0062077` and `GO:0097266` canonically, so the
  record did not need an id-label exception.
- QuickGO annotations for `Escherichia coli` K-12 included `PaaA`, `PaaB`,
  `PaaC`, and `PaaE` part-of annotations to `GO:0062077`, with no `PaaD`
  part-of annotation.
- Complex Portal resolved `CPX-2844` as the `Escherichia coli` K-12
  phenylacetyl-CoA 1,2-epoxidase complex and listed the protein members as two
  PaaA, two PaaB, two PaaC, and one PaaE.
- PubMed resolved the primary `PMID:21247899` citation as Grishin et al. 2011,
  DOI `10.1074/jbc.M110.194423`, and the full-text PMC route made the
  component-boundary evidence readable.
- InterPro resolved exact family entries for PaaA (`IPR011881`), PaaB
  (`IPR009359`), PaaC (`IPR011882`), and PaaE (`IPR011884`).
- UniProt resolved reviewed `Escherichia coli` K-12 PaaA, PaaB, PaaC, and PaaE
  accessions `P76077`, `P76078`, `P76079`, and `P76081`.

## Duplicate Check

Before adding the record, a hidden/ignored-inclusive duplicate search over
`data`, `history`, `pages`, `reports`, `scripts`, `docs`, `src`, `curation`,
`research`, and `.github` found no pre-existing exact record for:

- `GO:0062077`
- `phenylacetyl-CoA 1,2-epoxidase complex`
- `phenylacetyl-CoA 1,2-epoxidase`
- `paaABCE`
- `paaABCDE`
- `PMID:21247899`
- `paaA`
- `paaB`
- `paaC`
- `paaD`
- `paaE`

After scaffolding, a second hidden/ignored-inclusive review confirmed the
excluded PaaD UniProt accession `P76080` and InterPro accession `IPR011883`
were not asserted in the new record, rendered page, history record, reports, or
generated data. The only post-scaffold `PaaD` mentions in those paths were the
expected resolved boundary discussion entries that document why PaaD was not
modeled as a complex component.

## Rendered Artifact Review

- Confirmed `pages/structures/other/phenylacetyl_coa_1_2_epoxidase_complex.html`
  links `GO:0062077`, `GO:0097266`, `InterPro:IPR011881`,
  `InterPro:IPR009359`, `InterPro:IPR011882`, `InterPro:IPR011884`,
  `UniProtKB:P76077`, `UniProtKB:P76078`, `UniProtKB:P76079`,
  `UniProtKB:P76081`, `CPX:CPX-2844`, `PMID:21247899`, and
  `DOI:10.1074/jbc.M110.194423`.
- Confirmed `pages/data/structure_text_map.json` is byte-identical to
  `data/embeddings/structure_text_map.json`.
- Confirmed `pages/data/structure_text_neighbors.json` is byte-identical to
  `data/embeddings/structure_text_neighbors.json`.

## Validation

- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- Single-record `linkml-validate`
- Single-record `scripts/validate_strict.py --quiet`
- Single-history `scripts/validate_history.py`
- Full `scripts/validate_strict.py --quiet`
- Full `scripts/validate_history.py`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

## Findings

No concrete defects found. No review issue filed.
