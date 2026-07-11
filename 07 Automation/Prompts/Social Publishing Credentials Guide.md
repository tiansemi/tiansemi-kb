# Social Publishing Credentials Guide

## Principe de sécurité

Les credentials ne doivent jamais être stockés dans TSOS ni dans le dépôt du site.

Dossier local prévu :

```text
C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred
```

Variable d'environnement recommandée :

```powershell
$env:TSOS_CRED_DIR="C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred"
```

## Structure recommandée du dossier cred

```text
cred/
  linkedin_auth_keys.yaml
  linkedin_access_token.txt
  linkedin_person_urn.txt
  youtube_oauth_client.json
  youtube_token.json
  meta_app_credentials.json
  meta_page_access_token.txt
  instagram_account_id.txt
  tiktok_client.json
  tiktok_access_token.txt
```

## LinkedIn

Source officielle : https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin

À préparer :

- une application LinkedIn Developer ;
- le produit Share on LinkedIn ;
- le scope OAuth `w_member_social` ;
- un access token ;
- le Person URN du profil qui publie.

Endpoint de publication texte/article :

```text
POST https://api.linkedin.com/v2/ugcPosts
```

## YouTube

Source officielle : https://developers.google.com/youtube/v3/guides/uploading_a_video

À préparer :

- un projet Google Cloud ;
- YouTube Data API v3 activée ;
- un client OAuth ;
- un token OAuth autorisant l'upload vidéo ;
- les fichiers vidéo générés ou montés hors TSOS.

## TikTok

Source officielle : https://developers.tiktok.com/doc/content-posting-api-get-started/

À préparer :

- une application TikTok for Developers ;
- accès à la Content Posting API ;
- OAuth client key / secret ;
- access token ;
- vidéos prêtes au format vertical.

## Facebook / Instagram

Sources officielles :

- https://developers.facebook.com/docs/pages-api/posts/
- https://developers.facebook.com/docs/instagram-platform/

À préparer :

- application Meta Developer ;
- Page Facebook ;
- compte Instagram professionnel connecté à la Page ;
- permissions nécessaires selon le type de publication ;
- access token de Page ou token long-lived selon le workflow.

## Règle TianSemi

1. Générer les drafts dans TSOS.
2. Valider manuellement le contenu.
3. Préparer les assets visuels/vidéo.
4. Publier d'abord en mode dry-run.
5. Publier réellement seulement avec un flag explicite comme `--publish`.
6. Sauvegarder les URLs publiées dans le dossier du social pack.
