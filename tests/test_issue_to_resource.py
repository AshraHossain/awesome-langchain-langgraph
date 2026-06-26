"""Parsing an issue-form body into a resource entry (pure, no I/O)."""
from issue_to_resource import checked_stages, parse_sections, to_resource

SAMPLE = """### Name

LangGraph Bigtool

### URL

https://github.com/langchain-ai/langgraph-bigtool

### Description

Agent helper for selecting from large tool collections via semantic search.

### Category

Official Tools & Prebuilt Agents

### Lifecycle stage(s)

- [x] 🔨 build
- [ ] 🔭 observe
- [x] 📊 evaluate
- [ ] 🚀 deploy

### Is this a first-party langchain-ai project?

Yes (official)
"""


def test_parse_sections_extracts_all_labels():
    s = parse_sections(SAMPLE)
    assert s["Name"] == "LangGraph Bigtool"
    assert s["URL"].startswith("https://")
    assert "semantic search" in s["Description"]
    assert s["Category"] == "Official Tools & Prebuilt Agents"


def test_checked_stages_only_checked_in_canonical_order():
    s = parse_sections(SAMPLE)
    assert checked_stages(s["Lifecycle stage(s)"]) == ["build", "evaluate"]


def test_to_resource_builds_valid_shape():
    res, category = to_resource(parse_sections(SAMPLE))
    assert res["name"] == "LangGraph Bigtool"
    assert res["url"].startswith("https://")
    assert res["official"] is True
    assert res["lifecycle"] == ["build", "evaluate"]
    assert category == "Official Tools & Prebuilt Agents"


def test_official_false_when_no():
    body = SAMPLE.replace("Yes (official)", "No")
    res, _ = to_resource(parse_sections(body))
    assert res["official"] is False


def test_no_lifecycle_checked_defaults_to_build():
    body = SAMPLE.replace("- [x] 🔨 build", "- [ ] 🔨 build").replace("- [x] 📊 evaluate", "- [ ] 📊 evaluate")
    res, _ = to_resource(parse_sections(body))
    assert res["lifecycle"] == ["build"]


def test_no_response_becomes_empty():
    body = SAMPLE.replace("https://github.com/langchain-ai/langgraph-bigtool", "_No response_")
    assert parse_sections(body)["URL"] == ""
