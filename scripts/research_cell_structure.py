#!/usr/bin/env python3
"""Research one cell-structure record with native Codex or deep-research-client."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from deep_research_contract import ContractError, render_prompt_template, run_codex_research

REPO_ROOT = Path(__file__).resolve().parent.parent
STRUCTURES_DIR = REPO_ROOT / "data" / "structures"
RESEARCH_DIR = REPO_ROOT / "research"
TEMPLATE = REPO_ROOT / "templates" / "cell_structure_mechanism_research.md"
DEFAULT_CLIENT_COMMAND = (
    "uvx --python 3.12 --prerelease=allow "
    "--from deep-research-client[cyberian] deep-research-client"
)
PROVIDER_ALIASES = {"edison": "falcon", "futurehouse": "falcon", "claude-code": "claude_code"}


def canonical_provider(provider: str) -> str:
    key = provider.strip().casefold().replace("-", "_").replace(" ", "_")
    return PROVIDER_ALIASES.get(key, key)


def load_record(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Cell-structure file is not a YAML mapping: {path}")
    return data


def resolve_record(target: str) -> Path:
    candidate = Path(target)
    for path in (candidate, REPO_ROOT / candidate):
        if path.is_file():
            resolved = path.resolve()
            if resolved.is_relative_to(STRUCTURES_DIR.resolve()):
                return resolved
            raise ValueError(f"target must be beneath {STRUCTURES_DIR}: {resolved}")

    files = sorted(STRUCTURES_DIR.rglob("*.yaml"))
    stem_matches = [path for path in files if path.stem.casefold() == target.casefold()]
    if len(stem_matches) == 1:
        return stem_matches[0]
    field_matches = []
    for path in files:
        record = load_record(path)
        if any(
            str(record.get(field, "")).casefold() == target.casefold()
            for field in ("identifier", "label")
        ):
            field_matches.append(path)
    matches = stem_matches or field_matches
    if len(matches) == 1:
        return matches[0]
    if matches:
        choices = ", ".join(str(path.relative_to(REPO_ROOT)) for path in matches)
        raise ValueError(f"ambiguous cell-structure target {target!r}: {choices}")
    raise FileNotFoundError(f"cell-structure target not found: {target}")


def template_vars(record: dict[str, Any], path: Path) -> dict[str, str]:
    return {
        "record_path": str(path.relative_to(REPO_ROOT)),
        "structure_identifier": str(record.get("identifier", "")),
        "structure_label": str(record.get("label", path.stem)),
        "structure_category": str(record.get("structure_category", "")),
        "curation_status": str(record.get("curation_status", "")),
        "record_yaml": yaml.safe_dump(record, sort_keys=False, allow_unicode=True).strip(),
    }


def provider_args(provider: str) -> list[str]:
    return ["--use-cborg"] if provider == "cborg" else ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    env = os.environ.copy()
    if not env.get("EDISON_API_KEY") and env.get("EDISON_PLATFORM_API_KEY"):
        env["EDISON_API_KEY"] = env["EDISON_PLATFORM_API_KEY"]
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


def output_path(record: dict[str, Any], path: Path, provider: str, research_dir: Path) -> Path:
    relative = path.relative_to(STRUCTURES_DIR)
    return research_dir / "structures" / relative.parent / f"{relative.stem}-deep-research-{provider}.md"


def build_client_command(
    *,
    provider: str,
    template: Path,
    output: Path,
    variables: dict[str, str],
    passthrough: list[str],
    client_command: str,
) -> list[str]:
    command = [*shlex.split(client_command), "research", "--template", str(template)]
    for key, value in variables.items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(provider_args(provider))
    command.extend(["--output", str(output.resolve())])
    command.extend(passthrough)
    return command


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", required=True)
    parser.add_argument("--target", required=True, help="path, unique slug, identifier, or label")
    parser.add_argument("--template", type=Path, default=TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=RESEARCH_DIR)
    parser.add_argument(
        "--client-command",
        default=os.environ.get("DEEP_RESEARCH_CLIENT", DEFAULT_CLIENT_COMMAND),
    )
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--min-chars", type=int, default=1000)
    parser.add_argument("--min-sources", type=int, default=3)
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=True)
    parser.add_argument("--apply", dest="dry_run", action="store_false")
    args, passthrough = parser.parse_known_args(argv)
    args.passthrough = passthrough
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    provider = canonical_provider(args.provider)
    path = resolve_record(args.target)
    record = load_record(path)
    variables = template_vars(record, path)
    output = output_path(record, path, provider, args.research_dir)
    print(f"Researching: {variables['structure_label']} ({provider}) -> {output}")

    if provider == "codex":
        if args.passthrough:
            print("Codex does not accept client passthrough arguments", file=sys.stderr)
            return 2
        try:
            prompt = render_prompt_template(args.template, variables)
            if args.dry_run:
                print("codex --search --ask-for-approval never exec [schema validated]")
                print(f"prompt: {len(prompt)} characters")
                return 0
            summary = run_codex_research(
                prompt,
                output,
                repo_root=REPO_ROOT,
                timeout=args.timeout,
                min_chars=args.min_chars,
                min_sources=args.min_sources,
            )
        except ContractError as exc:
            print(f"Codex research rejected: {exc}", file=sys.stderr)
            return 1
        print(f"Validated {summary.characters} characters and {summary.sources} sources")
        return 0

    command = build_client_command(
        provider=provider,
        template=args.template,
        output=output,
        variables=variables,
        passthrough=args.passthrough,
        client_command=args.client_command,
    )
    if args.dry_run:
        print(shlex.join(command))
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True, cwd=REPO_ROOT, env=research_env(provider))
    if not output.is_file() or len(output.read_text(encoding="utf-8").strip()) < args.min_chars:
        raise SystemExit(f"provider returned success without a substantive report at {output}")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
