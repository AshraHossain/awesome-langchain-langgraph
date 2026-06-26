"""Generator must be deterministic, idempotent, and faithful to the data."""
import pytest
import re

from generate_readme import github_anchor, render, splice
from lib import AUTOGEN_END, AUTOGEN_START, README_FILE, iter_resources, load_data


@pytest.fixture(scope="module")
def data():
    return load_data()


@pytest.fixture(scope="module")
def output(data):
    return render(data)


def test_every_resource_name_appears(data, output):
    for _c, res in iter_resources(data):
        assert res["name"] in output, res["name"]


def test_every_url_appears(data, output):
    for _c, res in iter_resources(data):
        assert res["url"] in output, res["url"]


def test_every_category_title_appears(data, output):
    for cat in data["categories"]:
        assert cat["title"] in output


def test_official_star_present(data, output):
    assert "⭐" in output  # at least one official entry


def test_lifecycle_emoji_present(output):
    assert any(e in output for e in ("🔨", "🔭", "📊", "🚀"))


def test_render_is_deterministic(data):
    assert render(data) == render(data)


def test_splice_replaces_only_between_markers():
    readme = f"INTRO\n{AUTOGEN_START}\nOLD\n{AUTOGEN_END}\nOUTRO"
    out = splice(readme, "NEW")
    assert "INTRO" in out and "OUTRO" in out
    assert "OLD" not in out and "NEW" in out


def test_splice_is_idempotent(data):
    readme = f"INTRO\n{AUTOGEN_START}\nx\n{AUTOGEN_END}\nOUTRO"
    once = splice(readme, render(data))
    twice = splice(once, render(data))
    assert once == twice


def test_legend_present(output):
    assert "Legend" in output


def test_contents_section_present(output):
    assert "## Contents" in output


def test_toc_anchors_resolve_to_headings(data, output):
    """Every Contents link must point at a heading that exists, using the
    same slug GitHub computes — otherwise the TOC silently fails to jump."""
    toc_anchors = re.findall(r"\]\(#([^)]+)\)", output)
    heading_anchors = {github_anchor(line[4:]) for line in output.splitlines() if line.startswith("### ")}
    assert toc_anchors, "no TOC links found"
    for anchor in toc_anchors:
        assert anchor in heading_anchors, f"dangling TOC anchor: #{anchor}"


def test_github_anchor_handles_punctuation():
    # GitHub keeps the double hyphen where '&'/'—' were removed.
    assert github_anchor("Official Tools & Prebuilt Agents") == "official-tools--prebuilt-agents"
    assert github_anchor("Community — RAG & Knowledge Assistants") == "community--rag--knowledge-assistants"


def test_committed_readme_is_in_sync(data):
    """The committed README must match a fresh generation (CI parity)."""
    readme = README_FILE.read_text(encoding="utf-8")
    assert splice(readme, render(data)) == readme
