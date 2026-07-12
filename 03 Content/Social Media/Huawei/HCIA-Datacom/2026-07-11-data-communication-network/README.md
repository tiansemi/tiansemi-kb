---
title: "Social Pack — HCIA-Datacom : comprendre les réseaux de communication de données"
source_article: "03 Content/Blog/Exported/hcia-datacom-comprendre-reseaux-communication-donnees.md"
site_url: "https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees/"
status: "draft"
publication_status: "youtube-ready-linkedin-debt-facebook-tiktok-manual"
created: 2026-07-11
updated: 2026-07-12
tags:
  - social-media
  - huawei
  - hcia-datacom
---

# Social Pack — HCIA-Datacom : comprendre les réseaux de communication de données

URL source : https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees/

## Stratégie de publication

| Canal | Mode | Statut |
|---|---|---|
| YouTube | Automatisable via API | Prêt côté credentials, attente fichier vidéo |
| LinkedIn profil | Automatisable plus tard | Dette technique temporaire |
| LinkedIn page | Automatisable après revue LinkedIn | Bloqué par revue/permissions organisation |
| TikTok | Manuel | Génération assets seulement |
| Facebook | Manuel | Génération assets seulement |
| Instagram | Exclu | Pas de publication prévue |
| WhatsApp | Manuel | Draft prêt |

## Fichiers

- youtube-metadata.json
- youtube-short.md
- youtube-description.md
- facebook-post.md
- tiktok-short-script.md
- whatsapp-community.md
- linkedin-post.md
- publishing-checklist.md

## Commandes YouTube

Dry-run :

```powershell
python "07 Automation/Scripts/social_publishers/publish_youtube_video.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/youtube-metadata.json"
```

Publication réelle après création du fichier vidéo :

```powershell
python "07 Automation/Scripts/social_publishers/publish_youtube_video.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/youtube-metadata.json" --video-file "CHEMIN\VERS\VIDEO.mp4" --publish
```

## État LinkedIn

La page LinkedIn TianSemi est en revue. On laisse LinkedIn en dette technique temporaire.

Diagnostic précédent : le token actif était limité à `w_member_social`; la page exige `w_organization_social` lorsque l'app sera validée.
