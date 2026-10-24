"""Semantic validation checks for CellStructureRecord documents (#2408, #2410, #2417).

Complements closed-schema LinkML validation (``write_validated.py``) with
cross-field and graph-completeness invariants that JSON Schema alone cannot
express:

- Every ``CausalEdge.subject`` and ``CausalEdge.object`` references a declared
  ``CausalNode.node_id`` in the same graph.
- Every ``CausalNode.component_ref`` resolves to a declared ``component_id`` on
  the record.
- Every declared ``CausalNode`` participates in at least one incident
  ``CausalEdge`` (no isolated nodes).
- Every ``CausalEdge`` carries a non-blank ``description``.
- No ``CausalNode`` with ``node_type == 'GENE_OR_PROTEIN'`` carries a ``GO:``
  or ``cellstructuremech:`` structure/complex ``grounding`` or references a
  ``PROTEIN_COMPLEX`` component grounded to ``GO:`` or ``cellstructuremech:``
  (such multiprotein complexes/substructures must use ``node_type: STRUCTURE``).
- Every ``components[].protein_examples[].gene_symbol`` is included in a
  non-empty parent ``components[].gene_symbols`` list or explicitly disclosed
  as an organism-specific synonym/locus tag in ``protein_examples[].role``.
- Every ``#NNN`` GitHub issue mention in ``discussions`` prose (``prompt``,
  ``rationale``, ``resolution_note``) is backed by a full GitHub issue URL in
  that discussion's ``evidence`` list, and every ``attaches_to`` anchor
  resolves to a local ID on the record.
"""

from __future__ import annotations

import re
from typing import Any

DEFAULT_GITHUB_REPO = "CultureBotAI/CellStructureMech"
_PROSE_ISSUE_RE = re.compile(r"(?<![A-Za-z0-9_/])#([1-9]\d*)\b")
_STRUCTURE_GROUNDING_PREFIXES = ("GO:", "cellstructuremech:")
_SYNONYM_ROLE_RE = re.compile(
    r"\bgene ([^\s,()]+), which UniProt lists (?:under the primary name\b|without a gene symbol\b)"
)
_ALSO_SYNONYM_RE = re.compile(r"\(also declared as (?:synonym|locus tag)[s]? ([^)]+)\)")


def validate_causal_graphs(doc: dict[str, Any]) -> list[str]:
    """Return semantic validation error strings for ``doc['causal_graphs']``."""
    errors: list[str] = []
    comps_by_id = {
        c.get("component_id"): c
        for c in (doc.get("components") or [])
        if isinstance(c, dict) and c.get("component_id")
    }
    comp_ids = set(comps_by_id)
    for graph in doc.get("causal_graphs") or []:
        if not isinstance(graph, dict):
            continue
        gid = graph.get("graph_id") or "<graph>"
        nodes = [n for n in (graph.get("nodes") or []) if isinstance(n, dict)]
        edges = [e for e in (graph.get("edges") or []) if isinstance(e, dict)]
        node_ids = {n.get("node_id") for n in nodes if n.get("node_id")}

        incident: set[str] = set()
        for idx, edge in enumerate(edges):
            subj = edge.get("subject")
            obj = edge.get("object")
            if subj not in node_ids:
                errors.append(
                    f"{gid}: edge[{idx}] subject {subj!r} is not a declared node_id"
                )
            else:
                incident.add(subj)
            if obj not in node_ids:
                errors.append(
                    f"{gid}: edge[{idx}] object {obj!r} is not a declared node_id"
                )
            else:
                incident.add(obj)
            desc = edge.get("description")
            if not isinstance(desc, str) or not desc.strip():
                errors.append(
                    f"{gid}: edge[{idx}] ({subj} -> {obj}) lacks a non-empty description"
                )

        for node in nodes:
            nid = node.get("node_id")
            cref = node.get("component_ref")
            if cref and cref not in comp_ids:
                errors.append(
                    f"{gid}: node {nid!r} component_ref {cref!r} does not resolve to a component"
                )
            if nid and nid not in incident:
                errors.append(
                    f"{gid}: isolated CausalNode {nid!r} has zero incident edges"
                )
            if node.get("node_type") == "GENE_OR_PROTEIN":
                grounding = str(node.get("grounding") or "").strip()
                ref_comp = comps_by_id.get(cref) if cref else None
                comp_grounding = str((ref_comp or {}).get("grounding") or "").strip()
                if grounding.startswith(_STRUCTURE_GROUNDING_PREFIXES):
                    errors.append(
                        f"{gid}: node {nid!r} has node_type 'GENE_OR_PROTEIN' with "
                        f"structure/complex grounding {grounding!r} (expected 'STRUCTURE')"
                    )
                elif (
                    ref_comp
                    and ref_comp.get("component_type") == "PROTEIN_COMPLEX"
                    and comp_grounding.startswith(_STRUCTURE_GROUNDING_PREFIXES)
                ):
                    errors.append(
                        f"{gid}: node {nid!r} has node_type 'GENE_OR_PROTEIN' referencing "
                        f"grounded PROTEIN_COMPLEX component {cref!r} ({comp_grounding!r}; "
                        f"expected 'STRUCTURE')"
                    )
    return errors


def validate_component_protein_examples(doc: dict[str, Any]) -> list[str]:
    """Return error strings when ``protein_examples[].gene_symbol`` drifts from ``component.gene_symbols``."""
    errors: list[str] = []
    for comp in doc.get("components") or []:
        if not isinstance(comp, dict):
            continue
        cid = comp.get("component_id") or "<component>"
        gs = [
            str(s).strip()
            for s in (comp.get("gene_symbols") or [])
            if s is not None and str(s).strip()
        ]
        if not gs:
            continue
        gs_lower = {s.lower() for s in gs}
        for pe in comp.get("protein_examples") or []:
            if not isinstance(pe, dict):
                continue
            pe_sym = str(pe.get("gene_symbol") or "").strip()
            if not pe_sym or pe_sym.lower() in gs_lower:
                continue
            role = str(pe.get("role") or "")
            disclosed: set[str] = set()
            m1 = _SYNONYM_ROLE_RE.search(role)
            if m1:
                disclosed.add(m1.group(1).lower())
            m2 = _ALSO_SYNONYM_RE.search(role)
            if m2:
                for tok in re.split(r"[,;\s]+", m2.group(1)):
                    if tok and tok.lower() != "and":
                        disclosed.add(tok.lower())
            if pe_sym.lower() in role.lower() or (disclosed & gs_lower):
                continue
            errors.append(
                f"components#{cid}: protein_example {pe.get('uniprot_id')!r} "
                f"gene_symbol {pe_sym!r} is not in component.gene_symbols {gs!r} "
                f"or disclosed as a synonym in role"
            )
    return errors


def validate_discussion_issue_links(
    doc: dict[str, Any],
    *,
    github_repo: str = DEFAULT_GITHUB_REPO,
) -> list[str]:
    """Return error strings for ``discussions`` anchor or ``#NNN`` issue-link defects."""
    errors: list[str] = []
    anchors = {
        "components": {
            c.get("component_id")
            for c in (doc.get("components") or [])
            if isinstance(c, dict) and c.get("component_id")
        },
        "functions": {
            f.get("function_id")
            for f in (doc.get("functions") or [])
            if isinstance(f, dict) and f.get("function_id")
        },
        "causal_graphs": {
            g.get("graph_id")
            for g in (doc.get("causal_graphs") or [])
            if isinstance(g, dict) and g.get("graph_id")
        },
    }
    issue_prefix = f"https://github.com/{github_repo}/issues/"
    for disc in doc.get("discussions") or []:
        if not isinstance(disc, dict):
            continue
        did = disc.get("discussion_id") or "<discussion>"
        for anchor in disc.get("attaches_to") or []:
            if not isinstance(anchor, str):
                continue
            section, _, local = anchor.partition("#")
            if section in anchors and local not in anchors[section]:
                errors.append(
                    f"{did}: attaches_to anchor {anchor!r} does not resolve"
                )
        ev_refs = {
            str(ev.get("reference") or "").strip()
            for ev in (disc.get("evidence") or [])
            if isinstance(ev, dict)
        }
        prose = " ".join(
            str(disc.get(field) or "")
            for field in ("prompt", "rationale", "resolution_note", "text")
        )
        seen_nums: set[str] = set()
        for match in _PROSE_ISSUE_RE.finditer(prose):
            num = match.group(1)
            if num in seen_nums:
                continue
            seen_nums.add(num)
            expected_url = f"{issue_prefix}{num}"
            if expected_url not in ev_refs:
                errors.append(
                    f"{did}: prose mentions #{num} without {expected_url!r} in discussion.evidence"
                )
    return errors


def validate_record_semantics(
    doc: dict[str, Any],
    *,
    github_repo: str = DEFAULT_GITHUB_REPO,
) -> list[str]:
    """Run all semantic record checks on ``doc``."""
    return [
        *validate_causal_graphs(doc),
        *validate_component_protein_examples(doc),
        *validate_discussion_issue_links(doc, github_repo=github_repo),
    ]
