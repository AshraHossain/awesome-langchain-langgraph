.PHONY: install validate generate site links test serve docker check

install:
	pip install -r requirements.txt

validate:
	python scripts/validate.py

generate:
	python scripts/generate_readme.py

site: validate
	python scripts/build_site.py

links:
	python scripts/check_links.py

test:
	python -m pytest -q

# Full CI-equivalent gate (no network link check).
check: validate test
	python scripts/generate_readme.py --check

serve: site
	python -m http.server -d site 8080

docker:
	docker compose up --build
