#!/usr/bin/env python3
"""Validate repository history records against the vendored claw schema.

One implementation, called by both `just validate-history` and `scripts/run_qc.py`,
so the gate does not depend on the task runner being installed — CI runs qc with
uv alone, and a `just` shell-out failed there with exit 127 (#54).

    python scripts/validate_history.py                 # everything under history/
    python scripts/validate_history.py history/records/x/y.yaml
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "src" / "cellstructuremech" / "schema" / "history.yaml"
STRUCTURES_ROOT = REPO_ROOT / "data" / "structures"
HISTORY_ROOT = REPO_ROOT / "history"
TARGET_CLASS = "HistoryRecord"

# Six early append-only history directories from 2026-08/2026-09 recorded multi-record
# tranches or pre-underscore slugs before the 1:1 per-record convention was adopted.
# Because history/ is append-only by policy, these six legacy slugs are exempted from
# reverse target.path resolution while every structure record and every new history
# directory is strictly checked (#2410).
LEGACY_BATCH_HISTORY_SLUGS = frozenset({
    "divisome-injectisome-discussions",
    "mreb-filament",
    "records-tranche-1",
    "records-tranche-2",
    "records-tranche-3",
    "uniprot-evidence-titles",
})


def resolve_linkml_validate(executable: str | Path | None = None) -> str:
    """Resolve ``linkml-validate`` next to ``sys.executable`` before falling back to ``PATH``.

    ``scripts/run_qc.py`` invokes child scripts via ``sys.executable``. When run
    directly as ``.venv/bin/python scripts/run_qc.py`` without ``.venv/bin`` on
    ``PATH``, a bare ``linkml-validate`` lookup fails with ``FileNotFoundError``
    even though the binary sits sibling to ``sys.executable`` (#2407).
    """
    exe_path = Path(executable if executable is not None else sys.executable)
    sibling = exe_path.with_name("linkml-validate")
    if sibling.is_file():
        return str(sibling)
    return shutil.which("linkml-validate") or "linkml-validate"


def records(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(target.rglob("*.yaml"))
    return [target]


def check_structure_history_coverage(
    structures_root: Path = STRUCTURES_ROOT,
    history_root: Path = HISTORY_ROOT,
) -> list[str]:
    """Enforce 1:1 coverage between ``data/structures/`` and ``history/records/`` (#2410).

    Verifies that:
    - every structure YAML under ``structures_root`` has at least one history record
      under ``history_root / "records" / <slug> / *.yaml`` whose ``target.path``
      resolves to that structure file;
    - every history record under ``history_root / "records"`` carries ``target.kind == "record"``,
      ``target.slug`` matching its parent ``<slug>`` directory, and ``target.path``
      resolving to an existing structure YAML under ``structures_root``; and
    - no empty or orphaned ``history/records/<slug>`` directory exists without a
      matching structure YAML.
    """
    errors: list[str] = []
    repo_base = (
        structures_root.parent.parent
        if structures_root == STRUCTURES_ROOT
        else structures_root.parent
    )

    structure_by_rel: dict[str, Path] = {}
    structure_by_slug: dict[str, Path] = {}
    if structures_root.is_dir():
        for s_path in sorted(structures_root.rglob("*.yaml")):
            try:
                rel = s_path.relative_to(repo_base).as_posix()
            except ValueError:
                rel = s_path.as_posix()
            structure_by_rel[rel] = s_path
            structure_by_slug[s_path.stem] = s_path

    records_dir = history_root / "records"
    covered_rels: set[str] = set()
    covered_slugs: set[str] = set()

    if records_dir.is_dir():
        for slug_dir in sorted(p for p in records_dir.iterdir() if p.is_dir()):
            slug = slug_dir.name
            yaml_files = sorted(slug_dir.glob("*.yaml"))
            if not yaml_files:
                errors.append(
                    f"history/records/{slug}: directory contains no history YAML records"
                )
                continue
            is_legacy = slug in LEGACY_BATCH_HISTORY_SLUGS
            if slug not in structure_by_slug and not is_legacy:
                errors.append(
                    f"history/records/{slug}: orphaned history directory has no matching "
                    f"structure record under data/structures/*/{slug}.yaml"
                )
            for h_path in yaml_files:
                try:
                    instance = yaml.safe_load(h_path.read_text(encoding="utf-8"))
                except (OSError, yaml.YAMLError) as exc:
                    errors.append(f"{h_path}: {type(exc).__name__}: {exc}")
                    continue
                if not isinstance(instance, dict):
                    errors.append(f"{h_path}: history record did not parse as a mapping")
                    continue
                target_block = instance.get("target")
                if not isinstance(target_block, dict):
                    errors.append(f"{h_path}: missing target mapping")
                    continue
                kind = target_block.get("kind")
                if kind != "record":
                    errors.append(
                        f"{h_path}: target.kind under history/records/ must be 'record'; got {kind!r}"
                    )
                t_slug = target_block.get("slug")
                if t_slug and t_slug != slug:
                    errors.append(
                        f"{h_path}: target.slug {t_slug!r} does not match parent directory {slug!r}"
                    )
                t_path = target_block.get("path")
                if not isinstance(t_path, str) or not t_path.strip():
                    errors.append(f"{h_path}: target.path must be a non-empty string")
                    continue
                norm_path = t_path.strip()
                if norm_path not in structure_by_rel:
                    if not is_legacy:
                        errors.append(
                            f"{h_path}: target.path {norm_path!r} does not match any structure record"
                        )
                else:
                    covered_rels.add(norm_path)
                    covered_slugs.add(slug)

    for rel, s_path in sorted(structure_by_rel.items()):
        if rel not in covered_rels:
            errors.append(
                f"{rel}: structure record has no history record under "
                f"history/records/{s_path.stem}/ targeting {rel!r}"
            )

    return errors


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    target = Path(args[0]) if args else HISTORY_ROOT
    if not target.exists():
        print(f"validate-history: {target} does not exist", file=sys.stderr)
        return 2
    paths = records(target)
    if not paths:
        print(f"No history records under {target}.")
        return 0

    # Link check first: it explains a bad URL better than the schema's uri error.
    links = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_history_links.py"), str(target)],
        cwd=REPO_ROOT, check=False,
    )
    if links.returncode:
        return links.returncode

    linkml_validate_bin = resolve_linkml_validate()
    result = subprocess.run(
        [linkml_validate_bin, "--schema", str(SCHEMA), "--target-class", TARGET_CLASS,
         *[str(p) for p in paths]],
        cwd=REPO_ROOT, check=False,
    )
    if result.returncode:
        return result.returncode

    resolved_target = target.resolve()
    if resolved_target in {HISTORY_ROOT.resolve(), (HISTORY_ROOT / "records").resolve()}:
        coverage_errors = check_structure_history_coverage(STRUCTURES_ROOT, HISTORY_ROOT)
        if coverage_errors:
            for err in coverage_errors:
                print(f"validate-history coverage error: {err}", file=sys.stderr)
            print(
                f"ERROR: {len(coverage_errors)} structure-history coverage error(s)",
                file=sys.stderr,
            )
            return 1

    print(f"{len(paths)} history record(s) valid against {SCHEMA.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
