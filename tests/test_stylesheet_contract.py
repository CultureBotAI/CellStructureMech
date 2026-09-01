"""The stylesheet resolves, and resolves the same way in both dark declarations.

CSS never reports a failure. An undefined token falls back to its literal, a
duplicated selector quietly overrides the earlier one, and a dark value present
in one of the two dark blocks but not the other themes correctly by toggle and
incorrectly by OS preference. Every one of those renders, passes
`render_pages.py --check`, and passes a page-level site contract — so "it
rendered" says almost nothing about whether it rendered correctly.

Ported from AntibioticMech's contract of the same name (its #116), which was
written from the other side of the same PR pair as this repository's #95: a
visualisation added on `main` during an open design branch painted itself with
literal light colours, because nothing prompts an author to use tokens and
nothing fails when they do not.
"""

from __future__ import annotations

import re

STYLESHEET = "src/cellstructuremech/templates/style.css"
# Every stylesheet the site ships, including the ones embedded in a page. The
# landing page carries a 112-line inline block with its own :root palette, so a
# contract that read only style.css would leave the site's front door unchecked
# (#97).
TEMPLATE_DIR = "src/cellstructuremech/templates"
INLINE_STYLE = re.compile(r"<style[^>]*>(.*?)</style>", re.S)

# Declared more than once on purpose. Each entry is a decision, not an
# observation: a name added here should be a layer that deliberately re-opens a
# selector, never a merge that appended one stylesheet to another.
ALLOWED_DUPLICATE_SELECTORS: set[str] = set()

TOKEN_DECL = re.compile(r"^\s*(--[\w-]+)\s*:", re.M)
RULE_SELECTOR = re.compile(r"(?m)^([^\s@/}][^{]*)\{")
VAR_WITH_FALLBACK = re.compile(r"var\(\s*(--[\w-]+)\s*,\s*([^)]+)\)")
# Deliberately NOT anchored to the start of a line. The sibling's stylesheet
# puts one declaration per line; this one writes whole rules inline
# (`header .brand{font-weight:700;color:var(--ink)}`), so a line-anchored
# pattern matched almost nothing here and the check could not have failed.
COLOUR_LITERAL = re.compile(
    r"(?<![\w-])(?:color|background|background-color)\s*:\s*"
    r"(#[0-9a-fA-F]{3,8}|white|black)\b"
)


def _text(repo_root):
    return (repo_root / STYLESHEET).read_text(encoding="utf-8")


def _all_stylesheets(repo_root) -> dict[str, str]:
    """Name -> CSS, for the standalone stylesheet and every inline block."""
    sheets = {STYLESHEET: _text(repo_root)}
    for template in sorted((repo_root / TEMPLATE_DIR).glob("*.html")):
        for index, block in enumerate(INLINE_STYLE.findall(template.read_text(encoding="utf-8"))):
            sheets[f"{template.name} <style> #{index + 1}"] = block
    return sheets


# --- the four checks, as functions of the text -------------------------------
# A contract that has only ever been run against a passing file is a contract
# nobody has seen work. Each is exercised below against a stylesheet mutated to
# carry the exact defect it exists to catch (#95).


def undefined_fallbacks(text: str) -> list[tuple[str, str]]:
    defined = set(TOKEN_DECL.findall(text))
    return sorted({(name, fb.strip()) for name, fb in VAR_WITH_FALLBACK.findall(text)
                   if name not in defined})


def duplicate_selectors(text: str, allowed: set[str] = frozenset()) -> list[str]:
    seen: dict[str, int] = {}
    for selector in RULE_SELECTOR.findall(text):
        key = " ".join(selector.split())
        seen[key] = seen.get(key, 0) + 1
    return sorted(s for s, n in seen.items() if n > 1 and s not in allowed)


def colour_literals(text: str) -> list[str]:
    return sorted(set(COLOUR_LITERAL.findall(text)))


def dark_block_divergence(text: str) -> tuple[list[str], list[str], list[str]]:
    """(only under preference, only under toggle, same token different value)."""
    by_preference = _token_block(text, ':root:not([data-theme="light"])')
    by_toggle = _token_block(text, ':root[data-theme="dark"]')
    differing = sorted(name for name in by_preference
                       if name in by_toggle
                       and by_preference[name].strip() != by_toggle[name].strip())
    return (sorted(set(by_preference) - set(by_toggle)),
            sorted(set(by_toggle) - set(by_preference)),
            differing)


def _token_block(text: str, selector: str) -> dict[str, str]:
    """The custom-property declarations of the first rule with this selector.

    Written against the file as it is formatted rather than a canonical form:
    the brace may or may not be preceded by a space, and the preference block
    sits inside an @media rule.
    """
    match = re.search(re.escape(selector) + r"\s*\{", text)
    assert match, f"no rule for {selector}"
    body = text[match.end() : text.index("}", match.end())]
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body))


def test_no_var_falls_back_to_a_token_the_stylesheet_never_defines(repo_root):
    """A fallback for a token that exists is a default. A fallback for one that
    does not is a silent substitution — the literal is what actually paints."""
    missing = undefined_fallbacks(_text(repo_root))
    assert not missing, (
        "var() names a token this stylesheet never defines, so the literal "
        f"fallback is what actually paints: {missing}"
    )


def test_no_selector_is_declared_twice_outside_the_override_set(repo_root):
    """Appending one stylesheet to another produces a file that renders and is
    wrong: whichever copy lands last wins, including its palette."""
    duplicated = duplicate_selectors(_text(repo_root), ALLOWED_DUPLICATE_SELECTORS)
    assert not duplicated, (
        f"selector declared more than once; the later copy silently overrides the earlier: {duplicated}"
    )


def test_colours_come_from_tokens_so_they_can_respond_to_the_theme(repo_root):
    """A literal in a color/background declaration cannot change with the theme."""
    literals = colour_literals(_text(repo_root))
    assert not literals, (
        f"colour literal outside the token blocks; it cannot respond to the theme: {sorted(set(literals))}"
    )


def test_both_dark_blocks_declare_the_same_tokens(repo_root):
    """Dark values are declared twice by design — once for OS preference, once
    for the toggle. A token added to one and not the other yields a page that
    themes correctly one way and not the other, which no page-level check sees."""
    text = _text(repo_root)
    assert _token_block(text, ':root[data-theme="dark"]'), "expected both dark declarations"
    only_pref, only_toggle, differing = dark_block_divergence(text)
    assert not only_pref and not only_toggle, (
        f"only under prefers-color-scheme: {only_pref}; only under data-theme: {only_toggle}"
    )
    assert not differing, f"same token, different dark value: {differing}"


# --- mutation tests ----------------------------------------------------------
# Each injects the exact defect one check exists to catch. If a mutation stops
# being detected, the check has been weakened and the contract is decorative.


def test_an_undefined_token_fallback_is_detected(repo_root):
    mutated = _text(repo_root).replace("var(--muted)", "var(--muted-x, #999)", 1)
    assert ("--muted-x", "#999") in undefined_fallbacks(mutated)
    assert not undefined_fallbacks(_text(repo_root)), "the unmutated file must be clean"


def test_a_duplicated_selector_is_detected(repo_root):
    text = _text(repo_root)
    mutated = text + "\nbody{background:var(--bg)}\n"
    assert "body" in duplicate_selectors(mutated)


def test_an_appended_stylesheet_is_detected(repo_root):
    """The shape #95 describes: one stylesheet appended to another rather than
    folded in. Every selector in the appended copy duplicates one already there."""
    text = _text(repo_root)
    assert len(duplicate_selectors(text + text)) > 5


def test_a_colour_literal_is_detected(repo_root):
    for literal in ("#ffffff", "white", "#0a0a0a"):
        mutated = _text(repo_root) + f"\n.chart-ground{{\n  background: {literal};\n}}\n"
        assert literal in colour_literals(mutated), literal


def test_a_token_added_to_only_one_dark_block_is_detected(repo_root):
    """The asymmetry that themes correctly by toggle and wrongly by OS setting."""
    text = _text(repo_root)
    mutated = re.sub(r'(:root\[data-theme="dark"\]\s*\{)', r"\1\n  --plot-ground:#101014;", text, count=1)
    only_pref, only_toggle, _ = dark_block_divergence(mutated)
    assert only_toggle == ["--plot-ground"] and not only_pref


def test_the_same_token_with_different_dark_values_is_detected(repo_root):
    text = _text(repo_root)
    tokens = _token_block(text, ':root[data-theme="dark"]')
    name = sorted(tokens)[0]
    mutated = re.sub(rf'(:root\[data-theme="dark"\]\s*\{{[^}}]*?){re.escape(name)}\s*:[^;]+;',
                     rf"\1{name}:#123456;", text, count=1, flags=re.S)
    _, _, differing = dark_block_divergence(mutated)
    assert differing == [name], f"expected {name} to diverge, got {differing}"


# --- every stylesheet the site ships, not just the standalone one ------------


def test_every_stylesheet_is_free_of_undefined_token_fallbacks(repo_root):
    bad = {name: undefined_fallbacks(css) for name, css in _all_stylesheets(repo_root).items()}
    assert not {k: v for k, v in bad.items() if v}, {k: v for k, v in bad.items() if v}


def test_every_stylesheet_takes_its_colours_from_tokens(repo_root):
    """An inline block is as capable of a literal as a standalone file, and the
    landing page's block is where a literal would be least visible (#97)."""
    bad = {}
    for name, css in _all_stylesheets(repo_root).items():
        # Literals belong in a token declaration and nowhere else. Strip only
        # rules that actually declare tokens — a selector merely starting with
        # `:root` (`:root[data-theme="dark"] .btn{color:#121320}`) is a normal
        # rule and its literal must still be caught.
        without_tokens = re.sub(r"[^{}]*\{[^{}]*--[\w-]+\s*:[^{}]*\}", "", css, flags=re.S)
        if literals := colour_literals(without_tokens):
            bad[name] = literals
    assert not bad, f"colour literals outside a token block: {bad}"


def test_every_stylesheet_declares_its_tokens_in_all_of_its_theme_blocks(repo_root):
    """A stylesheet may hold tokens the canonical palette lacks — the landing
    page is self-contained and has its own components. What it may not do is
    declare a token in one theme block and not the others, which themes
    correctly one way and wrongly the other. This generalises the dark-symmetry
    check to every stylesheet, inline blocks included (#97)."""
    incomplete = {}
    for name, css in _all_stylesheets(repo_root).items():
        if ':root[data-theme="dark"]' not in css:
            continue  # a stylesheet with no theme blocks has nothing to keep in step
        light = set(_token_block(css, ":root"))
        pref = set(_token_block(css, ':root:not([data-theme="light"])'))
        toggle = set(_token_block(css, ':root[data-theme="dark"]'))
        # A dark block overrides a subset of the light palette; the two dark
        # blocks must cover exactly the same names as each other.
        if missing := sorted((pref ^ toggle) | (pref - light) | (toggle - light)):
            incomplete[name] = missing
    assert not incomplete, f"token declared in some theme blocks but not others: {incomplete}"


def test_a_second_palette_agrees_with_the_canonical_one(repo_root):
    """Two copies of a palette drift. Where both declare a token, the values
    must match, or one page themes differently from the others (#97)."""
    sheets = _all_stylesheets(repo_root)
    canonical = _token_block(sheets[STYLESHEET], ":root")
    disagreements = {}
    for name, css in sheets.items():
        if name == STYLESHEET or ":root" not in css:
            continue
        other = _token_block(css, ":root")
        differing = sorted(t for t in other if t in canonical
                           and other[t].split("/*")[0].strip() != canonical[t].split("/*")[0].strip())
        if differing:
            disagreements[name] = differing
    assert not disagreements, f"same token, different value from style.css: {disagreements}"
