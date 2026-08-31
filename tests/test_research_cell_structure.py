from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import research_cell_structure as research  # noqa: E402


def test_resolve_record_by_slug_and_identifier():
    by_slug = research.resolve_record("carboxysome")
    by_id = research.resolve_record("GO:0031470")
    assert by_slug == by_id
    assert by_slug.name == "carboxysome.yaml"


def test_openscientist_command_uses_real_client_provider():
    path = research.resolve_record("carboxysome")
    record = research.load_record(path)
    variables = research.template_vars(record, path)
    command = research.build_client_command(
        provider="openscientist",
        template=research.TEMPLATE,
        output=Path("research/out.md"),
        variables=variables,
        passthrough=[],
        client_command="deep-research-client",
    )
    assert command[:2] == ["deep-research-client", "research"]
    assert command[command.index("--provider") + 1] == "openscientist"
    assert "--output" in command


def test_codex_dry_run_uses_native_contract(capsys):
    assert research.main(["--provider", "codex", "--target", "carboxysome"]) == 0
    output = capsys.readouterr().out
    assert "codex --search --ask-for-approval never exec" in output
    assert "schema validated" in output
