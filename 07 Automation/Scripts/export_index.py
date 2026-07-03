from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "07 Automation" / "Exports" / "kb-index.json"


def parse_value(value):
    value = value.strip()
    if value in {"", "null", "None"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("\"'") for item in inner.split(",")]
    return value.strip("\"'")


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    current_key = None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(line[4:].strip().strip("\"'"))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = parse_value(value)
    return data


items = []
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    rel = path.relative_to(ROOT).as_posix()
    fm = read_frontmatter(path)
    items.append({
        "path": rel,
        "title": fm.get("title") or path.stem,
        "id": fm.get("id"),
        "domain": fm.get("domain"),
        "vendor": fm.get("vendor"),
        "category": fm.get("category"),
        "status": fm.get("status"),
        "publication_status": fm.get("publication_status"),
        "tags": fm.get("tags") or [],
    })

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({"count": len(items), "items": items}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Exported {len(items)} notes to {OUT.relative_to(ROOT)}")
