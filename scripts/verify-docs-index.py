import sys
from pathlib import Path

docs_dir = Path(__file__).resolve().parents[1] / "docs"
index_path = docs_dir / "index.md"

if not index_path.exists():
    print("docs/index.md not found")
    sys.exit(1)

content = index_path.read_text(encoding="utf-8")
missing = []

for doc in sorted(docs_dir.glob("*.md")):
    if doc.name == "index.md":
        continue
    rel = f"docs/{doc.name}"
    if rel not in content:
        missing.append(rel)

if missing:
    print("Missing in docs/index.md:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)

print("Docs index is up to date.")
