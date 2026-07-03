---
id: NET-CISCO-001
title: "OSI Model"
aliases: []
category: "Technical Topic"
domain: "Networking"
vendor: "Cisco"
difficulty: "beginner"
ccna: true
ccnp: false
hcip: false
exam: "CCNA 200-301"
status: "reviewed"
author: "MOULO OHOLO Jean Noel"
reviewed: true
last_review: 2026-07-03
created: 2026-07-03
updated: 2026-07-03
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
publication_status: "reviewed"
---

# OSI Model

## Résumé

> Le modèle OSI est un cadre de référence en sept couches qui décrit comment les données circulent d'une application jusqu'au support réseau.

---

## Définition

Le modèle OSI est un cadre de référence en sept couches qui décrit comment les données circulent d'une application jusqu'au support réseau.

---

## Pourquoi c'est important ?

Ce concept sert de base pour diagnostiquer, concevoir et expliquer les communications réseau. Il permet de relier la théorie CCNA aux commandes, aux captures Wireshark et aux labs.

---

## Objectif pédagogique

À la fin de cette note, l'apprenant doit pouvoir expliquer OSI Model, identifier son rôle dans une communication réseau et reconnaître les erreurs fréquentes associées.

---

## Fonctionnement

1. Identifier le contexte réseau.
2. Repérer la couche ou le mécanisme concerné.
3. Observer les informations transportées dans les en-têtes.
4. Vérifier le comportement avec des commandes ou une capture.

---

## Concepts clés

- [[Encapsulation]]
- [[PDU]]
- [[TCP-IP Model]]

---

## Architecture

À compléter avec un schéma dans [[04 Assets/Diagrams]].

---

## Exemple concret

Dans un LAN, un poste qui contacte une passerelle utilise plusieurs mécanismes liés : adressage logique, adresse MAC, encapsulation, puis transmission Ethernet.

---

## Cisco CLI

```bash
show ip interface brief
show running-config
show interfaces
```

---

## Huawei CLI

```bash
display ip interface brief
display current-configuration
display interface
```

---

## Wireshark

Filtrer les trames ou paquets liés au concept, observer les champs d'en-tête, puis comparer avec la configuration de l'équipement.

---

## Troubleshooting

| Problème | Cause probable | Solution |
| -------- | -------------- | -------- |
| Communication impossible | Mauvais adressage ou mauvais domaine réseau | Vérifier IP, masque, passerelle et VLAN |
| Information incohérente | Mauvaise couche analysée | Revenir au modèle OSI et isoler la couche concernée |

---

## Bonnes pratiques

- Toujours partir du modèle OSI pour structurer l'analyse.
- Valider avec une commande et une capture lorsque possible.
- Documenter les hypothèses avant de modifier la configuration.

---

## Erreurs fréquentes

- Confondre adresse MAC et adresse IP.
- Mélanger couche liaison et couche réseau.
- Oublier l'impact du VLAN ou de la passerelle par défaut.

---

## Questions d'entretien

- Peux-tu expliquer OSI Model avec un exemple simple ?
- À quelle couche OSI ce concept est-il principalement associé ?
- Quelle commande utiliserais-tu pour commencer le diagnostic ?

---

## Quiz

1. Quel est le rôle principal de OSI Model ?
   - Réponse : expliquer ou assurer une partie précise de la communication réseau selon son niveau.

---

## Flashcards

Q: Qu'est-ce que OSI Model ?
A: Le modèle OSI est un cadre de référence en sept couches qui décrit comment les données circulent d'une application jusqu'au support réseau.

---

## Labs

Créer un petit lab Packet Tracer avec deux hôtes, un switch et un routeur, puis vérifier le comportement associé à OSI Model.

---

## Références

- Cisco CCNA 200-301 Official Cert Guide.
- Documentation Cisco officielle à ajouter lors de la revue finale.

---

## Contenus générés

| Canal         | Statut     | Lien |
| ------------- | ---------- | ---- |
| Site TianSemi | À générer  |      |
| Blog          | À générer  |      |
| LinkedIn      | À générer  |      |
| Facebook      | À générer  |      |
| Instagram     | À générer  |      |
| TikTok        | À générer  |      |
| YouTube       | À générer  |      |
| Newsletter    | À générer  |      |
