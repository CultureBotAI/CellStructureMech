"""A hosted image must be displayed, with the attribution its licence requires.

The repository hosts CC BY material. Attribution is what that licence is granted
in exchange for, and it is only discharged if a reader of the page can see it.

This was not hypothetical: the template rendered images[0] as a full figure and
every later image as a bare link, so the second image on a record was
downloaded, hashed, committed under data/images/ and never shown -- the file and
the obligation both carried, neither displayed (#169). No record had two images
until the ribosome micrograph, so nothing had exercised the branch.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import pytest

from scripts.corpus import REPO_ROOT, load_records

PAGES = REPO_ROOT / "pages" / "structures"
HOSTED = {"CC0", "PUBLIC_DOMAIN", "CC_BY_3_0", "CC_BY_4_0"}


def _pages():
    for path, record in load_records():
        for index, image in enumerate(record.get("images") or []):
            yield path, index, image


IMAGES = list(_pages())


def _page(path: Path) -> str:
    page = PAGES / path.parent.name / (path.stem + ".html")
    return re.sub(r"\s+", " ", html.unescape(page.read_text(encoding="utf-8")))


@pytest.mark.skipif(not IMAGES, reason="no images in the corpus")
@pytest.mark.parametrize("path,index,image", IMAGES,
                         ids=[f"{p.stem}[{i}]" for p, i, _ in IMAGES])
def test_a_hosted_image_is_displayed_with_its_attribution(path, index, image):
    page = _page(path)
    if image.get("file"):
        assert image["file"] in page, (
            f"{path.name} image {index} is hosted at data/images/{image['file']} but the page "
            f"does not show it -- the file is carried without being displayed")
    if image.get("attribution"):
        assert image["attribution"] in page, (
            f"{path.name} image {index} carries an attribution the page never shows; for "
            f"{image.get('licence')} that is the condition of use, not a nicety")


@pytest.mark.skipif(not IMAGES, reason="no images in the corpus")
@pytest.mark.parametrize("path,index,image", IMAGES,
                         ids=[f"{p.stem}[{i}]" for p, i, _ in IMAGES])
def test_only_redistributable_licences_are_hosted(path, index, image):
    """A file on disk means we are redistributing it; link-only licences must not
    have one. Duplicates the corpus-integrity check deliberately -- this is the
    invariant that would be violated silently if the licence enum changed."""
    if image.get("file"):
        assert image.get("licence") in HOSTED, (
            f"{path.name} image {index} hosts a file under {image.get('licence')}, which is not "
            f"a redistributable licence")
