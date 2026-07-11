# Social Publishing Credentials Guide

## Principe de sÃ©curitÃ©

Les credentials ne doivent jamais Ãªtre stockÃ©s dans TSOS ni dans le dÃ©pÃ´t du site.

Dossier local prÃ©vu :

```text
C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique FÃ©lix HOUPHOUÃ‹T-BOIGNY - INP-HB\PROJETS\TS\cred
```

Variable d'environnement recommandÃ©e :

```powershell
$env:TSOS_CRED_DIR="C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique FÃ©lix HOUPHOUÃ‹T-BOIGNY - INP-HB\PROJETS\TS\cred"
```

## Structure recommandÃ©e du dossier cred

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

Ã€ prÃ©parer :

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

Ã€ prÃ©parer :

- un projet Google Cloud ;
- YouTube Data API v3 activÃ©e ;
- un client OAuth ;
- un token OAuth autorisant l'upload vidÃ©o ;
- les fichiers vidÃ©o gÃ©nÃ©rÃ©s ou montÃ©s hors TSOS.

## TikTok

Source officielle : https://developers.tiktok.com/doc/content-posting-api-get-started/

Ã€ prÃ©parer :

- une application TikTok for Developers ;
- accÃ¨s Ã  la Content Posting API ;
- OAuth client key / secret ;
- access token ;
- vidÃ©os prÃªtes au format vertical.

## Facebook / Instagram

Sources officielles :

- https://developers.facebook.com/docs/pages-api/posts/
- https://developers.facebook.com/docs/instagram-platform/

Ã€ prÃ©parer :

- application Meta Developer ;
- Page Facebook ;
- compte Instagram professionnel connectÃ© Ã  la Page ;
- permissions nÃ©cessaires selon le type de publication ;
- access token de Page ou token long-lived selon le workflow.

## RÃ¨gle TianSemi

1. GÃ©nÃ©rer les drafts dans TSOS.
2. Valider manuellement le contenu.
3. PrÃ©parer les assets visuels/vidÃ©o.
4. Publier d'abord en mode dry-run.
5. Publier rÃ©ellement seulement avec un flag explicite comme `--publish`.
6. Sauvegarder les URLs publiÃ©es dans le dossier du social pack.


## Note LinkedIn organisation

Pour publier comme page, le token doit inclure w_organization_social; w_member_social ne suffit pas.

