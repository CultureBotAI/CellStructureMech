# Website reference labels and routes

The renderer reads `data/website/references.json` offline. This snapshot contains
UniProt location names from `subcell.txt`, exact TraitMech record URLs extracted
from its published Browse table, GO relationship names and the two reviewed MicrO terms verified in OLS.
It records retrieval date, source URLs, SHA-256 hashes, release information and
UniProt attribution. It does not replace identifiers or associations in the
structure records. Unknown relationship targets retain their external identifier
and are explicitly marked as having no local record.

To refresh, download each URL in `scripts/build_website_references.py`'s `SOURCES`
mapping into a directory using the corresponding filename. Run
`python scripts/build_website_references.py INPUT_DIRECTORY --retrieved YYYY-MM-DD`,
review the resulting snapshot diff, and run `just render` and `just qc`.
The source bodies must be retained with the review evidence. The builder refuses
an incomplete snapshot or a changed identity/obsolete status for the two MicrO
terms. UniProt location names are attributed to the UniProt Consortium under
CC BY 4.0 on the generated record pages.
