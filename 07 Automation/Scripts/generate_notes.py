from pathlib import Path
import csv
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "07 Automation" / "Blueprints" / "cisco_ccna_seed.csv"
TODAY = date.today().isoformat()
AUTHOR = "MOULO OHOLO Jean Noel"

TEMPLATE = """---
id: {id}
title: "{title}"
aliases: []
category: "Technical Topic"
domain: "Networking"
vendor: "Cisco"
difficulty: "beginner"
ccna: true
ccnp: false
hcip: false
exam: "CCNA 200-301"
status: "draft"
author: "{author}"
reviewed: false
last_review:
created: {today}
updated: {today}
tags: [cisco, networking, ccna]
keywords: []
prerequisites: []
related: []
references: []
assets: []
labs: []
blog:
linkedin:
facebook:
instagram:
youtube:
tiktok:
site_url:
publication_status: "not-started"
---

# {title}

## Résumé

> Résumé court en 5 lignes maximum.

---

## Définition

---

## Pourquoi c'est important ?

---

## Objectif pédagogique

---

## Fonctionnement

---

## Concepts clés

---

## Architecture

---

## Exemple concret

---

## Cisco CLI

```bash

```

---

## Huawei CLI

```bash

```

---

## Wireshark

---

## Troubleshooting

| Problème | Cause probable | Solution |
| -------- | -------------- | -------- |

---

## Bonnes pratiques

---

## Erreurs fréquentes

---

## Questions d'entretien

---

## Quiz

---

## Flashcards

---

## Labs

---

## Références

---

## Contenus générés

| Canal         | Statut     | Lien |
| ------------- | ---------- | ---- |
| Site TianSemi | Non généré |      |
| Blog          | Non généré |      |
| LinkedIn      | Non généré |      |
| Facebook      | Non généré |      |
| Instagram     | Non généré |      |
| TikTok        | Non généré |      |
| YouTube       | Non généré |      |
| Newsletter    | Non généré |      |
"""

with CSV_PATH.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        path = ROOT / row["folder"] / f"{row['title']}.md"
        if path.exists():
            print(f"SKIP {path.relative_to(ROOT)}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(TEMPLATE.format(id=row["id"], title=row["title"], author=AUTHOR, today=TODAY), encoding="utf-8")
        print(f"CREATED {path.relative_to(ROOT)}")
