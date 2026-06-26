"""Generator must be deterministic, idempotent, and faithful to the data."""
import pytest
from generate_readme import render, splice
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


def test_committed_readme_is_in_sync(data):
    """The committed README must match a fresh generation (CI parity)."""
    readme = README_FILE.read_text(encoding="utf-8")
    assert splice(readme, render(data)) == readme
