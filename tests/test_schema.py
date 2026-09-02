"""Schema-level checks: it loads, and the corpus only uses values it declares."""

from __future__ import annotations

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
    assert "StructuralDataset" in view.all_classes()


def test_structural_dataset_extends_shared_dataset_enums(schema_path):
    view = _schema(schema_path)
    dataset = view.induced_class("StructuralDataset")
    assert dataset.attributes["dataset_type"].range == "StructuralDatasetTypeEnum"
    assert dataset.attributes["repository"].range == "StructuralDatasetRepositoryEnum"
    shared_types = set(view.get_enum("DatasetTypeEnum").permissible_values)
    structural_types = set(view.get_enum("StructuralDatasetTypeEnum").permissible_values)
    assert structural_types == shared_types | {
        "STRUCTURAL_IMAGING",
        "EXPERIMENTAL_STRUCTURE",
    }
    shared_repositories = set(view.get_enum("DatasetRepositoryEnum").permissible_values)
    structural_repositories = set(
        view.get_enum("StructuralDatasetRepositoryEnum").permissible_values
    )
    assert structural_repositories == shared_repositories | {
        "CRYOET_DATA_PORTAL",
        "RCSB_PDB",
    }


def test_structure_record_is_the_only_tree_root(schema_path):
    view = _schema(schema_path)
    roots = [name for name, cls in view.all_classes().items() if cls.tree_root]
    assert roots == ["CellStructureRecord"]


def test_vendored_canon_ref_is_an_immutable_claw_commit(repo_root):
    """mech_shared.yaml and history.yaml are vendored from claw at the commit in
    scripts/.vendored_canon_ref, and scripts/check_vendored_sync.sh compares
    the bytes against that commit in CI. This used to be a sha256 of the local
    file compared with itself (#48) — green forever, even after canon moved."""
    ref = (repo_root / "scripts" / ".vendored_canon_ref").read_text().strip()
    assert len(ref) == 40 and all(c in "0123456789abcdef" for c in ref), ref
    for vendored in ("mech_shared.yaml", "history.yaml"):
        assert (repo_root / "src" / "cellstructuremech" / "schema" / vendored).is_file()


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
        for dataset in doc.get("datasets") or []:
            add(dataset.get("accession"))
    missing = used - declared
    assert not missing, f"prefixes used in the corpus but undeclared in the schema: {sorted(missing)}"
