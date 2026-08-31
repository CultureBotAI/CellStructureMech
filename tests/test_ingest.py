"""Source-neutral ingestion safety contracts."""

from __future__ import annotations

from pathlib import Path

import pytest

from cellstructuremech.ingest import image_destination, write_image_with_validated_record
from cellstructuremech.validation.write_validated import ValidationFailedError


@pytest.mark.parametrize(
    "filename",
    ["../escape.png", "nested/escape.png", "nested\\escape.png", "/tmp/escape.png", "UPPER.PNG"],
)
def test_image_destination_requires_a_safe_lowercase_leaf(tmp_path, filename):
    record_path = Path("data/structures/envelope/test.yaml")
    with pytest.raises(ValueError, match="safe lowercase leaf"):
        image_destination(record_path, filename, tmp_path)


def test_invalid_record_is_rejected_before_image_bytes_are_written(tmp_path):
    record_path = tmp_path / "records" / "envelope" / "test.yaml"
    destination = tmp_path / "data" / "images" / "envelope" / "test" / "test.png"
    with pytest.raises(ValidationFailedError):
        write_image_with_validated_record(
            {"identifier": "GO:1"}, record_path, "test.png", b"image bytes", tmp_path
        )
    assert not destination.exists()
