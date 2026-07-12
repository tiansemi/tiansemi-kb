---
id: HUA-HCIA-DC-002
title: "Data Communication Network Devices"
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
updated: 2026-07-12
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
  - network-devices
keywords:
  - switch
  - router
  - firewall
  - access point
  - WAC
  - server
  - modular device
  - fixed device
prerequisites:
  - "Data Communication Network"
related:
  - "Data Communication Process"
  - "Huawei Network Device Operating Systems"
  - "Basic Operations on Huawei Network Devices"
commands:
  - "display version"
  - "display device"
  - "display interface brief"
  - "display ip interface brief"
  - "display current-configuration"
  - "display mac-address"
  - "display arp"
  - "display vlan"
labs:
  - "09 Labs/01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Data Communication Network Devices

## Résumé

Un réseau Datacom ne se résume pas à des câbles et à des adresses IP. Il est construit avec des terminaux, des équipements d'infrastructure et des équipements de sécurité qui coopèrent pour recevoir, traiter et transférer les données.

Dans le cours HCIA-Datacom V2.0, les équipements essentiels à reconnaître sont le switch, le routeur, le firewall, les AP, le WAC et les serveurs. Le point important n'est pas seulement de connaître leur nom, mais de comprendre où ils se placent dans une topologie d'entreprise et quel rôle ils jouent dans le chemin de la donnée.

Cette note sert de base pratique pour apprendre à lire une topologie, identifier les équipements, associer chaque équipement à une fonction, puis choisir les premières commandes Huawei de vérification.

---

## Objectifs officiels couverts

Cette note couvre les objectifs HCIA-Datacom suivants :

- différencier les types d'équipements réseau ;
- comprendre les fonctions de base des équipements Datacom ;
- reconnaître les équipements présents dans un réseau d'entreprise ;
- distinguer le rôle d'un switch, d'un routeur, d'un firewall, d'un AP, d'un WAC et d'un serveur ;
- comprendre la différence entre topologie physique et topologie logique ;
- comprendre la différence entre équipements fixes et équipements modulaires ;
- utiliser des commandes Huawei simples pour observer l'état d'un équipement.

---

## Explication simple

Un réseau d'entreprise peut être vu comme une organisation avec plusieurs rôles.

- Les **terminaux** produisent ou consomment les données : PC, téléphones, imprimantes, terminaux Wi-Fi.
- Les **switches d'accès** connectent les utilisateurs au réseau local.
- Les **switches cœur** agrègent le trafic et assurent l'interconnexion interne du campus.
- Le **routeur** choisit le chemin IP vers un autre réseau, un WAN ou Internet.
- Le **firewall** contrôle et sécurise les flux entre des zones de confiance différentes.
- Les **AP** fournissent l'accès Wi-Fi aux terminaux sans fil.
- Le **WAC** centralise la gestion de nombreux AP, surtout dans les scénarios Fit AP.
- Les **serveurs** fournissent les services : applications, fichiers, DNS, DHCP, authentification, stockage.

Dans un scénario de bureau typique, un utilisateur se connecte souvent ainsi :

```text
PC ou téléphone
  -> switch d'accès ou AP
  -> switch cœur
  -> firewall / routeur de sortie
  -> Internet ou serveur distant
```

L'erreur de débutant consiste à dire : "le réseau ne marche pas" sans préciser quel équipement est concerné. Un futur ingénieur Datacom doit plutôt demander : **où se situe la panne dans le chemin ?**

---

## Détails techniques

### Vue d'ensemble des équipements

| Équipement | Rôle principal | Position typique | Ce qu'il faut vérifier en premier |
| ---------- | -------------- | ---------------- | --------------------------------- |
| Terminal | Envoie ou reçoit les données | Poste utilisateur, téléphone, imprimante, caméra | Adresse IP, câble, Wi-Fi, passerelle |
| Switch d'accès | Connecte les terminaux au LAN | Étage, salle, baie d'accès | État des interfaces, VLAN, table MAC |
| Switch cœur | Agrège le trafic du campus | Salle équipements campus | Liens montants, routage/VLAN, disponibilité |
| Routeur | Transporte les paquets entre réseaux IP | Sortie WAN/Internet, interconnexion sites | Table de routage, interfaces IP, reachability |
| Firewall | Filtre et sécurise les flux | Frontière entre zones de sécurité | Politiques, NAT, sessions, interfaces |
| AP | Fournit le signal Wi-Fi | Bureaux, salles, zones ouvertes | Alimentation, association, couverture radio |
| WAC | Gère plusieurs AP de façon centralisée | Agrégation ou cœur réseau | AP en ligne, profils WLAN, tunnel de gestion |
| Serveur | Fournit un service réseau ou applicatif | Data center, salle serveur, cloud privé | Service actif, IP, passerelle, ports ouverts |

### Switch

Le switch est un équipement central dans un LAN. Son rôle principal est de transférer des trames Ethernet en s'appuyant sur les adresses MAC.

Dans un campus, on rencontre souvent :

- des **switches d'accès**, proches des utilisateurs ;
- des **switches cœur**, qui agrègent le trafic de plusieurs zones ;
- des **switches de data center**, conçus pour des besoins de débit, fiabilité et latence élevés.

Le cours Huawei distingue aussi les switches **fixes** et **modulaires** :

- un switch fixe possède un châssis et un nombre de ports relativement déterminés ;
- un switch modulaire reçoit des cartes ou modules spécialisés et convient mieux aux couches cœur ou aux réseaux exigeants.

### Routeur

Le routeur travaille principalement avec l'adresse IP de destination. Il choisit un chemin et transfère les paquets vers le prochain saut ou vers le réseau de destination.

Dans les scénarios HCIA, il faut retenir qu'un routeur peut assurer :

- la maintenance de routes et d'informations de routage ;
- la sélection du meilleur chemin ;
- le transfert de paquets ;
- l'accès WAN ou Internet ;
- parfois du NAT et certaines fonctions de sécurité.

### Firewall

Le firewall est un équipement de sécurité placé entre des zones de confiance différentes. Il observe et contrôle les flux, applique des politiques de sécurité et peut fournir des fonctions comme NAT, VPN, authentification ou chiffrement.

Dans un réseau d'entreprise, il est souvent placé à la sortie du réseau interne, entre le LAN/campus et Internet.

### AP et WAC

Un WLAN permet aux terminaux d'accéder au réseau grâce à des signaux radio. Dans le cours Huawei, les équipements WLAN importants sont :

- **Fat AP** : AP autonome, souvent adapté à de petits environnements ;
- **Fit AP** : AP contrôlé par un WAC, fréquent dans les entreprises moyennes ou grandes ;
- **Cloud AP** : AP géré par une plateforme cloud ;
- **WAC** : contrôleur qui gère, configure et supervise plusieurs AP.

Le scénario courant en entreprise est **Fit AP + WAC** : les AP diffusent le Wi-Fi, tandis que le WAC centralise la gestion.

### Serveurs et data center

Les serveurs fournissent les services utilisés par les utilisateurs et les applications. Dans une entreprise moyenne ou grande, ils peuvent être dans une salle data center séparée, reliée au cœur du campus.

Exemples :

- serveur d'application ;
- serveur de fichiers ;
- serveur DHCP ;
- serveur DNS ;
- plateforme NMS ;
- système de logs.

### Topologie physique et topologie logique

Le cours insiste sur l'importance de savoir dessiner et lire des topologies.

- La **topologie physique** montre les équipements, les ports, les câbles et les connexions réelles.
- La **topologie logique** montre les rôles, les flux, les VLAN, les zones de sécurité, les sous-réseaux ou les chemins de communication.

Dans la pratique, il faut souvent savoir passer de l'une à l'autre : un lien physique existe, mais il faut aussi comprendre quel trafic logique l'emprunte.

### Équipements fixes et modulaires

Les switches, routeurs et firewalls peuvent avoir des architectures fixes ou modulaires.

| Type | Caractéristique | Usage fréquent | Point d'attention |
| ---- | --------------- | -------------- | ----------------- |
| Fixe | Châssis intégré, ports prédéfinis | Accès utilisateur, petit réseau | Capacité d'évolution limitée |
| Modulaire | Châssis avec cartes ou modules | Cœur réseau, campus important, haute disponibilité | Coût, alimentation, ventilation, modules |

Dans les équipements modulaires, on peut rencontrer des cartes ou modules comme :

- **MPU** : contrôle, gestion et supervision du système ;
- **SFU** : échange interne des données entre cartes ;
- **LPU** : traitement des paquets et ports de service ;
- **SPU** : traitement de services avancés ;
- **CMU** : surveillance de l'environnement.

Pour un débutant HCIA, il ne s'agit pas encore de dimensionner un châssis complet, mais de comprendre que tous les équipements ne sont pas construits de la même façon.

---

## À retenir pour l'examen HCIA

- Un réseau Datacom est composé d'équipements terminaux et d'équipements d'infrastructure.
- Un switch transfère des trames dans un LAN grâce aux adresses MAC.
- Un routeur transfère des paquets entre réseaux IP grâce aux routes.
- Un firewall contrôle les flux entre zones de sécurité.
- Un AP fournit l'accès Wi-Fi ; un WAC centralise la gestion de nombreux AP.
- Un serveur fournit un service : application, fichier, DNS, DHCP, logs, supervision.
- Un switch d'accès est proche des utilisateurs ; un switch cœur agrège le trafic.
- Les équipements fixes sont fréquents à l'accès ; les équipements modulaires sont fréquents au cœur.
- Une topologie physique montre les connexions ; une topologie logique montre les rôles et les flux.
- Avant de configurer, il faut identifier l'équipement, son rôle et sa position dans le chemin.

---

## Commandes Huawei utiles

Ces commandes servent ici à **observer** les équipements. Elles ne configurent pas encore le réseau.

```bash
display version
display device
display interface brief
display ip interface brief
display current-configuration
display mac-address
display arp
display vlan
display stp brief
ping
tracert
```

| Commande | Utilité pratique | Quand l'utiliser |
| -------- | ---------------- | ---------------- |
| `display version` | Identifier le modèle, la version VRP et le temps de fonctionnement | Première prise en main d'un équipement |
| `display device` | Observer les cartes, modules ou composants détectés | Vérification d'un châssis ou d'un équipement modulaire |
| `display interface brief` | Voir rapidement les interfaces up/down | Diagnostic physique ou accès utilisateur |
| `display ip interface brief` | Voir les interfaces avec adressage IP | Diagnostic routeur, SVI ou interface L3 |
| `display current-configuration` | Lire la configuration active | Comprendre le rôle configuré d'un équipement |
| `display mac-address` | Observer les adresses MAC apprises | Vérifier si un switch voit un terminal |
| `display arp` | Observer les correspondances IP/MAC | Vérifier la résolution entre couche 2 et couche 3 |
| `display vlan` | Vérifier les VLAN existants | Diagnostic d'accès LAN |
| `display stp brief` | Voir l'état STP des ports | Diagnostic de boucle ou de blocage L2 |
| `ping` | Tester la connectivité IP | Vérifier la reachability |
| `tracert` | Voir le chemin IP suivi | Identifier où un chemin se coupe |

---

## Pratique obligatoire

### Objectif

Identifier les équipements d'une topologie campus et expliquer le rôle de chacun.

### Topologie

Utiliser une topologie papier, draw.io, eNSP ou une capture de scénario avec :

```text
Internet
  |
Routeur
  |
Firewall
  |
Switch cœur
  |---------------- Serveur / NMS / logs
  |
Switch d'accès
  |------ PC câblés
  |------ AP )) terminaux Wi-Fi
  |
WAC connecté au cœur ou à l'agrégation
```

### Étapes

1. Identifier tous les équipements visibles.
2. Classer chaque équipement : terminal, accès, cœur, sécurité, sans-fil, service.
3. Tracer le chemin d'un PC vers Internet.
4. Tracer le chemin d'un téléphone Wi-Fi vers un serveur interne.
5. Indiquer quel équipement vérifie l'accès filaire.
6. Indiquer quel équipement vérifie l'accès Wi-Fi.
7. Indiquer quel équipement applique les règles de sécurité.
8. Associer une commande Huawei d'observation à chaque étape.

### Vérification

| Élément à vérifier | Commande ou action |
| ------------------ | ------------------ |
| Équipement et version | `display version` |
| Modules/cartes détectés | `display device` |
| Ports physiques | `display interface brief` |
| Interfaces IP | `display ip interface brief` |
| Terminal vu par le switch | `display mac-address` |
| Correspondance IP/MAC | `display arp` |
| VLAN utilisateur | `display vlan` |
| Connectivité IP | `ping` |
| Chemin IP | `tracert` |

### Résultat attendu

L'apprenant doit produire :

- un schéma annoté ;
- un tableau des équipements et de leurs rôles ;
- le chemin suivi par deux flux ;
- trois points de panne possibles ;
- une commande de vérification pour chaque point de panne.

---

## Troubleshooting

| Symptôme | Cause probable | Vérification | Correction |
| -------- | -------------- | ------------ | ---------- |
| Un seul PC n'a pas accès au réseau | Câble débranché, port down ou mauvaise configuration du terminal | `display interface brief`, vérifier IP du PC | Rebrancher, changer le port, corriger IP/masque/passerelle |
| Plusieurs PC d'un même étage sont impactés | Switch d'accès ou uplink en panne | Vérifier uplink du switch d'accès | Restaurer le lien, vérifier module/SFP/câble |
| Les utilisateurs Wi-Fi ne se connectent pas | AP hors ligne ou problème WAC | Vérifier alimentation AP, état WAC/AP | Restaurer PoE, lien AP, configuration WLAN |
| Le LAN fonctionne mais Internet est inaccessible | Routeur, firewall ou sortie WAN en cause | `ping`, `tracert`, vérifier route et politique | Corriger route, NAT, politique firewall ou lien WAN |
| Un serveur interne est inaccessible | Serveur down, VLAN/routage/firewall incorrect | Ping serveur, ARP, route, règle de sécurité | Restaurer service ou corriger chemin réseau |
| Un terminal n'apparaît pas sur le switch | Mauvais port, mauvais VLAN ou câble | `display mac-address`, `display vlan` | Corriger port/VLAN/câblage |
| Les performances sont faibles | Uplink saturé ou équipement mal dimensionné | Vérifier interfaces, taux, erreurs | Augmenter capacité, corriger duplex, revoir architecture |

---

## Mini-lab TianSemi

### Titre

Lire une topologie campus et identifier le rôle des équipements.

### Scénario

Une entreprise dispose d'un bureau avec :

- 20 PC câblés ;
- 10 utilisateurs Wi-Fi ;
- 2 AP ;
- 1 switch d'accès ;
- 1 switch cœur ;
- 1 firewall ;
- 1 routeur de sortie ;
- 2 serveurs internes ;
- 1 plateforme NMS.

### Travail demandé

1. Dessiner la topologie physique.
2. Dessiner une topologie logique simplifiée.
3. Identifier les équipements d'accès, de cœur, de sécurité, de routage, sans-fil et de service.
4. Expliquer le chemin d'un PC vers Internet.
5. Expliquer le chemin d'un smartphone Wi-Fi vers un serveur interne.
6. Lister cinq commandes Huawei de vérification.
7. Décrire trois pannes possibles et leur premier équipement à vérifier.

### Critère de réussite

Le mini-lab est réussi si l'apprenant peut expliquer la topologie sans réciter une définition, en reliant chaque équipement à une fonction observable.

---

## Questions d'entretien

1. Quelle est la différence entre un switch et un routeur ?
   - Un switch transfère des trames dans un LAN en s'appuyant sur les adresses MAC ; un routeur transfère des paquets entre réseaux IP en s'appuyant sur une table de routage.

2. Pourquoi place-t-on souvent un firewall à la sortie du réseau d'entreprise ?
   - Pour contrôler les flux entre le réseau interne et les réseaux externes, appliquer des politiques de sécurité, éventuellement NAT/VPN, et réduire l'exposition du réseau interne.

3. Quelle est la différence entre un AP et un WAC ?
   - L'AP fournit l'accès radio aux terminaux Wi-Fi ; le WAC centralise la gestion et la configuration de plusieurs AP, notamment dans un scénario Fit AP.

4. Pourquoi un switch modulaire est-il souvent utilisé au cœur du réseau ?
   - Il offre plus d'évolutivité, de capacité, de redondance et de flexibilité grâce à ses cartes et modules.

5. Que vérifier si un utilisateur filaire ne se connecte pas au réseau ?
   - Le terminal, le câble, le port du switch, l'état de l'interface, le VLAN, l'adresse IP et la passerelle.

6. Pourquoi faut-il distinguer topologie physique et topologie logique ?
   - Parce qu'un câble ou un port ne suffit pas à expliquer les flux : il faut aussi comprendre les VLAN, sous-réseaux, zones de sécurité et chemins logiques.

---

## Quiz

1. Quel équipement transfère principalement des trames dans un LAN ?
   - A. Firewall
   - B. Switch
   - C. Serveur DNS
   - D. WAC
   - Réponse : B. Le switch transfère les trames Ethernet dans un LAN.

2. Quel équipement choisit un chemin en fonction d'une adresse IP de destination ?
   - A. Routeur
   - B. AP
   - C. Imprimante
   - D. Câble optique
   - Réponse : A. Le routeur sélectionne le chemin IP vers le réseau de destination.

3. Quel équipement contrôle les flux entre zones de sécurité ?
   - A. Switch d'accès
   - B. Firewall
   - C. PC utilisateur
   - D. AP
   - Réponse : B. Le firewall applique des politiques de sécurité entre réseaux ou zones.

4. Dans un scénario Fit AP, quel équipement gère les AP de façon centralisée ?
   - A. WAC
   - B. Serveur web
   - C. Routeur WAN
   - D. Imprimante réseau
   - Réponse : A. Le WAC centralise la gestion des Fit AP.

5. Quel type de switch est typiquement plus adapté au cœur d'un grand campus ?
   - A. Switch modulaire
   - B. Petit switch non manageable
   - C. AP autonome
   - D. Terminal utilisateur
   - Réponse : A. Un switch modulaire offre plus de capacité, évolutivité et redondance.

6. Quelle commande Huawei aide à voir rapidement les ports up/down ?
   - A. `display interface brief`
   - B. `display clock`
   - C. `display users`
   - D. `save`
   - Réponse : A. Elle résume l'état des interfaces.

7. Quelle commande permet de vérifier si un switch a appris l'adresse MAC d'un terminal ?
   - A. `display mac-address`
   - B. `display version`
   - C. `display arp`
   - D. `tracert`
   - Réponse : A. Elle affiche les adresses MAC apprises par le switch.

---

## Flashcards

- Q: Quel est le rôle principal d'un switch ?
  A: Transférer des trames dans un LAN, principalement à partir des adresses MAC.

- Q: Quel est le rôle principal d'un routeur ?
  A: Transférer des paquets entre réseaux IP en choisissant un chemin.

- Q: Quel est le rôle principal d'un firewall ?
  A: Contrôler et sécuriser les flux entre des zones de sécurité différentes.

- Q: Que fait un AP ?
  A: Il fournit l'accès Wi-Fi aux terminaux sans fil.

- Q: Que fait un WAC ?
  A: Il centralise la gestion et la configuration de plusieurs AP.

- Q: Quelle est la différence entre Fat AP et Fit AP ?
  A: Un Fat AP fonctionne de manière autonome ; un Fit AP est géré par un WAC.

- Q: Qu'est-ce qu'un switch d'accès ?
  A: Un switch placé près des utilisateurs pour connecter les terminaux au LAN.

- Q: Qu'est-ce qu'un switch cœur ?
  A: Un équipement qui agrège le trafic et interconnecte les différentes zones du campus.

- Q: Pourquoi dessiner une topologie ?
  A: Pour visualiser les équipements, les connexions, les rôles et les chemins de communication.

- Q: Quelle commande vérifie les interfaces up/down ?
  A: `display interface brief`.

- Q: Quelle commande vérifie les modules d'un équipement ?
  A: `display device`.

- Q: Quelle commande vérifie les adresses MAC apprises ?
  A: `display mac-address`.

- Q: Quelle commande vérifie la correspondance IP/MAC ?
  A: `display arp`.

- Q: Où place-t-on souvent le firewall dans un réseau d'entreprise ?
  A: À la frontière entre le réseau interne et le réseau externe, souvent à la sortie Internet.

- Q: Pourquoi les équipements modernes peuvent-ils être difficiles à classer ?
  A: Parce qu'ils intègrent parfois plusieurs fonctions, par exemple switching, routing, sécurité ou wireless.

---

## Références

- HCIA-Datacom V2.0 Training Material, section Data Communication Network et Data Communication Network Devices, pages 4-30.
- HCIA-Datacom V2.0 Lab Guide, Lab 01 - Basic Operations on Huawei Network Devices.
- Huawei Talent Certification page.

---

## Contenus générés

| Canal | Statut | Lien |
| ----- | ------ | ---- |
| Site TianSemi | À générer | |
| Blog | À générer | |
| Quiz | À générer | |
