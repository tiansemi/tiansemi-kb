---
id: HUA-HCIA-DC-001
title: "Data Communication Network"
official_title: "Data Communication Network"
course_unit: "1.1.1"
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
updated: 2026-07-13
source: "HCIA-Datacom V2.0 Training Material"
source_pages: "PDF 1-17"
tags: [huawei, hcia, datacom, network-basics]
prerequisites: []
related:
  - "[[Data Communication Network Devices]]"
  - "[[01 Data Communication Network Basics/Data Communication Process]]"
lab_required: false
publication_status: "generated"
blog: "03 Content/Blog/Exported/hcia-datacom-comprendre-reseaux-communication-donnees.md"
site_url: "https://tiansemi.github.io/apprentissage/reseaux/hcia-datacom-comprendre-reseaux-communication-donnees"
---

# Réseau de communication de données (Data Communication Network)

## Objectif du cours

Cette unité introduit les concepts de communication réseau et de réseau de communication de données. Elle présente les éléments d'une communication, les topologies, les principaux types de réseaux et la distinction entre réseaux d'entreprise et réseaux opérateurs.

## Communication

Huawei définit la communication comme la transmission et l'échange d'informations entre au moins deux points, au moyen d'un média et d'actions déterminées.

Un système de communication comporte trois éléments fondamentaux :

| Élément | Rôle | Exemple du support |
| --- | --- | --- |
| Source | produit et envoie l'information | ordinateur ou téléphone de l'utilisateur |
| Canal | transporte l'information | câble, fibre optique ou onde radio |
| Destination | reçoit l'information | équipement récepteur |

Deux autres notions sont indispensables :

- **information** : contenu à transmettre, par exemple voix, texte, image ou données ;
- **protocole de communication** : ensemble de règles convenues par les deux parties pour coder, transmettre et décoder correctement l'information.

## Évolution des technologies de communication

Le support distingue quatre grandes périodes :

1. **Époque ancienne** : signaux visuels ou sonores et communication postale, avec une faible vitesse et une portée limitée.
2. **Ère électrique** : télégraphe, téléphone et radio rendent possible une communication rapide à longue distance.
3. **Ère de l'information** : transistors, circuits intégrés, informatique, ARPANET, TCP/IP, Internet et générations successives de réseaux mobiles.
4. **Ère de l'Internet of Everything** : approfondissement de la 5G, exploration de la 6G et intégration de l'IoT et de l'intelligence artificielle.

La transition essentielle est le passage d'une communication principalement humaine à des échanges entre humains, machines et réseaux.

## Communication réseau

La communication réseau est la transmission d'informations entre des terminaux au moyen d'un réseau de communication de données.

Huawei illustre trois niveaux de complexité :

- deux ordinateurs reliés directement par un câble ;
- plusieurs ordinateurs reliés par un équipement comme un switch ou un routeur ;
- un terminal accédant à un service distant par Internet.

Internet constitue aujourd'hui le plus grand réseau informatique mondial. Son prédécesseur, ARPANET, est apparu en 1969.

## Réseau de communication de données

Un réseau de communication de données regroupe des équipements et des terminaux : routeurs, switchs, firewalls, WAC, AP, PC, imprimantes réseau et serveurs. Sa fonction fondamentale est de permettre la communication de données.

Dans la suite du cours, Huawei emploie également l'expression abrégée **datacom network**.

## Topologie réseau

Une topologie décrit de manière structurée la connexion des équipements par les médias de transmission. Elle peut représenter la structure physique ou logique du réseau et constitue un outil essentiel de l'ingénierie réseau.

| Topologie | Principe | Avantage principal | Limite principale |
| --- | --- | --- | --- |
| Bus | tous les nœuds partagent un même support | installation simple et peu de câbles | une panne du bus affecte tout le réseau |
| Étoile | tous les nœuds rejoignent un nœud central | ajout de nœuds et supervision facilités | dépendance au nœud central |
| Anneau | les nœuds forment une boucle fermée | quantité de câbles réduite | insertion d'un nouveau nœud contraignante |
| Arbre | organisation hiérarchique de plusieurs étoiles | extension rapide | panne d'un nœud haut placée très impactante |
| Maillage complet | tous les nœuds sont interconnectés | disponibilité et efficacité élevées | coût, ports et câblage importants |
| Maillage partiel | seuls les nœuds essentiels sont interconnectés | compromis de coût | fiabilité inférieure au maillage complet |

Les réseaux réels combinent souvent plusieurs topologies afin d'équilibrer coût, performance et fiabilité.

## Types de réseaux

Huawei utilise deux méthodes courantes de classification.

### Selon la couverture géographique

| Type | Portée et fonction | Technologies ou exemples cités |
| --- | --- | --- |
| LAN | zone limitée, par exemple domicile, bâtiment ou campus | Ethernet, Wi-Fi |
| MAN | interconnexion de sites dans un campus étendu ou une ville | Ethernet haut débit, WiMAX |
| WAN | longues distances entre villes ou pays | PPP, MPLS, SRv6 ; Internet comme scénario typique |

### Selon l'entité qui exploite le réseau

| Type | Définition | Scénarios cités |
| --- | --- | --- |
| Réseau d'entreprise | réseau privé construit et maintenu par une organisation | campus, data center, backbone privé |
| Réseau opérateur | infrastructure publique exploitée par un fournisseur de télécommunications | backbone Internet, réseau mobile, liaisons privées |

Sauf indication contraire, le cours HCIA-Datacom décrit principalement les réseaux d'entreprise.

## Réseau d'entreprise dans un environnement de bureau

Un réseau de bureau relie les équipements et terminaux d'une organisation. Il permet le partage des ressources et l'échange d'informations, et fournit un point d'accès unifié aux services internes et externes. Le schéma Huawei présente notamment des zones de réception, bureaux, salle de réunion et mobilité, reliées par des switchs d'accès et des AP.

## Résumé fidèle du cours

- La communication repose sur une source, un canal et une destination, ainsi que sur une information et un protocole commun.
- Un réseau de communication de données transporte des informations entre des terminaux.
- Les topologies décrivent l'organisation physique ou logique du réseau.
- Les réseaux peuvent être classés par couverture géographique ou par entité d'exploitation.
- Le parcours HCIA-Datacom se concentre principalement sur les réseaux d'entreprise.

## Révision TianSemi

1. Quels sont les trois éléments fondamentaux d'un système de communication ?
2. Quelle différence existe entre LAN, MAN et WAN ?
3. Pourquoi les réseaux réels combinent-ils plusieurs topologies ?
4. Quelle distinction Huawei établit-il entre réseau d'entreprise et réseau opérateur ?

## Références

- Huawei, *HCIA-Datacom V2.0 Training Material*, pages PDF 1-17.
- Huawei Talent, HCIA-Datacom V2.0 : https://e.huawei.com/en/talent/#/cert/product-details?certifiedProductId=1316&authenticationLevel=CTYPE_CARE_HCIA&technicalField=IIC&version=2.0
