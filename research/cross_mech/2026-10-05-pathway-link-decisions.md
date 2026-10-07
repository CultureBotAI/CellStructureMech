# Structure–pathway link decisions

The reviewed PathwayMech revision is `d8ec2b69f7a4c615aecddff80498fef1e1fab0ce`.
The three target record paths, exact labels, taxa and byte digests are preserved
in `conf/pathwaymech_targets.json`; source record content is CC BY 4.0 with
PathwayMech and upstream provenance available at those immutable paths.

| Structure lead | Decision and limit |
| --- | --- |
| Divisome | Link to WP5060 for the E. coli septal-synthesis segment. Add reviewed K-12 FtsW/P0ABG4 and FtsI/P0AD68 examples to the existing septal-synthase component using independent localization evidence. |
| Elongasome | Link to WP5060 for the E. coli sidewall-synthesis segment. This is a functional correspondence, not an exact PBP2 accession join: WP5060's Q2TL65 is not the curated K-12 P0AD65 entry. |
| Peptidoglycan cell wall | Link as material produced by WP5060 for the existing E. coli exemplar. The wall is not the whole pathway. |
| Peroxisome | Link as a site of the beta-oxidation segment in the budding-yeast model. Do not assign every activation or auxiliary reaction to the organelle. |
| Peroxisomal matrix | Same bounded beta-oxidation relation, with the target's narrower S288C strain scope made explicit. |
| Chitosome | Link as delivery support for CHS3 in yeast chitin biosynthesis. Synthesis at the plasma membrane is not synthesis inside the vesicle. |
| Glycine cleavage complex | Deferred: the curated organism/example evidence is E. coli K-12, whereas the current pathway is yeast. Adding yeast taxa or examples is a separate curation decision. |
| Succinate dehydrogenase complex II | Deferred: the structural exemplar is E. coli; the candidate TCA model is yeast. No organism transfer from enzyme name alone. |
| Cytoophidium | Rejected as a catalytic-pathway link for the current record: its Caulobacter morphology function is explicitly independent of CTP synthase catalytic activity. |
| Lipid droplet | Deferred: the current structure claim is neutral-lipid storage. A biosynthetic role does not follow from storage, and a separate product-storage relation would need an explicit product join. |

UniProtKB entries P0ABG4 and P0AD68 were read anonymously on 2026-10-05.
Both are reviewed entries with organism NCBITaxon:83333. The exact recommended
name of P0ABG4 retains UniProt's "Probable" qualifier. Their septal membership
comes from [Wang et al. 1998](https://pubmed.ncbi.nlm.nih.gov/9603865/) and
[Mercer and Weiss 2002](https://pubmed.ncbi.nlm.nih.gov/11807049/), whose
abstracts were read through Europe PMC. Pathway membership does not supply this
evidence. Neither example changes the structure's taxonomic scope.

The link review also read the abstracts already cited by the relevant curated
functions: [Typas et al.](https://doi.org/10.1038/nrmicro2677),
[Vollmer et al.](https://doi.org/10.1111/j.1574-6976.2007.00094.x),
[Sibirny](https://doi.org/10.1093/femsyr/fow038), and the primary
[Ziman et al. trafficking study](https://doi.org/10.1091/mbc.9.6.1565).
No new verbatim snippet is asserted. Review abstracts support the bounded
existing functions; they are not represented as new primary strain experiments.
