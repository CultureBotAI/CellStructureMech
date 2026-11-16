"""2026-11-16 PR #1069: prove the current Golgi integration catches missing SVGs.

Input: owned worktree with graph hook. Output: failed mutation-test log and exact
restore receipt in .temp/graph-canary/. Run from Claw's environment for its lock.
"""

import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from plugins.lock_manager import LockManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worktree", type=Path, required=True)
    root = parser.parse_args().worktree.resolve()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out = root / ".temp/graph-canary" / (stamp + "-golgi-mutation")
    out.mkdir()
    path = root / "src/cellstructuremech/templates/structure.html"
    original = path.read_bytes()
    needle = b"{{ g | graph_svg(loop.index) }}"
    assert original.count(needle) == 1
    mutant = original.replace(needle, b"")
    env = dict(os.environ)
    temp = out / "temporary"
    temp.mkdir()
    env.update(
        TMPDIR=str(temp),
        TMP=str(temp),
        TEMP=str(temp),
        UV_CACHE_DIR=str(root / ".temp/graph-canary/cache/uv"),
        PYTHONPYCACHEPREFIX=str(out / "bytecode"),
        PYTEST_ADDOPTS="-ra --basetemp=" + str(out / "pytest"),
    )
    command = [
        "uv",
        "run",
        "python",
        "-m",
        "pytest",
        "-q",
        "tests/test_mechanism_graph.py::test_newer_golgi_record_renders_diagram_alongside_evidence",
    ]
    try:
        with LockManager().lock("cellstructuremech", "steward_golgi_mutation"):
            assert path.read_bytes() == original
            path.write_bytes(mutant)
        result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
        (out / "stdout.log").write_text(result.stdout)
        (out / "stderr.log").write_text(result.stderr)
    finally:
        with LockManager().lock("cellstructuremech", "steward_golgi_restore"):
            assert path.read_bytes() == mutant
            path.write_bytes(original)
    restored = path.read_bytes() == original
    receipt = {
        "command": command,
        "mutation": "remove only graph template hook",
        "exit_code": result.returncode,
        "restored": restored,
        "template_sha256": hashlib.sha256(original).hexdigest(),
    }
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(out)
    print(result.stdout[-1800:])
    assert restored and result.returncode == 1
    assert "assert 0 == 1" in result.stdout


if __name__ == "__main__":
    main()
