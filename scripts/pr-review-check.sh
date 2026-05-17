#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ ! -d content/questions ]]; then
  echo "content/questions not found" >&2
  exit 1
fi

shopt -s nullglob
json_files=(content/questions/*.json)
if [[ ${#json_files[@]} -eq 0 ]]; then
  echo "no JSON files in content/questions" >&2
  exit 1
fi

for f in "${json_files[@]}"; do
  python3 -c "import json, pathlib, sys; json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))" "$f"
  echo "OK JSON: $f"
done

if [[ ! -d docs ]]; then
  echo "docs/ missing" >&2
  exit 1
fi

md_count=$(find docs -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
if [[ "$md_count" -lt 1 ]]; then
  echo "no markdown files in docs/" >&2
  exit 1
fi
echo "OK docs: ${md_count} markdown file(s) at docs/"
