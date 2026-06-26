# Awesome LangChain Knowledge Graph

## Project Stats
- **Files**: 17 Python + 16 Markdown
- **Nodes**: 217
- **Edges**: 315
- **Communities**: 13

## Architecture Overview
This graph maps the full pipeline:
1. Data validation (validate.py)
2. Resource generation (generate_readme.py, build_site.py, build_api.py)
3. Testing (test_*.py files)
4. CI/CD workflows (.github/workflows/)
5. Documentation (README.md, CONTRIBUTING.md, USER_GUIDE.md, VISUAL_GUIDE.md)

## Key Components
- validate(): Schema + structural validation
- load_data(): Read resources.json and apply schema
- render(): Generate HTML cards from resource data
- iter_resources(): Common iterator for resources
- build_filters(): Create interactive filter buttons
- fetch + link_check: Network requests and validation

God nodes (most connected) represent core abstractions that multiple components depend on.
Surprising connections show unexpected relationships between modules.
