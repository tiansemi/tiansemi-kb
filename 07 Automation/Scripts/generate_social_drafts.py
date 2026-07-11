from __future__ import annotations

import argparse
import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_ROOT = ROOT / "03 Content" / "Social Media"


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
    value = value.translate(str.maketrans("àâäçéèêëîïôöùûüÿñ", "aaaceeeeii oouuuyn".replace(" ", "")))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "social-pack"


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Article TianSemi"


def write(path: Path, content: str, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        print(f"SKIP {path.relative_to(ROOT).as_posix()}")
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT).as_posix()}")


def build_pack(article: Path, output_root: Path, overwrite: bool) -> None:
    text = article.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    title = str(meta.get("title") or first_heading(body))
    url = str(meta.get("canonical_url") or meta.get("site_url") or "")
    category = str(meta.get("category") or "TianSemi")
    slug = slugify(str(meta.get("slug") or title))
    pack = output_root / "Huawei" / "HCIA-Datacom" / f"{date.today().isoformat()}-{slug}"

    write(pack / "README.md", f"""
---
title: "Social Pack — {title}"
source_article: "{article.relative_to(ROOT).as_posix()}"
site_url: "{url}"
status: "draft"
publication_status: "not-published"
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
tags:
  - social-media
  - huawei
  - hcia-datacom
---

# Social Pack — {title}

URL source : {url}

## Fichiers à compléter

- linkedin-post.md
- facebook-post.md
- instagram-carousel.md
- tiktok-short-script.md
- youtube-short.md
- youtube-description.md
- whatsapp-community.md
- publishing-checklist.md
""", overwrite)

    write(pack / "linkedin-post.md", f"""
---
platform: LinkedIn
status: draft
source_url: "{url}"
publication_status: not-published
---

# LinkedIn Post

Nouveau contenu TianSemi : {title}

Point clé : transforme la notion en réflexe pratique, pas seulement en définition.

Lire l'article : {url}

#Huawei #HCIADatacom #Réseaux
""", overwrite)

    write(pack / "facebook-post.md", f"""
---
platform: Facebook
status: draft
source_url: "{url}"
publication_status: not-published
---

# Facebook Post

Nouvelle ressource TianSemi : {title}

Objectif : expliquer simplement, pratiquer et retenir les bases.

Lien : {url}
""", overwrite)

    write(pack / "instagram-carousel.md", f"""
---
platform: Instagram
format: carousel
status: draft
source_url: "{url}"
publication_status: not-published
---

# Instagram Carousel

## Slide 1 — Hook
{title}

## Slide 2 — Problème
Ce que les débutants confondent souvent.

## Slide 3 — Concept clé
L'idée à retenir.

## Slide 4 — Exemple
Un exemple visuel simple.

## Slide 5 — Erreur fréquente
Une erreur à éviter.

## Slide 6 — Mini-lab
Une action pratique à faire.

## Slide 7 — CTA
Lire l'article : {url}
""", overwrite)

    write(pack / "tiktok-short-script.md", f"""
---
platform: TikTok
format: short-video
status: draft
source_url: "{url}"
publication_status: not-published
---

# TikTok / Short Script

## Hook
Tu prépares HCIA-Datacom ? Commence par comprendre ceci.

## Corps
Explique l'idée centrale avec un schéma simple et un exemple concret.

## CTA
Article complet sur TianSemi : {url}
""", overwrite)

    write(pack / "youtube-short.md", f"""
---
platform: YouTube
format: short
status: draft
source_url: "{url}"
publication_status: not-published
---

# YouTube Short

## Title
{title}

## Script
Une version courte, visuelle et directe de l'article.

## Hashtags
#Huawei #HCIADatacom #Networking
""", overwrite)

    write(pack / "youtube-description.md", f"""
---
platform: YouTube
format: description
status: draft
source_url: "{url}"
publication_status: not-published
---

# YouTube Description

Dans cette vidéo, on résume : {title}

Article complet : {url}

#Huawei #HCIADatacom #Réseaux
""", overwrite)

    write(pack / "whatsapp-community.md", f"""
---
platform: WhatsApp
status: draft
source_url: "{url}"
publication_status: not-published
---

# WhatsApp Community Post

Nouvelle ressource TianSemi : {title}

Lien : {url}
""", overwrite)

    write(pack / "publishing-checklist.md", f"""
---
title: "Publishing Checklist — {title}"
status: draft
---

# Publishing Checklist

- [ ] LinkedIn
- [ ] Facebook
- [ ] Instagram carousel
- [ ] TikTok / Short
- [ ] YouTube Short
- [ ] WhatsApp community

Après publication :

- [ ] Copier les URLs publiées.
- [ ] Mettre à jour `publication_status`.
- [ ] Mettre à jour la note source TSOS si besoin.
""", overwrite)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate social media draft packs from a TSOS exported article.")
    parser.add_argument("article", type=Path)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    build_pack(args.article, args.output_root, args.overwrite)


if __name__ == "__main__":
    main()