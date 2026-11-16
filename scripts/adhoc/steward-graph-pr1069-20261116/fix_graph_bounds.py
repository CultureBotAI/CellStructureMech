"""2026-11-16 #3075: bounded viewport fix in the isolated PR1069 repair.
Input: exact pre-fix graph module. Output: content-derived viewport; no data edits.
The original module is retained in the owned .temp receipt directory.
"""

import argparse
import hashlib
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worktree", type=Path, required=True)
    args = parser.parse_args()
    root = args.worktree.resolve()
    path = root / "scripts/mechanism_graph.py"
    old = path.read_text()
    assert (
        hashlib.sha256(old.encode()).hexdigest()
        == "20684d7982b8e44ca2a64c8c697fde3cac192325b235a4109f60632314846592"
    )
    (root / ".temp/graph-canary/pre-3075-mechanism_graph.py").write_text(old)
    start = old.index("    width = max(x for x, _ in positions.values())")
    end = old.index("    parallel: dict[tuple[str, str], int]", start)
    block = old[start:end]
    header = block[block.index("    out = [") :].replace("    out = [", "    header = [", 1)
    header = header.replace('viewBox="0 0 {width} {height}"', 'viewBox="{left} {top} {width} {height}"')
    replacement = """    # Cubic curves stay within the convex hull of their control points. Keep
    # those points and conservative text ink bounds, then derive the viewport
    # after routing every edge (#3075), including negative/top and right lanes.
    points: list[tuple[float, float]] = []

    def text_bounds(text: str, x: float, y: float, size: int = 13, *, centered: bool = False) -> None:
        # One em per code point conservatively bounds the displayed system-font
        # labels; extra vertical room covers ascenders, descenders and strokes.
        extent = len(text) * size
        start_x = x - extent / 2 if centered else x
        points.extend([(start_x, y - size * 1.4), (start_x + extent, y + size * 0.5)])

    out = []
"""
    text = old[:start] + replacement + old[end:]
    replacements = {
        "            bend = (sx + tx) / 2\n": (
            "            bend = (sx + tx) / 2\n"
            "            control = (bend, sy - offset, bend, ty - offset, tx, ty)\n"
        ),
        "            lane = sx + 65 + offset\n": (
            "            lane = sx + 65 + offset\n            control = (lane, sy, lane, ty, tx, ty)\n"
        ),
        "            sx, sy = x1 + box_w - 30, y1\n": (
            "            sx, sy = x1 + box_w - 30, y1\n"
            "            control = (sx + 100, sy - 60 - offset, sx - 80, sy - 60 - offset, sx - 50, sy)\n"
        ),
        "            lane = max(sy, ty) + 40 + index * 10 + offset\n": (
            "            lane = max(sy, ty) + 40 + index * 10 + offset\n"
            "            control = (sx, lane, tx, lane, tx, ty)\n"
        ),
        '        predicate = str(edge.get("predicate") or "related to")\n': (
            "        points.extend([(sx, sy), *zip(control[::2], control[1::2], strict=True)])\n"
            '        predicate = str(edge.get("predicate") or "related to")\n'
            "        text_bounds(predicate, lx, ly, centered=True)\n"
        ),
        '        node_type = str(node.get("node_type") or "NODE")\n': (
            "        points.extend([(x, y), (x + box_w, y + box_h)])\n"
            '        node_type = str(node.get("node_type") or "NODE")\n'
            "        text_bounds(node_type, x + 12, y + 19, size=10)\n"
        ),
        "        for i, line in enumerate(lines[key]):\n": (
            "        for i, line in enumerate(lines[key]):\n"
            "            text_bounds(line, x + 12, y + 39 + i * 17)\n"
        ),
    }
    for needle, value in replacements.items():
        assert text.count(needle) == 1, needle
        text = text.replace(needle, value)
    tail = """    out.append("</svg></div></figure>")
    return Markup("\\n".join(out))
"""
    assert text.count(tail) == 1
    bounds = """    left = min(x for x, _ in points) - 20
    top = min(y for _, y in points) - 20
    width = max(x for x, _ in points) + 20 - left
    height = max(y for _, y in points) + 20 - top
"""
    text = text.replace(
        tail, bounds + header + '    return Markup("\\n".join([*header, *out, "</svg></div></figure>"]))\n'
    )
    path.write_text(text)
    print("Updated graph viewport from emitted geometry and text bounds.")


if __name__ == "__main__":
    main()
