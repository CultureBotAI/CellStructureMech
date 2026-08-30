"""Schema-level checks: it loads, and the corpus only uses values it declares."""

from __future__ import annotations

import hashlib

import yaml
from linkml_runtime.utils.schemaview import SchemaView


def _schema(schema_path):
    return SchemaView(str(schema_path))


def test_schema_loads_with_its_imports(schema_path):
    view = _schema(schema_path)
    assert "CellStructureRecord" in view.all_classes()
    # The vendored mech_shared module must resolve, or Discussion/Dataset
    # silently disappear from the record shape.
    assert "Discussion" in view.all_classes()
    assert "Dataset" in view.all_classes()


def test_structure_record_is_the_only_tree_root(schema_path):
    view = _schema(schema_path)
    roots = [name for name, cls in view.all_classes().items() if cls.tree_root]
    assert roots == ["CellStructureRecord"]


def test_mech_shared_is_vendored_byte_identical(repo_root):
    """The shared module is vendored across the Mech repos and must not be
    edited in one place. Pin the sha of the copy we shipped."""
    path = repo_root / "src" / "cellstructuremech" / "schema" / "mech_shared.yaml"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = "1a5e21eb2ee9f3584ff6af3a6906b1d442e18c41de405b1bf907c20f44eafa2a"
    assert digest == expected, (
        "mech_shared.yaml has been edited locally. It is vendored byte-identical "
        "across the Mech repos — change it once upstream and re-vendor everywhere, "
        "then update this pin."
    )


def _permissible(view, enum_name: str) -> set[str]:
    return set(view.get_enum(enum_name).permissible_values)


def test_corpus_uses_only_declared_enum_values(schema_path, records):
    view = _schema(schema_path)
    checks = [
        ("structure_category", "StructureCategoryEnum", lambda d: [d.get("structure_category")]),
        ("structure_kind", "StructureKindEnum", lambda d: [d.get("structure_kind")]),
        ("mapping_status", "MappingStatusEnum", lambda d: [d.get("mapping_status")]),
        ("component_type", "ComponentTypeEnum",
         lambda d: [c.get("component_type") for c in d.get("components") or []]),
        ("presence", "PresenceEnum",
         lambda d: [t.get("presence") for t in d.get("taxonomic_distribution") or []]),
        ("relation", "TraitRelationEnum",
         lambda d: [t.get("relation") for t in d.get("associated_traits") or []]),
        ("node_type", "CausalNodeTypeEnum",
         lambda d: [n.get("node_type") for g in d.get("causal_graphs") or [] for n in g.get("nodes") or []]),
    ]
    for field, enum_name, extract in checks:
        allowed = _permissible(view, enum_name)
        bad = set()
        for _, doc in records:
            for value in extract(doc):
                if value is not None and value not in allowed:
                    bad.add(value)
        assert not bad, f"{field}: values not in {enum_name}: {sorted(bad)}"


def test_category_directories_match_the_enum(repo_root, schema_path):
    """The filesystem layout is derived from StructureCategoryEnum."""
    view = _schema(schema_path)
    allowed = {v.lower() for v in _permissible(view, "StructureCategoryEnum")}
    structures = repo_root / "data" / "structures"
    if not structures.exists():
        return
    unexpected = {d.name for d in structures.iterdir() if d.is_dir()} - allowed
    assert not unexpected, f"category directories not in the enum: {sorted(unexpected)}"


def test_schema_prefixes_cover_every_curie_in_the_corpus(schema_path, records):
    """A CURIE whose prefix the schema does not declare cannot be expanded to a
    URI, so it is not resolvable by any downstream consumer."""
    declared = set(yaml.safe_load(schema_path.read_text(encoding="utf-8"))["prefixes"])
    used = set()

    def add(curie):
        if isinstance(curie, str) and ":" in curie and not curie.startswith(("http://", "https://")):
            used.add(curie.split(":", 1)[0])

    for _, doc in records:
        add(doc["identifier"])
        for key in ("parent_structures", "part_of", "has_part", "xrefs", "replaces"):
            for c in doc.get(key) or []:
                add(c)
        for c in doc.get("components") or []:
            add(c.get("grounding"))
        for f in doc.get("functions") or []:
            add(f.get("grounding"))
        for t in doc.get("associated_traits") or []:
            add(t.get("trait_id"))
        for g in doc.get("causal_graphs") or []:
            for n in g.get("nodes") or []:
                add(n.get("grounding"))
            for e in g.get("edges") or []:
                add(e.get("predicate_id"))
    missing = used - declared
    assert not missing, f"prefixes used in the corpus but undeclared in the schema: {sorted(missing)}"
