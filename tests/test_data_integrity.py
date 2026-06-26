"""The real data file must always be valid and internally consistent.

These are the tests that actually matter for an awesome list: the live data
passes the schema, has no dupes, no dead-by-construction URLs, and every
lifecycle tag is real. Padding this to an arbitrary count would add noise,
not safety — so each test asserts one property that would genuinely break the
site or README if violated.
"""
import re
from urllib.parse import urlparse

import pytest
from lib import iter_resources, load_data, load_schema
from validate import validate


@pytest.fixture(scope="module")
def data():
    return load_data()


def test_live_data_passes_full_validation(data):
    assert validate(data, load_schema()) == []


def test_has_required_top_level_keys(data):
    assert {"version", "lifecycle_stages", "categories"} <= set(data)


def test_version_is_semver(data):
    assert re.fullmatch(r"\d+\.\d+\.\d+", data["version"])


def test_at_least_one_category(data):
    assert len(data["categories"]) >= 1


def test_category_ids_unique(data):
    ids = [c["id"] for c in data["categories"]]
    assert len(ids) == len(set(ids))


def test_category_ids_are_slugs(data):
    for cat in data["categories"]:
        assert re.fullmatch(r"[a-z0-9-]+", cat["id"]), cat["id"]


def test_every_category_has_resources(data):
    for cat in data["categories"]:
        assert cat["resources"], cat["id"]


def test_groups_are_known(data):
    for cat in data["categories"]:
        assert cat["group"] in {"ecosystem", "community"}


def test_urls_unique(data):
    urls = [res["url"] for _c, res in iter_resources(data)]
    assert len(urls) == len(set(urls))


def test_urls_are_http_s_with_host(data):
    for _c, res in iter_resources(data):
        parsed = urlparse(res["url"])
        assert parsed.scheme in {"http", "https"}, res["url"]
        assert parsed.netloc, res["url"]


def test_descriptions_within_bounds(data):
    for _c, res in iter_resources(data):
        assert 10 <= len(res["description"]) <= 280, res["name"]


def test_names_non_empty(data):
    for _c, res in iter_resources(data):
        assert res["name"].strip()


def test_official_is_bool(data):
    for _c, res in iter_resources(data):
        assert isinstance(res["official"], bool)


def test_lifecycle_non_empty_and_unique(data):
    for _c, res in iter_resources(data):
        lc = res["lifecycle"]
        assert lc and len(lc) == len(set(lc)), res["name"]


def test_lifecycle_values_declared(data):
    known = set(data["lifecycle_stages"])
    for _c, res in iter_resources(data):
        assert set(res["lifecycle"]) <= known, res["name"]


def test_core_ecosystem_present(data):
    titles = {c["title"] for c in data["categories"]}
    assert "Core Ecosystem" in titles


def test_four_pillars_listed(data):
    names = {res["name"] for _c, res in iter_resources(data)}
    for pillar in ("LangChain (Python)", "LangGraph (Python)", "Deep Agents", "LangSmith"):
        assert pillar in names, pillar


def test_each_lifecycle_stage_used_somewhere(data):
    used = set()
    for _c, res in iter_resources(data):
        used.update(res["lifecycle"])
    assert used == set(data["lifecycle_stages"])


def test_community_group_exists(data):
    assert any(c["group"] == "community" for c in data["categories"])
