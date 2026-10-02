# Contractile Vacuole Pore YAML Record Review

- **PR:** #1918
- **Branch:** `add-contractile-vacuole-pore`
- **Reviewed head:** `2bd5729652c87ce5293beeef12cf0c3de0170236`
- **Record:** `data/structures/membrane_organelle/contractile_vacuole_pore.yaml`
- **Identifier:** `GO:0031913`
- **Reviewed at:** `2026-10-02T15:31:01Z`

## Scope

Reviewed the PR diff that adds the `GO:0031913` contractile vacuole pore
record, generated structure page, generated embedding and page indexes, README
statistics, and append-only history records for `contractile_vacuole_pore`.

## Duplicate Search

Re-ran a hidden/ignored-inclusive search for:

- `GO:0031913`
- `contractile vacuole pore`
- `contractile-vacuole pore`
- `contractile vacuole pores`
- `CVP`
- `10503189`
- `4357833`
- `10.1111/j.1550-7408.1973.tb03587.x`
- `10.1016/S0091-679X(08)61528-9`

Expected matches after this PR were limited to:

- the new record, rendered page, generated text-projection JSON, and generated
  CURIE cache/report rows;
- the new append-only history records;
- existing `contractile_vacuole.yaml`, whose GO definition mentions
  contractile vacuole pores;
- pre-existing `oral_apparatus` and `deep_fiber` evidence that cites Frankel
  2000 for different GO definitions;
- the prior deep-fiber review report that had searched `10503189`.

No pre-existing standalone `GO:0031913` record or conflicting exact
contractile-vacuole-pore record was present. This duplicate sweep included
ignored and hidden files.

## Evidence And Boundary Checks

- `GO:0031913` exactly denotes `contractile vacuole pore`; OLS and QuickGO both
  report it as a live cellular-component term with the GO definition used in
  the YAML.
- The GO graph reports `GO:0031913` as a subclass of `GO:0098797` plasma
  membrane protein complex and as part of both `GO:0031164` contractile
  vacuolar membrane and `GO:0005856` cytoskeleton.
- `structure_category: MEMBRANE_ORGANELLE` keeps the record in the
  contractile-vacuole file neighborhood; `structure_kind:
  MULTIPROTEIN_COMPLEX` follows the GO plasma-membrane-protein-complex parent.
- The record keeps McKanna 1973 as primary structural evidence for the
  Paramecium pore without asserting an exact Paramecium species.
- No molecular `components` were added; the open TODO records that exact
  InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal groundings were not
  verified.
- The topology graph stays nonmechanistic and only asserts GO-backed
  parthood plus GO-defined liquid-flow regulation.

## Validation Reviewed

Confirmed local green gates before the initial PR commit:

- focused LinkML validation for `contractile_vacuole_pore.yaml`
- focused strict validation for `contractile_vacuole_pore.yaml`
- embedding, rendered-page, and README drift checks
- focused history validation for `history/records/contractile_vacuole_pore`
- full strict validation
- full history validation
- snippet verification
- TraitMech link validation
- CURIE liveness validation
- id/label correspondence validation
- `git diff --check`
- `scripts/run_qc.py`

Confirmed the same focused, generated-artifact, external, full strict/history,
whitespace, and full-QC gates after the review fixes.

## Findings And Fixes

### #1919: Tighten contractile-vacuolar-membrane evidence wording

The initial `GO:0031164` record-level evidence note said that the contractile
vacuolar membrane contains the pore. That parthood is carried by the
`GO:0031913` term, not by the `GO:0031164` definition itself.

Fixed in `2bd57296` by narrowing the `GO:0031164` evidence note to identify
only the contractile vacuolar membrane term.

### #1920: Remove genus-level Paramecium canonical example

The initial `canonical_examples` list included `NCBITaxon:5884` Paramecium.
`canonical_examples` should identify reference organisms, not a genus inferred
from McKanna 1973's title.

Fixed in `2bd57296` by removing the genus-level canonical example while
retaining McKanna 1973 as function and record-level structural evidence.
