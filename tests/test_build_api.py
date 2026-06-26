"""The static JSON API must be a faithful, complete projection of the data."""
import pytest
from build_api import artifacts, flatten, shield, stats
from lib import iter_resources, load_data


@pytest.fixture(scope="module")
def data():
    return load_data()


def test_flatten_count_equals_total(data):
    assert len(flatten(data)) == sum(len(c["resources"]) for c in data["categories"])


def test_flatten_entries_carry_category_metadata(data):
    for entry in flatten(data):
        assert entry["category_id"] and entry["category_title"] and entry["group"]
        assert {"name", "url", "description", "official", "lifecycle"} <= set(entry)


def test_flatten_preserves_every_url(data):
    flat_urls = {e["url"] for e in flatten(data)}
    assert flat_urls == {res["url"] for _c, res in iter_resources(data)}


def test_stats_total_matches(data):
    s = stats(data)
    assert s["total"] == len(flatten(data))


def test_stats_by_lifecycle_sums_consistently(data):
    s = stats(data)
    # Each resource contributes to one or more stages; total tags >= total resources.
    assert sum(s["by_lifecycle"].values()) >= s["total"]
    assert set(s["by_lifecycle"]) == set(data["lifecycle_stages"])


def test_stats_by_group_sums_to_total(data):
    s = stats(data)
    assert sum(s["by_group"].values()) == s["total"]


def test_stats_official_count_correct(data):
    s = stats(data)
    assert s["official"] == sum(1 for e in flatten(data) if e["official"])


def test_shield_is_valid_endpoint_schema(data):
    sh = shield(data)
    assert sh["schemaVersion"] == 1
    assert sh["label"] == "resources"
    assert sh["message"] == str(stats(data)["total"])


def test_artifacts_include_expected_endpoints(data):
    arts = artifacts(data)
    assert "api/resources.json" in arts
    assert "api/stats.json" in arts
    assert "api/shield.json" in arts
    for stage in data["lifecycle_stages"]:
        assert f"api/lifecycle/{stage}.json" in arts


def test_lifecycle_slice_only_contains_matching_resources(data):
    arts = artifacts(data)
    for stage in data["lifecycle_stages"]:
        for entry in arts[f"api/lifecycle/{stage}.json"]:
            assert stage in entry["lifecycle"]


def test_every_resource_appears_in_some_lifecycle_slice(data):
    arts = artifacts(data)
    covered = set()
    for stage in data["lifecycle_stages"]:
        covered.update(e["url"] for e in arts[f"api/lifecycle/{stage}.json"])
    assert covered == {e["url"] for e in flatten(data)}
