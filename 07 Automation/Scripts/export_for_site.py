from pathlib import Path
from datetime import date
import re

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "03 Content" / "Blog" / "Exported"
TODAY = date.today().isoformat()


def slugify(text):
    text = text.lower()
    replacements = {"é": "e", "è": "e", "ê": "e", "à": "a", "ç": "c", "ù": "u", "ô": "o", "î": "i", "ï": "i"}
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "article"


def split_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    data = {}
    end = None
    for index, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end = index
            break
        if ":" in line and not line.startswith("  - "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("\"'")
    body = "\n".join(lines[end + 1:]) if end else text
    return data, body


def unique_path(path):
    if not path.exists():
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}-{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


OUT_DIR.mkdir(parents=True, exist_ok=True)
count = 0
for path in sorted((ROOT / "01 Domains").rglob("*.md")):
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta, body = split_frontmatter(text)
    if meta.get("publication_status") not in {"reviewed", "published"}:
        continue
    title = meta.get("title") or path.stem
    slug = slugify(title)
    out = unique_path(OUT_DIR / f"{slug}.md")
    article = f"""---
title: "{title}"
slug: "{slug}"
date: {TODAY}
author: "{meta.get('author') or 'MOULO OHOLO Jean Noel'}"
category: "{meta.get('category') or 'Technical Topic'}"
tags: {meta.get('tags') or '[]'}
description: "Article TianSemi généré depuis la note TSOS {title}."
source_note: "{path.relative_to(ROOT).as_posix()}"
---

{body.strip()}
"""
    out.write_text(article, encoding="utf-8")
    print(f"EXPORTED {out.relative_to(ROOT)}")
    count += 1
print(f"Exported {count} site articles")
