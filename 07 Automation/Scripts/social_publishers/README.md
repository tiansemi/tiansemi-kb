# Social Publishers

Ce dossier contiendra les scripts de publication réelle par plateforme.

## Règle de sécurité

- Pas de secret dans Git.
- Les credentials restent dans C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred.
- Les scripts doivent lire les secrets via TSOS_CRED_DIR ou variables d'environnement.
- Toute publication réelle doit exiger un flag explicite --publish.
- Le mode par défaut doit rester dry-run.

## Priorité d'implémentation

1. LinkedIn texte + lien article.
2. Facebook Page texte + lien.
3. YouTube metadata + upload vidéo quand les vidéos seront prêtes.
4. TikTok upload vidéo quand les accès API sont validés.
5. Instagram carousel quand les visuels carrés seront générés.