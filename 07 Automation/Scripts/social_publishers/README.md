# Social Publishers

Ce dossier contient les scripts de publication rÃ©elle par plateforme.

## RÃ¨gle de sÃ©curitÃ©

- Pas de secret dans Git.
- Les credentials restent dans `C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique FÃ©lix HOUPHOUÃ‹T-BOIGNY - INP-HB\PROJETS\TS\cred`.
- Les scripts doivent lire les secrets via `TSOS_CRED_DIR` ou variables d'environnement.
- Toute publication rÃ©elle doit exiger un flag explicite `--publish`.
- Le mode par dÃ©faut doit rester `dry-run`.

## LinkedIn

Script : `publish_linkedin_text.py`

Credentials attendus :

```text
cred/
  linkedin_access_token.txt
  linkedin_person_urn.txt
```

Les deux fichiers peuvent contenir directement la valeur, avec ou sans retour Ã  la ligne final.

Dry-run par dÃ©faut, avec le dernier draft Huawei HCIA-Datacom :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py"
```

Dry-run avec un draft prÃ©cis :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md"
```

Sauvegarder le JSON envoyÃ© Ã  LinkedIn pour revue :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" --payload-out "07 Automation/Exports/linkedin_payload_preview.json"
```

Publier rÃ©ellement :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" --publish
```
Note author URN :

- Pour publier comme membre LinkedIn, `linkedin_person_urn.txt` doit contenir une valeur de type `urn:li:person:...`.
- Si le fichier contient une URN d'organisation ou de company, le dry-run fonctionne, mais la publication rÃ©elle est bloquÃ©e par dÃ©faut.
- Pour publier comme organisation, il faut confirmer que l'application LinkedIn et le token disposent des permissions adaptÃ©es, puis utiliser `--allow-non-person-author` en plus de `--publish`.

## PrioritÃ© d'implÃ©mentation

1. LinkedIn texte + lien article.
2. Facebook Page texte + lien.
3. YouTube metadata + upload vidÃ©o quand les vidÃ©os seront prÃªtes.
4. TikTok upload vidÃ©o quand les accÃ¨s API sont validÃ©s.
5. Instagram carousel quand les visuels carrÃ©s seront gÃ©nÃ©rÃ©s.
## LinkedIn page publishing

Script : `publish_linkedin_text.py`

Publication dry-run :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md"
```

Vérification non secrète du token :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --check-token
```

Publication réelle :

```powershell
python "07 Automation/Scripts/social_publishers/publish_linkedin_text.py" "03 Content/Social Media/Huawei/HCIA-Datacom/2026-07-11-data-communication-network/linkedin-post.md" --publish
```

Pour publier comme page/organisation TianSemi, le token doit inclure `w_organization_social`. Le scope `w_member_social` publie seulement comme profil membre.

