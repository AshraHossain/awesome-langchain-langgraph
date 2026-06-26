"""Validator must reject bad data — tested with deliberately broken copies."""
import copy

import pytest
from lib import load_data, load_schema
from validate import validate


@pytest.fixture
def good():
    return load_data()


@pytest.fixture
def schema():
    return load_schema()


def test_good_data_has_no_errors(good, schema):
    assert validate(good, schema) == []


def test_missing_required_field_flagged(good, schema):
    bad = copy.deepcopy(good)
    del bad["categories"][0]["resources"][0]["url"]
    assert any("url" in e for e in validate(bad, schema))


def test_bad_url_scheme_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"][0]["url"] = "ftp://example.com"
    assert validate(bad, schema)


def test_duplicate_url_flagged(good, schema):
    bad = copy.deepcopy(good)
    first = bad["categories"][0]["resources"][0]["url"]
    bad["categories"][0]["resources"].append(
        {"name": "dup", "url": first, "description": "duplicate entry here", "official": False, "lifecycle": ["build"]}
    )
    assert any("duplicate url" in e for e in validate(bad, schema))


def test_duplicate_category_id_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"].append(copy.deepcopy(bad["categories"][0]))
    assert any("duplicate category id" in e for e in validate(bad, schema))


def test_unknown_lifecycle_stage_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"][0]["lifecycle"] = ["teleport"]
    assert validate(bad, schema)


def test_unknown_group_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["group"] = "nonsense"
    assert validate(bad, schema)


def test_extra_property_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"][0]["sneaky"] = "field"
    assert validate(bad, schema)


def test_too_long_description_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"][0]["description"] = "x" * 281
    assert validate(bad, schema)


def test_bad_version_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["version"] = "v1"
    assert validate(bad, schema)


def test_empty_resources_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"] = []
    assert validate(bad, schema)


def test_non_bool_official_flagged(good, schema):
    bad = copy.deepcopy(good)
    bad["categories"][0]["resources"][0]["official"] = "yes"
    assert validate(bad, schema)
