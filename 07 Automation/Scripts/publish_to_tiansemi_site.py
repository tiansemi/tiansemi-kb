from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SITE_ROOT = Path(r"C:\Users\MOULO Oholo Jean\Documents\ts\tiansemi.github.io")
DEFAULT_SECTION = "apprentissage/reseaux"
BASE_URL = "https://tiansemi.github.io"


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip().splitlines()
    body = text[end + 5 :].strip()
    data: dict[str, object] = {}
    key: str | None = None
    for line in raw:
        if line.startswith("  - ") and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(line[4:].strip().strip('"\''))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                data[key] = []
            elif value.startswith('"') and value.endswith('"'):
                data[key] = value[1:-1]
            else:
                data[key] = value
    return data, body


def slugify(value: str) -> str:
    value = value.lower()
    replacements = str.maketrans("àâäçéèêëîïôöùûüÿñ", "aaaceeeeii_oouuuyn".replace("_", ""))
    value = value.translate(replacements)
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "article"


def inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def table_to_html(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [inline_markdown(cell.strip()) for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return "\n".join(f"<p>{inline_markdown(line)}</p>" for line in lines)
    head = rows[0]
    body = rows[2:]
    out = ['<div class="learning-table-wrap">', '<table class="learning-table">', '<thead><tr>']
    out.extend(f"<th>{cell}</th>" for cell in head)
    out.extend(["</tr></thead>", "<tbody>"])
    for row in body:
        out.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    out.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(out)


def markdown_to_html(body: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    ordered_items: list[str] = []
    table_lines: list[str] = []
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items, ordered_items
        if list_items:
            out.append("<ul>" + "".join(f"<li>{item}</li>" for item in list_items) + "</ul>")
            list_items = []
        if ordered_items:
            out.append("<ol>" + "".join(f"<li>{item}</li>" for item in ordered_items) + "</ol>")
            ordered_items = []

    def flush_table() -> None:
        nonlocal table_lines
        if table_lines:
            out.append(table_to_html(table_lines))
            table_lines = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph(); flush_list(); flush_table()
            if not in_code:
                in_code = True
                code_lines = []
            else:
                code = html.escape("\n".join(code_lines))
                out.append(f'<pre class="learning-code" data-code-label="Exemple technique"><code>{code}</code></pre>')
                in_code = False
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_paragraph(); flush_list(); flush_table()
            continue
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            flush_paragraph(); flush_list(); flush_table()
            out.append(f"<section><h2>{inline_markdown(line[3:].strip())}</h2>")
            continue
        if line.startswith("|幅"):
            pass
        if line.startswith("|") and line.endswith("|"):
            flush_paragraph(); flush_list()
            table_lines.append(line)
            continue
        if line.startswith("- "):
            flush_paragraph(); flush_table()
            list_items.append(inline_markdown(line[2:].strip()))
            continue
        ordered = re.match(r"^\d+\.\s+(.*)$", line)
        if ordered:
            flush_paragraph(); flush_table()
            ordered_items.append(inline_markdown(ordered.group(1)))
            continue
        if line.startswith("> "):
            flush_paragraph(); flush_list(); flush_table()
            out.append(f"<blockquote><p>{inline_markdown(line[2:].strip())}</p></blockquote>")
            continue
        paragraph.append(line.strip())
    flush_paragraph(); flush_list(); flush_table()
    return "\n".join(out)


def build_page(meta: dict[str, object], body_html: str, section: str, hero_image: str | None) -> str:
    title = str(meta.get("title") or "Article TianSemi")
    description = str(meta.get("description") or "Ressource TianSemi")
    slug = str(meta.get("slug") or slugify(title))
    url = f"{BASE_URL}/{section}/{slug}/"
    image_tag = ""
    if hero_image:
        image_tag = f'<figure style="margin:0 0 2rem;"><img src="../../../{hero_image}" width="1200" height="675" loading="eager" decoding="async" alt="Visuel de la ressource {html.escape(title)}" style="display:block;width:100%;height:auto;border-radius:24px;border:1px solid var(--color-border);"></figure>'
    return f'''<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} — TianSemi</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="TianSemi">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{url}">
    <link rel="shortcut icon" href="../../../favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="../../../assets/css/navigation.min.css">
    <link rel="stylesheet" href="../../../assets/css/learning.min.css">
  </head>
  <body class="dark_theme">
    <div data-site-nav data-site-root="../../../"></div>
    <main class="learning-page">
      <div class="learning-shell">
        <article class="learning-article">
          <header class="learning-article__header">
            <p class="learning-eyebrow">{html.escape(str(meta.get('category') or 'TianSemi'))}</p>
            <h1>{html.escape(title)}</h1>
            <p class="learning-article__lead">{html.escape(description)}</p>
          </header>
          {image_tag}
          <div class="learning-article__grid">
            <div class="learning-prose">
              {body_html}
            </div>
          </div>
        </article>
      </div>
    </main>
    <script src="../../../assets/js/navigation.min.js"></script>
    <script src="../../../assets/js/learning.min.js"></script>
    <script src="../../../assets/js/i18n.min.js"></script>
  </body>
</html>
'''


def upsert_sitemap(site_root: Path, url: str) -> None:
    sitemap = site_root / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    if url in text:
        return
    block = f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{date.today().isoformat()}</lastmod>\n  </url>\n"
    sitemap.write_text(text.replace("</urlset>", block + "</urlset>"), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish a TSOS Markdown article to the TianSemi static site.")
    parser.add_argument("article", type=Path, help="Markdown article exported from TSOS")
    parser.add_argument("--site-root", type=Path, default=DEFAULT_SITE_ROOT)
    parser.add_argument("--section", default=DEFAULT_SECTION)
    parser.add_argument("--hero-image", default=None, help="Relative image path from site root, for example assets/images/cover.svg")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    text = args.article.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    slug = str(meta.get("slug") or slugify(str(meta.get("title") or args.article.stem)))
    body_html = markdown_to_html(body)
    target = args.site_root / args.section / slug / "index.html"
    if target.exists() and not args.overwrite:
        print(f"SKIP existing page: {target}")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_page(meta, body_html, args.section, args.hero_image), encoding="utf-8")
        print(f"WROTE {target}")
    upsert_sitemap(args.site_root, f"{BASE_URL}/{args.section}/{slug}/")
    print("DONE")


if __name__ == "__main__":
    main()