# Graph Report - .  (2026-06-26)

## Corpus Check
- Corpus is ~9,128 words - fits in a single context window. You may not need a graph.

## Summary
- 217 nodes · 315 edges · 13 communities
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 74 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]

## God Nodes (most connected - your core abstractions)
1. `validate()` - 18 edges
2. `iter_resources()` - 17 edges
3. `load_data()` - 12 edges
4. `flatten()` - 11 edges
5. `artifacts()` - 10 edges
6. `parse_sections()` - 10 edges
7. `apply()` - 9 edges
8. `stats()` - 8 edges
9. `to_resource()` - 8 edges
10. `files` - 6 edges

## Surprising Connections (you probably didn't know these)
- `test_every_resource_name_appears()` --calls--> `iter_resources()`  [INFERRED]
  tests/test_generate_readme.py → scripts/lib.py
- `test_every_url_appears()` --calls--> `iter_resources()`  [INFERRED]
  tests/test_generate_readme.py → scripts/lib.py
- `data()` --calls--> `load_data()`  [INFERRED]
  tests/test_data_integrity.py → scripts/lib.py
- `good()` --calls--> `load_data()`  [INFERRED]
  tests/test_validate.py → scripts/lib.py
- `data()` --calls--> `load_data()`  [INFERRED]
  tests/test_generate_readme.py → scripts/lib.py

## Communities (13 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.10
Nodes (18): github_anchor(), main(), int, str, Generate the curated list section of README.md from resources.json.  The prose (, Slugify a heading the way GitHub does: lowercase, strip punctuation     (but kee, render(), splice() (+10 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (24): object, artifacts(), flatten(), main(), int, str, Generate a static JSON API from resources.json into site/api/.  Static hosting c, One flat list; each entry carries its category id/title/group. (+16 more)

### Community 2 - "Community 2"
Cohesion: 0.14
Nodes (21): load_schema(), main(), int, str, Validate resources.json against the schema plus structural rules.  Governance ga, validate(), test_live_data_passes_full_validation(), Validator must reject bad data — tested with deliberately broken copies. (+13 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (21): additionalProperties, type, minItems, type, additionalProperties, propertyNames, type, properties (+13 more)

### Community 4 - "Community 4"
Cohesion: 0.13
Nodes (12): iter_resources(), Yield (category, resource) pairs across the whole list., The real data file must always be valid and internally consistent.  These are th, test_descriptions_within_bounds(), test_each_lifecycle_stage_used_somewhere(), test_four_pillars_listed(), test_lifecycle_non_empty_and_unique(), test_lifecycle_values_declared() (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.16
Nodes (20): Path, apply(), checked_stages(), main(), parse_sections(), int, str, Turn a 'Suggest a resource' issue-form submission into a validated entry.  GitHu (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.12
Nodes (20): items, minLength, type, enum, pattern, type, additionalProperties, properties (+12 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (13): files, code, document, image, paper, video, graphifyignore_patterns, needs_graph (+5 more)

### Community 8 - "Community 8"
Cohesion: 0.18
Nodes (9): main(), int, Copy the data file into site/ so the static page can fetch it.  ponytail: the pa, load_data(), Shared helpers for the awesome-list tooling., data(), data(), data() (+1 more)

### Community 9 - "Community 9"
Cohesion: 0.36
Nodes (9): $(), buildFilters(), escapeHtml(), highlight(), init(), render(), STAGE_EMOJI, state (+1 more)

### Community 10 - "Community 10"
Cohesion: 0.22
Nodes (8): categories, lifecycle_stages, build, deploy, evaluate, observe, updated, version

### Community 11 - "Community 11"
Cohesion: 0.36
Nodes (8): bool, float, check(), is_alive(), main(), int, str, Check every URL in resources.json is reachable.  The 'evals before you trust the

## Knowledge Gaps
- **52 isolated node(s):** `code`, `document`, `paper`, `image`, `video` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `load_data()` connect `Community 8` to `Community 0`, `Community 1`, `Community 2`, `Community 5`, `Community 11`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Why does `iter_resources()` connect `Community 4` to `Community 0`, `Community 1`, `Community 2`, `Community 8`, `Community 11`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `apply()` connect `Community 5` to `Community 8`, `Community 2`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `validate()` (e.g. with `iter_resources()` and `apply()`) actually correct?**
  _`validate()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `iter_resources()` (e.g. with `validate()` and `main()`) actually correct?**
  _`iter_resources()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `load_data()` (e.g. with `main()` and `main()`) actually correct?**
  _`load_data()` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `flatten()` (e.g. with `iter_resources()` and `test_flatten_count_equals_total()`) actually correct?**
  _`flatten()` has 7 INFERRED edges - model-reasoned connections that need verification._