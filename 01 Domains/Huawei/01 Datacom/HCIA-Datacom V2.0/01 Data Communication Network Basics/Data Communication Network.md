---
id: HUA-HCIA-DC-001
title: "Data Communication Network"
category: "Huawei HCIA-Datacom Topic"
domain: "Datacom"
vendor: "Huawei"
certification: "HCIA-Datacom"
version: "V2.0"
difficulty: "beginner"
status: "draft"
author: "MOULO OHOLO Jean Noel"
reviewed: false
created: 2026-07-06
updated: 2026-07-11
module: "01 Data Communication Network Basics"
type: "topic"
source: "Training Material"
lab_required: true
source_material:
  - "HCIA-Datacom V2.0 Training Material.pdf"
source_lab:
  - "HCIA-Datacom V2.0 Lab Guide.pdf"
official_source:
  - "https://e.huawei.com/en/talent/cert/#/careerCert"
tags:
  - huawei
  - hcia
  - datacom
keywords:
  - data communication network
  - enterprise network
  - carrier network
  - lan
  - man
  - wan
prerequisites: []
related:
  - "[[Data Communication Network Devices]]"
  - "[[Data Communication Process]]"
  - "[[Network Reference Models]]"
  - "[[Huawei Network Device Operating Systems]]"
commands:
  - display version
  - display device
  - display interface brief
  - display ip interface brief
labs:
  - "Dessiner la topologie d'un petit réseau d'entreprise"
  - "Identifier le rôle de chaque équipement dans une topologie campus"
assets:
  - "04 Assets/Diagrams/Huawei/HCIA-Datacom V2.0"
blog: "03 Content/Blog/Exported/hcia-datacom-comprendre-reseaux-communication-donnees.md"
publication_status: "generated"
site_url: "https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees"
---

# Data Communication Network

## Résumé

> Un data communication network est un réseau qui permet à des terminaux, serveurs et équipements réseau d'échanger des données.
> Toute communication implique au minimum une source, un canal de transmission et une destination.
> En HCIA-Datacom, ce sujet sert de base pour comprendre les équipements Huawei, les topologies LAN/MAN/WAN et les réseaux d'entreprise.
> L'objectif pratique est de savoir lire une topologie, identifier le rôle des équipements et commencer un diagnostic simple.

---

## Objectifs officiels couverts

- Comprendre ce qu'est un réseau de communication de données.
- Identifier les types d'équipements réseau et leurs fonctions de base.
- Expliquer le processus général d'échange de données entre une source et une destination.
- Différencier les grandes portées de réseau : LAN, MAN et WAN.
- Distinguer un réseau d'entreprise d'un réseau opérateur.
- Relier la théorie à une première pratique d'observation sur équipement Huawei VRP.

---

## Explication simple

Un **data communication network** est un ensemble d'équipements connectés qui transportent des données d'un point à un autre. Par exemple, lorsqu'un PC ouvre une page web interne de l'entreprise, la donnée part du PC, traverse un switch, éventuellement un routeur ou un firewall, puis arrive au serveur.

Une communication peut être résumée avec trois éléments :

| Élément | Rôle | Exemple |
| ------- | ---- | ------- |
| Source | Équipement qui envoie les données. | PC, smartphone, caméra IP, serveur |
| Channel | Support ou chemin utilisé pour transporter les données. | Câble Ethernet, fibre, Wi-Fi, réseau opérateur |
| Destination | Équipement qui reçoit les données. | Serveur, imprimante, application, autre PC |

La source et la destination dépendent du sens de l'échange. Quand un PC demande une page web, le PC est la source et le serveur est la destination. Quand le serveur répond, le serveur devient la source et le PC devient la destination.

L'idée clé : un réseau ne sert pas seulement à "connecter des câbles". Il sert à transporter une information de manière fiable, contrôlée et exploitable.

---

## Détails techniques

### Équipements courants

| Équipement | Rôle principal | Exemple dans un réseau campus |
| ---------- | -------------- | ----------------------------- |
| Terminal | Produit ou consomme les données. | PC étudiant, smartphone, imprimante, caméra |
| Switch | Connecte les équipements dans un LAN et transfère les trames selon les adresses MAC. | Switch d'accès dans une salle de cours |
| Router | Relie plusieurs réseaux IP et choisit un chemin vers la destination. | Routeur vers Internet ou vers un autre site |
| Firewall | Filtre et sécurise les flux selon des règles. | Pare-feu entre le LAN et Internet |
| AP | Fournit l'accès Wi-Fi aux terminaux sans fil. | Access Point dans un bâtiment |
| WAC | Centralise la gestion de plusieurs AP. | Wireless Access Controller du campus |
| Server | Fournit un service aux utilisateurs. | Serveur web, DNS, DHCP, fichiers |

Dans une petite topologie, les fonctions routeur et firewall peuvent être dans deux équipements séparés ou dans un même équipement intégré. Pour raisonner proprement, il faut distinguer le rôle de routage, qui choisit un chemin IP, et le rôle de sécurité, qui autorise ou bloque les flux.

### LAN, MAN et WAN

| Type | Portée | Exemple |
| ---- | ------ | ------- |
| LAN | Réseau local dans un bâtiment, une salle ou un campus proche. | Réseau d'une école ou d'un bureau |
| MAN | Réseau métropolitain couvrant une ville ou une zone urbaine. | Interconnexion de plusieurs sites dans une ville |
| WAN | Réseau étendu entre villes, pays ou continents. | Connexion entre filiales via opérateur |

Dans la pratique quotidienne, on parle très souvent de LAN et de WAN. Le terme MAN apparaît moins souvent dans les petites entreprises, mais il reste important pour comprendre les réseaux à l'échelle d'une ville ou d'une zone métropolitaine.

### Enterprise network vs carrier network

Un **enterprise network** est construit pour les besoins internes d'une organisation : utilisateurs, serveurs, Wi-Fi, sécurité, accès Internet, applications métier.

Un **carrier network** est construit par un opérateur pour transporter les données de nombreux clients. Il doit gérer une grande échelle, des liens longue distance, de la redondance forte et des services réseau fournis à plusieurs entreprises.

Pour l'examen HCIA-Datacom, la différence importante est l'objectif :

- réseau d'entreprise : connecter et sécuriser les utilisateurs d'une organisation ;
- réseau opérateur : transporter et fournir des services de connectivité à grande échelle.

---

## À retenir pour l’examen HCIA

- Une communication réseau contient toujours une source, un canal et une destination.
- Un terminal envoie ou reçoit les données ; un switch, un routeur, un firewall, un AP ou un WAC aide à transporter, contrôler ou sécuriser ces données.
- Un LAN couvre une zone locale ; un MAN couvre une zone métropolitaine ; un WAN couvre une grande distance.
- Le switch est central dans le LAN ; le routeur est central pour relier plusieurs réseaux IP ; le firewall est central pour le contrôle de sécurité.
- Dans un dépannage débutant, il faut identifier où se trouve l'utilisateur, par quel équipement il passe, puis vérifier l'état physique et logique du chemin.

---

## Commandes Huawei utiles

Le concept de data communication network est théorique, mais un ingénieur doit rapidement savoir observer un équipement Huawei. Ces commandes servent à découvrir l'état général d'un appareil, pas à configurer le concept lui-même.

Selon le modèle d'équipement, la version VRP et le contexte de lab, certaines sorties peuvent varier. L'objectif HCIA ici est de savoir quoi observer : version système, matériel détecté, état des interfaces et interfaces IP.

```bash
display version
display device
display interface brief
display ip interface brief
```

| Commande | Utilité pratique |
| -------- | ---------------- |
| `display version` | Voir la version VRP, le modèle logiciel et des informations système. |
| `display device` | Vérifier les composants détectés par l'équipement, surtout sur routeurs ou châssis compatibles. |
| `display interface brief` | Observer rapidement les interfaces et leur état physique/logique. |
| `display ip interface brief` | Vérifier les interfaces IP, leurs adresses et leur état. |

---

## Pratique obligatoire

### Objectif

Savoir représenter un petit réseau d'entreprise et expliquer le rôle de chaque équipement.

### Topologie

Topologie logique à dessiner :

```text
PC utilisateur ---- Switch d'accès ---- Router ---- Firewall ---- Internet
                         |
                       Server
                         |
                        WAC ---- AP ---- Smartphone
```

### Étapes

1. Dessiner la topologie d'un petit réseau d'entreprise.
2. Placer au minimum : PC, switch, routeur, firewall, AP, WAC et serveur.
3. Ajouter les liens : câble Ethernet, liaison vers Internet et accès Wi-Fi.
4. Annoter le rôle de chaque équipement.
5. Identifier la source, le channel et la destination pour deux scénarios :
   - un PC accède au serveur interne ;
   - un smartphone accède à Internet via Wi-Fi.

### Vérification

- Chaque équipement a un rôle clair.
- Le chemin des données est visible.
- Les équipements de sécurité et d'accès ne sont pas confondus.
- La topologie distingue LAN, accès Wi-Fi et sortie WAN/Internet.

### Résultat attendu

L'apprenant doit pouvoir expliquer oralement le chemin suivi par une donnée et dire quel équipement vérifier en premier si un utilisateur n'accède pas au réseau.

---

## Troubleshooting

| Symptôme | Cause probable | Vérification | Correction |
| -------- | -------------- | ------------ | ---------- |
| Un utilisateur n'accède pas au réseau | Câble débranché, Wi-Fi non associé, port down | Vérifier le terminal, le câble ou l'association Wi-Fi, puis l'interface côté switch ou AP | Reconnecter le câble, activer le Wi-Fi, corriger le port ou déplacer le test sur un autre port |
| Le terminal est connecté mais ne joint pas le serveur | Mauvais VLAN, mauvaise adresse IP ou passerelle absente | Vérifier l'adresse IP du terminal et `display ip interface brief` sur la passerelle | Corriger l'adressage, le VLAN ou la passerelle |
| Plusieurs utilisateurs d'un même switch sont impactés | Problème sur le switch d'accès ou son uplink | Vérifier les interfaces du switch avec `display interface brief` | Rétablir l'uplink, remplacer le câble ou corriger la configuration |
| Les utilisateurs Wi-Fi ne se connectent pas | AP hors ligne ou problème WAC | Vérifier l'alimentation AP, la liaison AP-switch et l'état côté contrôleur | Rétablir l'AP, vérifier le switch d'accès ou l'association au WAC |
| L'accès Internet ne fonctionne pas mais le LAN répond | Routeur, firewall ou lien WAN en cause | Vérifier le routeur/firewall et le lien de sortie | Corriger la route, la règle de sécurité ou escalader vers l'opérateur |

Question clé : **un utilisateur n'accède pas au réseau, quel équipement vérifier en premier ?**  
Réponse pratique : commencer par le terminal et le point d'accès immédiat au réseau, c'est-à-dire le câble/port switch pour un poste filaire, ou l'AP/association Wi-Fi pour un terminal sans fil. Ensuite seulement, remonter vers le switch d'accès, la passerelle, le firewall, puis les services distants.

---

## Mini-lab TianSemi

### Lab 1 — Dessiner la topologie d’un petit réseau d’entreprise

Objectif : transformer une description métier en schéma réseau simple.

Consigne :

1. Une petite entreprise possède 10 PCs, 1 serveur, 1 accès Internet, 1 réseau Wi-Fi et 1 firewall.
2. Dessiner une topologie logique.
3. Placer les rôles : terminal, switch, router, firewall, AP, WAC, server.
4. Marquer en couleur :
   - source ;
   - channel ;
   - destination.

Livrable attendu : un schéma dans `04 Assets/Diagrams/Huawei/HCIA-Datacom V2.0`.

### Lab 2 — Identifier le rôle de chaque équipement dans une topologie campus

Objectif : lire une topologie campus et expliquer le rôle des équipements.

Consigne :

1. Prendre une topologie avec utilisateurs filaires, utilisateurs Wi-Fi, switchs d'accès, routeur/firewall et serveur.
2. Pour chaque équipement, écrire :
   - rôle ;
   - couche logique approximative ;
   - type de trafic observé ;
   - première vérification en cas de panne.
3. Présenter le diagnostic pour le cas : "un étudiant connecté en Wi-Fi n'accède pas au serveur interne".

---

## Questions d’entretien

1. **Qu'est-ce qu'un data communication network ?**  
   Réponse attendue : un ensemble d'équipements et de supports permettant d'échanger des données entre une source et une destination.

2. **Quels sont les trois éléments de base d'une communication ?**  
   Réponse attendue : source, channel et destination.

3. **Quelle est la différence entre un switch et un routeur ?**  
   Réponse attendue : le switch connecte des équipements dans un LAN ; le routeur relie plusieurs réseaux IP et choisit un chemin.

4. **À quoi sert un firewall dans un réseau d'entreprise ?**  
   Réponse attendue : il contrôle et filtre les flux selon des règles de sécurité.

5. **Quelle est la différence entre un réseau d'entreprise et un réseau opérateur ?**  
   Réponse attendue : le réseau d'entreprise sert une organisation ; le réseau opérateur transporte les services de connectivité pour de nombreux clients.

---

## Quiz

1. **Quel élément représente l'équipement qui envoie les données ?**
   - A. Channel
   - B. Destination
   - C. Source
   - D. Firewall
   - Réponse : C
   - Explication : la source est le point de départ de la communication.

2. **Quel équipement connecte principalement les terminaux dans un LAN ?**
   - A. Switch
   - B. WAC
   - C. Firewall
   - D. Carrier backbone
   - Réponse : A
   - Explication : le switch assure la connectivité locale des terminaux filaires dans un LAN.

3. **Quel type de réseau couvre généralement une grande distance entre plusieurs sites ?**
   - A. LAN
   - B. MAN
   - C. WAN
   - D. PAN
   - Réponse : C
   - Explication : un WAN interconnecte des sites éloignés.

4. **Quel équipement contrôle plusieurs points d'accès Wi-Fi dans une architecture centralisée ?**
   - A. AP
   - B. WAC
   - C. Terminal
   - D. Serveur DNS
   - Réponse : B
   - Explication : le WAC centralise la gestion des AP.

5. **Un PC filaire n'a plus accès au réseau. Quelle vérification est la plus logique en premier ?**
   - A. Vérifier le port et le câble côté switch
   - B. Modifier le routage OSPF
   - C. Redémarrer le serveur web
   - D. Changer l'adresse MAC du firewall
   - Réponse : A
   - Explication : on commence par l'accès immédiat au réseau avant d'accuser les couches plus éloignées.

---

## Flashcards

Q: Qu'est-ce qu'un data communication network ?  
A: Un réseau qui permet à des équipements d'échanger des données entre une source et une destination.

Q: Quels sont les trois éléments de base d'une communication ?  
A: Source, channel et destination.

Q: Quel est le rôle d'un terminal ?  
A: Produire ou consommer les données, comme un PC, un smartphone ou une imprimante.

Q: Quel est le rôle d'un switch ?  
A: Connecter les équipements d'un LAN et transférer les trames localement.

Q: Quel est le rôle d'un routeur ?  
A: Relier plusieurs réseaux IP et choisir un chemin vers la destination.

Q: Quel est le rôle d'un firewall ?  
A: Filtrer et sécuriser les flux réseau.

Q: Quel est le rôle d'un AP ?  
A: Fournir l'accès Wi-Fi aux terminaux sans fil.

Q: Quel est le rôle d'un WAC ?  
A: Centraliser la gestion de plusieurs points d'accès Wi-Fi.

Q: Quelle est la différence entre LAN et WAN ?  
A: Un LAN couvre une zone locale ; un WAN couvre une grande distance.

Q: La source et la destination sont-elles toujours fixes ?  
A: Non. Elles dépendent du sens de l'échange : un serveur peut être destination pendant une requête puis source pendant la réponse.

Q: Quelle commande Huawei donne une vue rapide des interfaces ?  
A: `display interface brief`.

---

## Références

* HCIA-Datacom V2.0 Training Material
* HCIA-Datacom V2.0 Lab Guide
* Huawei Talent Certification page

---

## Contenus générés

| Canal         | Statut    | Lien |
| ------------- | --------- | ---- |
| Site TianSemi | Généré | 03 Content/Blog/Exported/hcia-datacom-comprendre-reseaux-communication-donnees.md |
| Quiz          | À générer |      |

