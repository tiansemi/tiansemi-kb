---
title: "Publishing Checklist — HCIA-Datacom : comprendre les réseaux de communication de données"
status: draft
updated: 2026-07-11
---

# Publishing Checklist

- [ ] LinkedIn page TianSemi
  - Statut : bloqué credentials.
  - Diagnostic : token actif, scope actuel `w_member_social`.
  - Requis : `w_organization_social` pour publier comme organisation/page.
  - Organisation : `urn:li:organization:142874764`.
- [ ] Facebook
- [ ] Instagram carousel
- [ ] TikTok / Short
- [ ] YouTube Short
- [ ] WhatsApp Community

## Commandes LinkedIn

Vérifier le token :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --check-token
```

Publier après génération du bon token :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --publish
```
