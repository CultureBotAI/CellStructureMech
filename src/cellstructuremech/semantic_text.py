"""Biological text projection shared by the legacy and common map encoders."""

from __future__ import annotations


def clean(value: object) -> str:
    return " ".join(str(value or "").split())


def semantic_text(record: dict) -> str:
    """Project a record to stable biological prose, excluding provenance noise.

    IDs, citations, images, curation history, source-specific complex assertions,
    and imported protein examples are intentionally absent. They describe how a
    record was curated, not what the structure is.
    """
    lines = [
        f"name: {clean(record['label'])}",
        f"definition: {clean(record.get('definition'))}",
        f"category: {clean(record.get('structure_category')).lower()}",
        f"kind: {clean(record.get('structure_kind')).lower()}",
    ]
    synonyms = [clean(item.get("synonym_text")) for item in record.get("synonyms") or []]
    if synonyms:
        lines.append("synonyms: " + "; ".join(synonyms))
    for item in record.get("components") or []:
        parts = [clean(item.get("label")), clean(item.get("role"))]
        lines.append("component: " + ". ".join(part for part in parts if part))
    for item in record.get("functions") or []:
        parts = [clean(item.get("label")), clean(item.get("description"))]
        lines.append("function: " + ". ".join(part for part in parts if part))
    for item in record.get("taxonomic_distribution") or []:
        label = clean(item.get("taxon_label"))
        presence = clean(item.get("presence")).lower()
        lines.append(f"taxonomic scope: {label} ({presence})")
    for item in record.get("physical_properties") or []:
        prop = clean(item.get("property")).lower().replace("_", " ")
        context = clean(item.get("context"))
        lines.append("physical property: " + "; ".join(part for part in (prop, context) if part))
    return "\n".join(line for line in lines if not line.endswith(": ")) + "\n"
