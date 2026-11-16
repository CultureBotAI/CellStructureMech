"""2026-11-16 PR #1069 repair: native checks with durable logs and test scratch.

Inputs: the prepared CellStructure worktree; named native check. Outputs: unique
timestamped command/stdout/stderr/exit receipts under the worktree's .temp/.
All temporary/cache roots are redirected there. No provider calls or publication.
"""

import argparse
import datetime
import json
import os
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["setup", "focused", "render", "drift", "qc", "lint"])
    parser.add_argument("--worktree", type=Path, required=True)
    args = parser.parse_args()
    root = args.worktree.resolve()
    if shutil.disk_usage(root).free < 50 * 1024**3:
        raise RuntimeError("Less than 50 GiB free; stop before work")
    subprocess.run(["git", "check-ignore", "--quiet", ".temp/graph-canary"], cwd=root, check=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out = root / ".temp" / "graph-canary" / (stamp + "-" + args.stage)
    out.mkdir(parents=True)
    temp = out / "temporary"
    temp.mkdir()
    cache = root / ".temp" / "graph-canary" / "cache"
    cache.mkdir(exist_ok=True)
    env = dict(os.environ)
    env.update(
        TMPDIR=str(temp),
        TMP=str(temp),
        TEMP=str(temp),
        UV_CACHE_DIR=str(cache / "uv"),
        XDG_CACHE_HOME=str(cache),
        PYTHONPYCACHEPREFIX=str(out / "bytecode"),
        PYTEST_ADDOPTS="-ra --basetemp=" + str(out / "pytest"),
        PYTHONDONTWRITEBYTECODE="1",
    )
    commands = {
        "setup": ["uv", "sync", "--extra", "dev"],
        "focused": [
            "uv",
            "run",
            "--extra",
            "dev",
            "python",
            "-m",
            "pytest",
            "-q",
            "tests/test_mechanism_graph.py",
            "tests/test_detail_table_scrolling.py",
            "tests/test_record_review_contract.py::test_every_saved_structured_bundle_is_valid",
        ],
        "render": ["just", "render"],
        "drift": ["just", "render-check"],
        "qc": ["just", "qc"],
        "lint": [
            "uv",
            "run",
            "--extra",
            "dev",
            "python",
            "-m",
            "ruff",
            "check",
            "scripts/mechanism_graph.py",
            "scripts/render_pages.py",
            "tests/test_mechanism_graph.py",
            "scripts/adhoc/steward-graph-pr1069-20261116",
        ],
    }
    command = commands[args.stage]
    with (out / "stdout.log").open("x") as stdout, (out / "stderr.log").open("x") as stderr:
        completed = subprocess.run(command, cwd=root, env=env, stdout=stdout, stderr=stderr, check=False)
    receipt = {
        "started_at": stamp,
        "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "command": command,
        "exit_code": completed.returncode,
        "cwd": str(root),
        "durable_temporary_root": str(temp),
        "receipt_directory": str(out),
    }
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    print((out / "stdout.log").read_text()[-5000:])
    print((out / "stderr.log").read_text()[-2000:])
    raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
