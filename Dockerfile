# Stage 1: validate the data and stage it next to the static page.
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir jsonschema
COPY data ./data
COPY scripts ./scripts
COPY site ./site
COPY README.md ./README.md
# Fail the build if the data is invalid, then stage resources.json into site/.
RUN python scripts/validate.py && python scripts/build_site.py

# Stage 2: serve the static, searchable directory.
FROM nginx:1.27-alpine
COPY --from=build /app/site /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK CMD wget -qO- http://localhost/ >/dev/null 2>&1 || exit 1
