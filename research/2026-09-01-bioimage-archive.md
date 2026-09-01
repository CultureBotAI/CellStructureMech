# BioImage Archive live reassessment

Checked 2026-09-01 because the queue's 2026-08-29 row still described the
source as unverified. The official BioStudies search and study APIs now expose
enough metadata for a fail-closed importer.

## Decision

Adopt direct `S-BIAD` submissions only. Each accepted study must:

- be attached to the `BioImages` collection and use a `BioImages.v*` template;
- carry the matching `10.6019/S-BIADNNNN` DOI pattern;
- state exactly CC0 or CC BY 4.0 with a matching Creative Commons URL;
- name an organism in a Biosample; and
- declare the selected file in a Study Component's JSON manifest.

Brokered/legacy accessions and studies without exact hostable terms remain
refused. A collection-wide licence assumption is not made.

## Canary selection

`S-BIAD2294`, *Bactericidal Membrane Attack Complex formation initiates at the
new pole of E. coli*, is CC0. Its Figure 3 specimen says that *E. coli* MG1655
peptidoglycan was labelled with HADA. `Figure 3.json` lists each TIFF as three
named channels: phase contrast, C9-AF647, and HADA (CFP). The selected file is:

`Figure 3/Replicate 1 (MW240530) 8 minutes/Series002_1.tif`

The manifest reports 4,382,973 bytes. The live file has exactly that size and
three TIFF planes; plane 3 is the HADA signal. Lossless PNG export is 484,180
bytes, below the repository's 2 MiB hosted-image cap.

Two alternatives were rejected as canaries:

- `S-BIAD1375` studies a flagellum-dependent phenotype, but its fluorescence
  files do not image the flagellum itself.
- `S-BIAD3905` labels its SEM experiment as a cell-wall study, but the candidate
  image shows whole-cell surface morphology and does not resolve the thin
  Gram-negative peptidoglycan layer.

## Official endpoints exercised

- `https://www.ebi.ac.uk/biostudies/api/v1/collections/BioImages`
- `https://www.ebi.ac.uk/biostudies/api/v1/studies/S-BIAD2294`
- `https://www.ebi.ac.uk/biostudies/files/S-BIAD2294/Figure%203.json`
- the exact file URL derived from the manifest path
