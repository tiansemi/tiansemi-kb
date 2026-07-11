# Social Publishers

Ce dossier contient les scripts de publication réelle par plateforme.

## Règle de sécurité

- Pas de secret dans Git.
- Les credentials restent dans `C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred`.
- Les scripts doivent lire les secrets via `TSOS_CRED_DIR` ou variables d'environnement.
- Toute publication réelle doit exiger un flag explicite `--publish`.
- Le mode par défaut doit rester `dry-run`.

## LinkedIn

Script : `publish_linkedin_text.py`

Credentials attendus :

```text
cred/
  linkedin_access_token.txt
  linkedin_person_urn.txt
```

Les deux fichiers peuvent contenir directement la valeur, avec ou sans retour à la ligne final.

Dry-run par défaut, avec le dernier draft Huawei HCIA-Datacom :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py"
```

Dry-run avec un draft précis :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md"
```

Sauvegarder le JSON envoyé à LinkedIn pour revue :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" --payload-out "07 Automation/Exports/linkedin_payload_preview.json"
```

Publier réellement :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" --publish
```
Note author URN :

- Pour publier comme membre LinkedIn, `linkedin_person_urn.txt` doit contenir une valeur de type `urn:li:person:...`.
- Si le fichier contient une URN d'organisation ou de company, le dry-run fonctionne, mais la publication réelle est bloquée par défaut.
- Pour publier comme organisation, il faut confirmer que l'application LinkedIn et le token disposent des permissions adaptées, puis utiliser `--allow-non-person-author` en plus de `--publish`.

## Priorité d'implémentation

1. LinkedIn texte + lien article.
2. Facebook Page texte + lien.
3. YouTube metadata + upload vidéo quand les vidéos seront prêtes.
4. TikTok upload vidéo quand les accès API sont validés.
5. Instagram carousel quand les visuels carrés seront générés.
