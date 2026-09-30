# YAML record review: septin_complex

- PR: #1819
- Record: `data/structures/cytoskeleton/septin_complex.yaml`
- Reviewed: 2026-09-30T10:22:18Z

## Findings

### 1. The fission-yeast rows should state the oligomeric Spn1-4 complex evidence

Severity: medium

Location: `data/structures/cytoskeleton/septin_complex.yaml:46`

The `taxonomic_distribution` and `canonical_examples` rows cite the right primary
paper, but their notes stay at the level of septins assembling into complexes
or being tested for "complex formation, localization, and function." An et al.
2004 specifically report a *Schizosaccharomyces pombe* Spn1-4 complex with two
copies of each septin and a defined chain order. The row text should use that
structure-level observation rather than a looser septation context so the
species distribution and canonical example directly support `GO:0031105`.

Recommendation: update both *S. pombe* notes to mention the Spn1/Spn2/Spn3/Spn4
oligomeric septin complex from An et al. 2004, without broadening to a universal
stoichiometry for all septin complexes.

## Non-findings

- The existing-record check used `rg --no-ignore --hidden` over
  `data/structures`; it found `GO:0031105` only as boundary evidence on the
  broader septin-ring record, not as a top-level identifier, label, or synonym.
- `GO:0032991` is the direct current OLS parent for `GO:0031105`, while the
  current OLS `part_of` targets include `GO:0032156` septin cytoskeleton and
  `GO:0005938` cell cortex.
- The `septin_proteins` component correctly remains `REVIEWED_LABEL_ONLY`; the
  record does not guess InterPro, Pfam, NCBIfam, UniProtKB, ComplexPortal,
  ChEBI, SO, or NCBITaxon groundings.
- The generated browse, category, grounded, index, structure page, and embedding
  artifacts include `GO:0031105` and match the curated YAML.
