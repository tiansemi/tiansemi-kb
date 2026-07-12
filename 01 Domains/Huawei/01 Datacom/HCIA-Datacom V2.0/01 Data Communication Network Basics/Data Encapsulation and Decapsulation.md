---
id: HUA-HCIA-DC-006
title: "Data Encapsulation and Decapsulation"
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
  - encapsulation
  - decapsulation
  - pdu
keywords:
  - data
  - segment
  - packet
  - frame
  - bitstream
  - header
  - payload
  - FCS
prerequisites:
  - "Data Communication Process"
  - "Network Reference Models"
related:
  - "Ethernet Switching Basics"
  - "IP Address and Configuration"
  - "Huawei Network Device Operating Systems"
commands:
  - "display interface brief"
  - "display mac-address"
  - "display arp"
  - "display ip interface brief"
  - "display ip routing-table"
  - "ping"
  - "tracert"
labs:
  - "01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Data Encapsulation and Decapsulation

## Résumé

> L'encapsulation ajoute, couche après couche, les informations nécessaires au transport d'une donnée. Une donnée applicative devient un segment après l'ajout des informations de transport, un paquet après l'ajout de l'en-tête IP, une trame après l'ajout de l'en-tête Ethernet et du FCS, puis un flux de bits sur le média. À la destination, la décapsulation réalise le chemin inverse et remet la donnée à la bonne application.

---

## Objectifs officiels couverts

Cette note couvre les objectifs Huawei liés à l'encapsulation et à la décapsulation :

- expliquer le passage des données dans les couches du modèle TCP/IP équivalent ;
- nommer les PDU à chaque couche ;
- distinguer header, payload et trailer ;
- comprendre le rôle des ports TCP, des adresses IP, des informations Ethernet et du FCS ;
- décrire l'encapsulation côté émetteur et la décapsulation côté récepteur ;
- relier les informations de chaque couche aux équipements qui les utilisent ;
- utiliser ce chemin pour structurer un troubleshooting de bout en bout.

---

## Explication simple

Envoyer des données revient à placer un message dans plusieurs enveloppes adaptées à chaque étape du trajet.

Le navigateur produit une donnée. TCP ajoute des informations permettant d'identifier les applications et de gérer le transport. IP ajoute les adresses logiques utiles au routage. Ethernet ajoute les informations nécessaires à la livraison sur le lien local et un contrôle FCS. La couche physique convertit ensuite l'ensemble en bits et en signaux.

```text
Donnée applicative
    -> [En-tête TCP | Donnée]                         = Segment
        -> [En-tête IP | Segment]                    = Paquet
            -> [En-tête Ethernet | Paquet | FCS]     = Trame
                -> 0 1 1 0 1 ...                     = Flux de bits
```

Le serveur récepteur effectue l'opération inverse. Chaque couche lit les informations qui lui sont destinées, retire son encapsulation et remet le payload à la couche supérieure.

---

## Détails techniques

### Vocabulaire essentiel

| Terme | Définition pratique |
| --- | --- |
| Data | information produite ou consommée par une application |
| Payload | contenu utile transporté par une PDU ; il peut contenir la PDU de la couche supérieure |
| Header | informations ajoutées avant le payload |
| Trailer | informations ajoutées après le payload |
| PDU | unité de données propre à une couche ou à un protocole |
| Encapsulation | ajout des informations de contrôle pendant la descente de la pile |
| Decapsulation | lecture et retrait progressif de ces informations pendant la remontée de la pile |
| FCS | champ de contrôle placé à la fin d'une trame Ethernet pour détecter certaines erreurs de transmission |

### Les PDU dans le modèle à cinq couches

| Couche | Traitement principal | PDU présentée dans le cours |
| --- | --- | --- |
| Application | crée et interprète le contenu applicatif | Data |
| Transport | ajoute notamment les ports et les fonctions TCP/UDP | Segment pour l'exemple TCP |
| Réseau | ajoute l'adressage IP et les informations d'acheminement | Packet |
| Liaison de données | ajoute les informations du lien local et le FCS Ethernet | Frame |
| Physique | transmet les bits sous forme de signaux | Bitstream |

### Encapsulation côté émetteur

Le support Huawei illustre le processus avec un navigateur qui accède à un site web.

#### 1. Couche application

Le navigateur utilise HTTP pour formuler une requête. La donnée applicative inclut en réalité les informations HTTP, même si le schéma simplifié ne montre pas tout le détail de l'en-tête applicatif.

```text
[Données HTTP]
```

#### 2. Couche transport

HTTP s'appuie ici sur TCP. Le module TCP ajoute un en-tête contenant notamment les ports source et destination. La PDU est appelée segment.

```text
[En-tête TCP | Données HTTP]
```

Le port de destination identifie le service attendu sur le serveur ; le port source aide à identifier la conversation côté client.

#### 3. Couche réseau

Le module IPv4 ou IPv6 ajoute son en-tête. Il contient notamment les adresses IP source et destination. La PDU devient un paquet.

```text
[En-tête IP | En-tête TCP | Données HTTP]
```

Les routeurs utilisent principalement les informations IP pour acheminer le paquet vers le réseau de destination.

#### 4. Couche liaison de données

Dans l'exemple Ethernet, la carte réseau ajoute un en-tête Ethernet et un champ FCS en fin de trame.

```text
[En-tête Ethernet | En-tête IP | En-tête TCP | Données HTTP | FCS]
```

Les adresses de liaison servent à la livraison sur le segment local. Le FCS permet au récepteur de détecter une trame altérée ; une trame en erreur n'est pas réparée par Ethernet, elle est rejetée.

#### 5. Couche physique

La trame est convertie en bitstream, puis en signal électrique, optique ou radio selon le média.

### Transmission dans le réseau

À chaque saut routé, l'équipement retire l'encapsulation de liaison reçue, examine le paquet IP, choisit le prochain saut, puis construit une nouvelle trame adaptée au lien suivant.

Conséquences importantes :

- les adresses MAC sont locales au lien et peuvent changer à chaque saut ;
- les adresses IP identifient les extrémités logiques et restent généralement associées à la communication de bout en bout ;
- certains champs IP évoluent pendant le transit, et des fonctions comme NAT peuvent modifier l'adressage ;
- le contenu applicatif ne doit pas être confondu avec les informations d'acheminement ajoutées autour de lui.

### Décapsulation côté récepteur

Le récepteur traite les informations dans l'ordre inverse :

1. la couche physique remet le bitstream à la couche liaison ;
2. la couche liaison vérifie la trame, notamment le FCS, puis retire l'en-tête et le trailer Ethernet ;
3. la couche réseau vérifie que le paquet est destiné localement et retire l'en-tête IP ;
4. la couche transport utilise les ports et l'état de la conversation pour remettre les données à la bonne application ;
5. l'application interprète la requête ou la réponse reçue.

```text
Bitstream
    -> Frame
        -> Packet
            -> Segment
                -> Data applicative
```

### Informations stables et informations locales

| Information | Portée principale | Observation |
| --- | --- | --- |
| Adresse MAC source/destination | lien local | réécrite lors d'un nouveau saut de couche 2 |
| Adresse IP source/destination | communication routée | généralement conservée, hors mécanismes de traduction ou traitement particulier |
| Port source/destination | conversation applicative | identifie les processus de bout en bout |
| FCS Ethernet | une trame sur un lien | recalculé pour chaque nouvelle trame |

---

## À retenir pour l'examen HCIA

- La donnée descend la pile chez l'émetteur et remonte la pile chez le récepteur.
- Chaque couche traite son propre header et considère la PDU supérieure comme payload.
- Dans le modèle du cours : data, segment, packet, frame, bitstream.
- TCP ajoute notamment les numéros de port ; IP ajoute les adresses logiques ; Ethernet ajoute un en-tête de liaison et un FCS.
- Le FCS est un mécanisme de détection d'erreur de trame, pas une garantie de livraison de bout en bout.
- Les routeurs remplacent l'encapsulation de liaison pour le lien suivant tout en acheminant le paquet IP.
- Les adresses MAC ont une portée locale au segment ; les adresses IP permettent l'acheminement entre réseaux.
- Une panne peut être localisée en vérifiant les informations de chaque couche dans l'ordre.

---

## Commandes Huawei utiles

Les commandes ne montrent pas toutes les étapes d'encapsulation dans un seul écran. Elles exposent les tables et états utilisés par les couches.

| Commande | Information observée | Lien avec l'encapsulation |
| --- | --- | --- |
| `display interface brief` | état du support et du protocole de ligne | la trame peut-elle être transmise sur l'interface ? |
| `display mac-address` | adresses MAC apprises | comment la trame est-elle transférée dans le LAN ? |
| `display arp` | association IP/MAC du prochain voisin | quelle adresse de liaison encapsulera le paquet localement ? |
| `display ip interface brief` | adresses IP des interfaces | quelles adresses de couche réseau sont configurées ? |
| `display ip routing-table` | routes et prochains sauts | vers quel lien le paquet sera-t-il envoyé ? |
| `ping <adresse>` | réponses ICMP | le chemin IP aller-retour fonctionne-t-il ? |
| `tracert <adresse>` | sauts successifs | jusqu'où le paquet progresse-t-il ? |

---

## Pratique obligatoire

### Objectif

Construire manuellement les PDU d'une requête web, puis identifier les informations qui changent à un saut routé.

### Topologie

```text
PC-A ---- S1 ---- R1 ---- S2 ---- Serveur-B
```

### Données de départ

- PC-A : adresse IP et adresse MAC à définir dans le lab ;
- R1 : une interface dans chaque réseau ;
- Serveur-B : service web actif ;
- protocole applicatif : HTTP ;
- protocole de transport : TCP ;
- protocole de réseau : IPv4 ;
- protocole de liaison : Ethernet.

### Étapes

1. Écrire la donnée applicative simplifiée : `GET /`.
2. Ajouter les ports TCP source et destination.
3. Ajouter les adresses IP source et destination.
4. Ajouter les adresses MAC utilisées entre PC-A et R1.
5. Ajouter le FCS comme champ conceptuel de fin de trame.
6. Représenter la trame reçue puis réémise par R1.
7. Identifier les champs qui restent identiques et ceux qui changent.
8. Associer une commande Huawei à chaque information vérifiable.

### Vérification

```text
display interface brief
display mac-address
display arp
display ip interface brief
display ip routing-table
ping <adresse-serveur>
tracert <adresse-serveur>
```

### Résultat attendu

L'apprenant doit produire deux schémas :

- l'encapsulation complète sur le premier lien ;
- la nouvelle trame construite après le routage par R1.

Il doit expliquer que le paquet IP devient le payload de la nouvelle trame de liaison.

---

## Troubleshooting

| Symptôme | Couche ou information suspecte | Vérification | Correction |
| --- | --- | --- | --- |
| Aucune transmission sur le lien | physique ou interface | `display interface brief` | corriger câble, transceiver ou état administratif |
| Le switch ne livre pas la trame correctement | adresse MAC ou VLAN | `display mac-address` | corriger port, VLAN ou apprentissage |
| La passerelle ne peut pas être encapsulée en Ethernet | résolution ARP absente | `display arp` et adressage local | corriger masque, IP ou voisin |
| Le routeur ne sait pas où envoyer le paquet | route absente | `display ip routing-table` | ajouter ou corriger le chemin de routage |
| Le paquet atteint le serveur mais pas le service | port ou application indisponible | vérifier le service et son port | démarrer ou corriger le service |
| Erreurs ou pertes sur une interface | support dégradé | afficher les compteurs détaillés de l'interface | corriger le média ou la négociation |

### Lecture par enveloppes

Lorsqu'une communication échoue, poser les questions dans cet ordre :

1. Le bitstream peut-il traverser le support ?
2. La trame possède-t-elle une destination locale atteignable ?
3. Le paquet possède-t-il un chemin IP ?
4. Le segment vise-t-il le bon service ?
5. L'application comprend-elle les données ?

---

## Mini-lab TianSemi

### Titre

Observer l'encapsulation d'un ping à travers un routeur.

### Matériel

- deux réseaux IP reliés par un routeur Huawei ;
- un terminal dans chaque réseau ;
- un switch par réseau si nécessaire ;
- facultatif : un outil de capture sur un terminal.

### Travail demandé

1. Vérifier les interfaces et les routes avant le test.
2. Vider uniquement les observations de la fiche, sans modifier la configuration.
3. Lancer un `ping` du terminal A vers le terminal B.
4. Relever les associations ARP et les adresses MAC apprises.
5. Dessiner la trame du premier lien et celle du second lien.
6. Expliquer pourquoi les adresses MAC diffèrent tandis que les adresses IP représentent toujours les extrémités de la communication.

### Questions de validation

- Quel protocole de réseau transporte ICMP ?
- Quelle information permet au routeur de choisir le prochain saut ?
- Pourquoi le FCS n'est-il pas identique sur deux trames différentes ?
- Quelle couche remet finalement la réponse au programme `ping` ?

---

## Questions d'entretien

1. Décrivez l'encapsulation d'une requête HTTP.
2. Quelle différence existe entre payload, header et trailer ?
3. Pourquoi un paquet IP est-il encapsulé dans une trame Ethernet ?
4. Quelles informations sont utilisées par un switch et par un routeur ?
5. Pourquoi les adresses MAC changent-elles lors d'un passage par un routeur ?
6. À quoi sert le FCS Ethernet ?
7. Quelle différence existe entre encapsulation et décapsulation ?
8. Comment utilisez-vous les PDU pour diagnostiquer une panne ?

---

## Quiz

### 1. Quelle PDU est produite après l'ajout de l'en-tête TCP dans l'exemple du cours ?

- A. Frame
- B. Segment
- C. Bitstream
D. Route

**Réponse : B.**

### 2. Quelle information est ajoutée principalement par la couche réseau ?

- A. Les adresses IP
- B. Le FCS Ethernet uniquement
- C. Le signal optique
D. Le nom du fichier de configuration

**Réponse : A.**

### 3. Où se trouve le FCS dans une trame Ethernet ?

- A. Avant tous les headers
- B. Dans le trailer de la trame
- C. Dans l'adresse IP
D. Dans le port TCP

**Réponse : B.**

### 4. Quelle PDU est transmise par la couche physique ?

- A. Bitstream
- B. Segment uniquement
- C. Table de routage
D. Session CLI

**Réponse : A.**

### 5. Que fait la décapsulation ?

- A. Ajoute toutes les couches à la source
- B. Retire progressivement les informations de couche à la destination
- C. Efface les routes
D. Remplace l'application

**Réponse : B.**

### 6. Quelle information change normalement à chaque saut routé ?

- A. Les adresses MAC de la trame
- B. Le contenu applicatif complet
- C. Le nom de l'utilisateur
D. Le modèle OSI

**Réponse : A.**

### 7. Quelle commande aide à trouver l'adresse MAC du prochain voisin IP ?

- A. `save`
- B. `display arp`
- C. `reboot`
D. `sysname`

**Réponse : B.**

### 8. Le FCS garantit-il la livraison de bout en bout ?

- A. Oui
- B. Non, il sert à détecter certaines erreurs de trame sur un lien
- C. Il remplace TCP
D. Il remplace le routage

**Réponse : B.**

---

## Flashcards

**Q : Qu'est-ce que l'encapsulation ?**

R : L'ajout progressif de headers et parfois d'un trailer pendant la descente des couches.

**Q : Qu'est-ce que la décapsulation ?**

R : Le retrait progressif des informations de couche pour remettre la donnée à l'application.

**Q : Quelle est la PDU de la couche transport dans l'exemple TCP ?**

R : Le segment.

**Q : Quelle est la PDU de la couche réseau ?**

R : Le packet.

**Q : Quelle est la PDU de la couche liaison ?**

R : La frame.

**Q : Quelle est la PDU de la couche physique ?**

R : Le bitstream.

**Q : Que contient principalement un en-tête TCP pour identifier les applications ?**

R : Des numéros de port source et destination.

**Q : Que contient l'en-tête IP pour l'acheminement ?**

R : Notamment les adresses IP source et destination.

**Q : À quoi sert le FCS ?**

R : À détecter certaines erreurs dans une trame Ethernet reçue.

**Q : Pourquoi une nouvelle trame est-elle créée après un routage ?**

R : Parce que l'encapsulation de liaison est propre au lien et au prochain voisin.

---

## Références

- HCIA-Datacom V2.0 Training Material, section « Data Encapsulation and Decapsulation », pages PDF 80-86.
- HCIA-Datacom V2.0 Training Material, chapitre « Network Reference Models », pages PDF 46-79 pour le modèle à cinq couches et les protocoles utilisés par l'exemple.
- HCIA-Datacom V2.0 Lab Guide, lab « Basic Operations on Huawei Network Devices », pages PDF 14-25 pour les commandes de base utilisées dans le mini-lab.
- Huawei Talent Certification page : https://e.huawei.com/en/talent/cert/#/careerCert

---

## Contenus générés

| Canal | Statut | Lien |
| --- | --- | --- |
| Site TianSemi | À générer | |
| Quiz | Intégré à la note | |
