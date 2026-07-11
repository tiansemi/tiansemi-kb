---
title: "Social Pack — HCIA-Datacom : comprendre les réseaux de communication de données"
source_article: "03 Content/Blog/Exported/hcia-datacom-comprendre-reseaux-communication-donnees.md"
site_url: "https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees/"
status: "draft"
publication_status: "blocked-linkedin-credentials"
created: 2026-07-11
updated: 2026-07-11
tags:
  - social-media
  - huawei
  - hcia-datacom
---

# Social Pack — HCIA-Datacom : comprendre les réseaux de communication de données

URL source : https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees/

## Fichiers

- linkedin-post.md
- facebook-post.md
- instagram-carousel.md
- tiktok-short-script.md
- youtube-short.md
- youtube-description.md
- whatsapp-community.md
- publishing-checklist.md

## État LinkedIn

Publication comme organisation/page TianSemi tentée le 2026-07-11.

Résultat : bloqué par credentials.

Diagnostic : le token LinkedIn est actif mais porte seulement le scope `w_member_social`. Pour publier comme page/organisation avec `author = urn:li:organization:142874764`, LinkedIn exige `w_organization_social`.

Action requise : générer un nouveau token LinkedIn avec le produit/API permettant `w_organization_social`, puis relancer :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --check-token
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --publish
```
