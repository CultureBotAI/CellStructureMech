# YAML Record Review: phycobilisome_rod

- **Record:** `data/structures/energy_complex/phycobilisome_rod.yaml`
- **PR:** https://github.com/CultureBotAI/CellStructureMech/pull/1962
- **Initial commit:** `e6cfea00`
- **Review-fix commit:** `e22dc58a`
- **Review issue:** https://github.com/CultureBotAI/CellStructureMech/issues/1963
- **Reviewer:** codex
- **Timestamp:** 2026-10-03T03:01:40Z

## Scope

Adversarial review of the new minted
`cellstructuremech:phycobilisome_rod` record added in PR #1962. The review
covered exact-duplicate rejection, the decision to mint a rod-specific local
identifier rather than use the whole-antenna `GO:0030089` term, parthood to
the whole phycobilisome, parentage under `GO:0030076`, component boundaries for
rod phycobiliproteins and rod/rod-terminal/rod-core linkers, taxonomic scope
for cyanobacteria and red algae, canonical examples, DOI/PMID readability,
causal-graph evidence, generated site output, and append-only history.

Hidden and ignored files were included in the exact duplicate search for the
new identifier, top-level label, exact synonym, and old evidence identifiers
before the record was added. No exact maintained identifier, top-level label,
or synonym duplicate was found outside `.git`.

## Findings

### #1963: Sui/Chang-backed rod assertions exceeded the readable evidence

The initial rod record used the Sui 2021 phycobilisome review
(`DOI:10.1146/annurev-biophys-062920-063657`) as the `definition_source` and
as evidence for rod-specific component, transfer, boundary, and curation-TODO
statements. The scoped literature helper could only read Sui 2021 as PubMed
abstract `PMID:33957054`; that abstract supports high-level phycobilisome
composition and cyanobacterial/red-algal scope, but not every narrow rod claim
in the new YAML.

The draft also cited Chang 2015 (`DOI:10.1038/cr.2015.59`) for a PCC 7120
canonical example with peripheral-rod wording. Its accessible abstract
supported an intact PCC 7120 phycobilisome/PSII study, not that exact rod
sentence.

- Filed: https://github.com/CultureBotAI/CellStructureMech/issues/1963
- Fixed in: `e22dc58a`
- Fix: moved the rod definition source and rod-specific component, function,
  graph-edge, and discussion evidence to directly readable Kawakami 2022
  support; removed unsupported `cpeA`/`cpeB` gene symbols from the broad rod
  phycobiliprotein component; removed the unsupported PCC 7120 canonical
  example; and tightened the remaining `Thermostichus vulcanus` notes so they
  describe the isolated phycocyanin rod resolved from phycobilisome
  preparations, not a rod solved inside a fully intact phycobilisome.

## Post-Fix Checks

- `uv run python scripts/validate_strict.py --quiet data/structures/energy_complex/phycobilisome_rod.yaml`
- `just validate-history history/records/phycobilisome_rod`
- `just text-embeddings-refresh`
- `just render`
- `just docs-stats`
- `just text-map-check`
- `just render-check`
- `just docs-check`
- `git diff --check`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `just qc`

## Residual Scope

The retained red-algal scope is backed by Kawakami 2022's discussion of red
algal phycoerythrin rods, but the component now keeps only the directly
supported `cpcA`/`cpcB` phycocyanin gene symbols. Red-algal phycoerythrin rod
gene symbols should be added only after a readable source directly verifies
the exact identifiers.
