---
id: HUA-HCIA-DC-003
title: "Data Communication Process"
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
  - data-communication
  - troubleshooting
keywords:
  - data communication process
  - packet
  - data payload
  - header
  - trailer
  - gateway
  - terminal
  - encapsulation
  - decapsulation
prerequisites:
  - "Data Communication Network"
  - "Data Communication Network Devices"
related:
  - "Network Reference Models"
  - "Data Encapsulation and Decapsulation"
  - "Huawei Network Device Operating Systems"
commands:
  - "ping"
  - "tracert"
  - "display version"
  - "display device"
  - "display interface brief"
  - "display ip interface brief"
  - "display arp"
  - "display mac-address"
  - "display ip routing-table"
labs:
  - "01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Data Communication Process

## Résumé

> Un processus de communication de données décrit le trajet complet d'une information depuis une application source jusqu'à une application destination. Dans le cours HCIA-Datacom, Huawei l'explique avec l'analogie d'un colis : les données sont préparées, emballées, adressées, transférées par plusieurs équipements, puis ouvertes par le destinataire. Comprendre ce trajet permet de relier la théorie réseau aux commandes de vérification, au troubleshooting et aux futurs chapitres sur les modèles de référence, Ethernet, IP et l'encapsulation.

---

## Objectifs officiels couverts

Cette note couvre les objectifs HCIA-Datacom liés à la compréhension du processus de communication de données :

- comprendre comment une donnée quitte une source et atteint une destination ;
- expliquer le rôle d'une source, d'un canal, d'une destination et des équipements intermédiaires ;
- distinguer les notions de data payload, packet, header, trailer, encapsulation et decapsulation ;
- comprendre le rôle d'un gateway dans l'échange entre réseaux ;
- préparer l'étude des modèles de référence réseau, de l'encapsulation, d'Ethernet, d'IP, des services réseau et du troubleshooting.

---

## Explication simple

Une communication réseau ressemble à l'envoi d'un colis.

Quand une personne envoie un objet, elle ne le dépose pas simplement dans la rue. Elle le met dans un emballage, ajoute une adresse de destination, parfois une adresse d'expéditeur, puis le colis passe par plusieurs points de tri avant d'arriver chez le destinataire.

Dans un réseau, c'est la même logique :

1. une application produit une donnée ;
2. cette donnée devient un payload, c'est-à-dire le contenu utile ;
3. les protocoles ajoutent des informations autour du payload ;
4. l'ensemble devient un packet ou une unité de transmission ;
5. le terminal envoie ce paquet vers le réseau ;
6. les équipements intermédiaires le lisent partiellement pour choisir le prochain chemin ;
7. le terminal de destination retire progressivement les informations ajoutées ;
8. l'application de destination reçoit finalement la donnée exploitable.

L'idée importante est simple : les équipements réseau ne transportent pas une donnée brute. Ils transportent une donnée structurée, avec des informations de contrôle qui permettent de l'acheminer correctement.

---

## Détails techniques

### Vue d'ensemble du trajet

| Étape | Élément concerné | Rôle dans la communication | Exemple pratique |
|---|---|---|---|
| 1 | Application source | Produit la donnée à transmettre | Un navigateur demande une page web |
| 2 | Terminal source | Prépare la donnée pour le réseau | Un PC génère du trafic IP |
| 3 | Protocole réseau | Ajoute des informations de contrôle | Adresse source, adresse destination, type de protocole |
| 4 | Interface réseau | Transmet sur un support physique ou radio | Carte Ethernet ou Wi-Fi |
| 5 | Switch d'accès | Transporte la trame dans le LAN | Transmission selon l'adresse MAC |
| 6 | Gateway | Permet de sortir du réseau local | Routeur ou firewall de sortie |
| 7 | Routeurs intermédiaires | Acheminent de réseau en réseau | Choix du prochain saut selon la table de routage |
| 8 | Gateway destination | Rejoint le réseau du destinataire | Routeur du réseau serveur |
| 9 | Terminal destination | Reçoit et traite la donnée | Serveur web ou poste utilisateur |
| 10 | Application destination | Exploite le contenu utile | Service web, application métier, DNS, SSH |

### Les termes essentiels

| Terme | Définition pratique | Point d'attention HCIA |
|---|---|---|
| Data payload | Donnée utile transportée par une couche réseau | Le payload d'une couche peut devenir la donnée d'entrée de la couche suivante |
| Packet | Unité de données échangée ou transmise selon un format précis | Le format peut changer pendant le trajet selon la couche ou le lien utilisé |
| Header | Information ajoutée avant le payload | Sert souvent à porter des adresses, des ports, des types ou des informations de contrôle |
| Trailer | Information ajoutée après le payload | Toutes les unités de données n'ont pas forcément un trailer |
| Encapsulation | Ajout d'un header et parfois d'un trailer autour d'un payload | C'est le mécanisme qui prépare la donnée pour une couche inférieure |
| Decapsulation | Retrait des informations ajoutées pour récupérer le payload | Le destinataire remonte progressivement les couches |
| Gateway | Point de passage entre réseaux ou environnements différents | Un gateway est un rôle de déploiement, pas forcément un type unique d'équipement |
| Terminal | Équipement final qui agit comme source ou destination | PC, serveur, smartphone, caméra IP, imprimante réseau |

### Les trois grands moments du processus

#### 1. Préparation côté source

Le terminal source reçoit une donnée depuis une application. Cette donnée est ensuite préparée pour le transport. Les protocoles ajoutent les informations nécessaires : qui envoie, qui reçoit, quel protocole utiliser, comment vérifier ou transporter l'information.

C'est ici que l'on commence à parler d'encapsulation.

#### 2. Transfert dans le réseau

Le paquet traverse un ou plusieurs équipements : switchs, routeurs, firewalls, gateways ou autres équipements selon la topologie. Certains équipements ne lisent qu'une partie des informations. Par exemple, un switch se concentre surtout sur les informations de couche 2, alors qu'un routeur travaille principalement avec les informations IP.

Chaque saut rapproche le paquet de sa destination.

#### 3. Réception côté destination

Le terminal destination reçoit l'unité de données, vérifie les informations utiles, retire progressivement les éléments ajoutés, puis transmet le payload à l'application concernée.

C'est ici que l'on parle de décapsulation.

### Pourquoi le format peut changer pendant le trajet

Dans un réseau réel, le contenu applicatif peut rester le même, mais les informations de transport autour de lui peuvent changer. Par exemple, une trame Ethernet peut être reconstruite à chaque nouveau lien, tandis que le paquet IP conserve généralement l'adresse IP source et destination pendant le routage classique.

Pour le troubleshooting, cette nuance est fondamentale : il faut savoir quelle information reste stable et quelle information est locale à un segment du réseau.

---

## À retenir pour l'examen HCIA

- Une communication réseau est un processus de bout en bout, pas seulement une commande `ping`.
- Le payload représente la donnée utile transportée.
- Un paquet contient généralement un header, un payload et parfois un trailer.
- L'encapsulation ajoute des informations de contrôle ; la décapsulation les retire.
- Un gateway permet de passer d'un réseau ou environnement à un autre.
- Un terminal peut être source ou destination de la communication.
- Les équipements intermédiaires prennent des décisions selon les informations qu'ils savent lire.
- Pour dépanner, il faut suivre le trajet de la donnée étape par étape.
- Cette notion prépare directement les chapitres sur les modèles OSI/TCP-IP, Ethernet, IP, routage, services réseau, sécurité et troubleshooting.

---

## Commandes Huawei utiles

Ces commandes ne "configurent" pas le processus de communication. Elles permettent d'observer où la communication fonctionne ou se bloque.

| Commande Huawei | Ce qu'elle permet de vérifier | Quand l'utiliser |
|---|---|---|
| `display version` | Version logicielle et information générale de l'équipement | Vérifier rapidement l'environnement avant un lab ou un diagnostic |
| `display device` | État matériel de l'équipement | Vérifier que les composants sont reconnus et opérationnels |
| `display interface brief` | État des interfaces physiques et logiques | Vérifier si un lien est up/down |
| `display ip interface brief` | Adresses IP et état des interfaces IP | Vérifier l'adressage de base |
| `display arp` | Correspondances IP/MAC connues localement | Diagnostiquer un problème de résolution locale |
| `display mac-address` | Table MAC apprise par un switch | Vérifier si le switch apprend les terminaux |
| `display ip routing-table` | Routes connues par l'équipement | Vérifier si un chemin existe vers le réseau destination |
| `ping` | Test de connectivité IP simple | Valider ou isoler une panne de communication |
| `tracert` | Chemin suivi jusqu'à une destination | Identifier à quel saut la communication échoue |

Exemple de première vérification :

```bash
display interface brief
display ip interface brief
display arp
display ip routing-table
ping 192.168.1.1
tracert 8.8.8.8
```

---

## Pratique obligatoire

### Objectif

Suivre le trajet logique d'une donnée de bout en bout, puis associer chaque étape à un équipement, une information réseau et une commande de vérification Huawei.

### Topologie

```text
PC-A ---- Switch d'accès ---- Gateway/Routeur ---- Réseau intermédiaire ---- Serveur-B
```

Variante campus :

```text
PC-A ---- Switch d'accès ---- Switch d'agrégation ---- Firewall/Routeur ---- Internet/WAN ---- Serveur-B
```

### Étapes

1. Dessiner la topologie.
2. Identifier la source, le canal et la destination.
3. Placer les équipements intermédiaires.
4. Indiquer le payload transporté, par exemple une requête web ou un ping.
5. Indiquer les informations ajoutées autour du payload : adresses, protocole, contrôle.
6. Suivre le chemin du paquet jusqu'à la destination.
7. Identifier ce que chaque équipement doit lire pour prendre une décision.
8. Ajouter une commande de vérification par étape importante.

### Vérification

| Point de contrôle | Question à se poser | Commande possible |
|---|---|---|
| Terminal source | Le terminal a-t-il une configuration IP correcte ? | `ipconfig` côté PC ou vérification dans l'interface graphique |
| Interface réseau | Le lien est-il actif ? | `display interface brief` |
| Réseau local | Le switch apprend-il l'adresse MAC ? | `display mac-address` |
| Résolution locale | L'équipement connaît-il l'adresse MAC du voisin IP ? | `display arp` |
| Sortie du LAN | La passerelle est-elle joignable ? | `ping <gateway>` |
| Routage | Existe-t-il une route vers la destination ? | `display ip routing-table` |
| Chemin bout en bout | Où le trafic s'arrête-t-il ? | `tracert <destination>` |

### Résultat attendu

L'apprenant doit être capable de raconter le trajet de la donnée sans réciter uniquement des définitions. Il doit pouvoir dire :

- qui envoie ;
- ce qui est envoyé ;
- par où la donnée passe ;
- quel équipement prend quelle décision ;
- quelle commande permet de vérifier chaque étape.

---

## Troubleshooting

| Symptôme | Cause probable | Vérification | Correction |
|---|---|---|---|
| Le terminal ne communique avec personne | Interface down, câble débranché ou Wi-Fi non connecté | `display interface brief` côté équipement, état réseau côté terminal | Corriger le lien physique ou radio |
| Le terminal a une IP incorrecte | Mauvais adressage ou DHCP indisponible | Vérifier l'adresse IP, le masque et la passerelle | Corriger la configuration IP ou le service DHCP |
| Le terminal ne joint pas la passerelle | Mauvais VLAN, mauvais port ou passerelle incorrecte | `display mac-address`, `display arp`, `ping <gateway>` | Corriger VLAN, port, IP ou passerelle |
| Le switch n'apprend pas l'adresse MAC du terminal | Port inactif, terminal déconnecté ou mauvais lien | `display mac-address` et `display interface brief` | Corriger le branchement ou l'état du port |
| Le routeur ne connaît pas la destination | Route absente ou mauvaise route | `display ip routing-table` | Ajouter ou corriger la route attendue |
| Le chemin s'arrête à un saut précis | Problème de routage, filtrage ou équipement intermédiaire | `tracert <destination>` | Examiner l'équipement où le trafic s'arrête |
| Le ping échoue mais le chemin semble correct | Filtrage ICMP ou politique de sécurité | Vérifier ACL/firewall si disponible | Adapter la politique ou tester avec un autre protocole |
| Le serveur est joignable mais l'application ne répond pas | Service applicatif arrêté ou mauvais port | Test applicatif, logs serveur, contrôle des ports | Redémarrer/corriger le service ou ouvrir le port nécessaire |

### Méthode TianSemi

Quand une communication échoue, ne commence pas par une commande avancée. Suis le trajet :

1. terminal ;
2. lien ;
3. switch ;
4. gateway ;
5. routage ;
6. filtrage ;
7. serveur ;
8. application.

---

## Mini-lab TianSemi

### Titre

Suivre le trajet d'une donnée dans un petit réseau d'entreprise.

### Objectif

Comprendre comment une donnée passe d'un terminal source vers un serveur destination, puis identifier les points de panne possibles.

### Matériel

- papier, tableau blanc ou draw.io ;
- eNSP si disponible ;
- deux terminaux, un switch et un routeur si l'environnement de lab est prêt.

### Scénario

Un utilisateur sur `PC-A` veut accéder à une application hébergée sur `Serveur-B`. La communication ne fonctionne pas toujours. Tu dois suivre le trajet de la donnée et trouver où commencer le diagnostic.

### Travail demandé

1. Dessiner la topologie `PC-A -> Switch -> Gateway -> Serveur-B`.
2. Indiquer la source, le canal, la destination et les équipements intermédiaires.
3. Nommer le payload transmis, par exemple une requête web.
4. Ajouter sur le dessin les notions de packet, header et payload.
5. Identifier à quel moment l'encapsulation se produit côté source.
6. Identifier à quel moment la décapsulation se produit côté destination.
7. Ajouter trois pannes volontaires : lien down, mauvaise passerelle, route absente.
8. Pour chaque panne, proposer une commande Huawei utile.

### Questions de validation

- Quelle est la différence entre payload et packet ?
- Pourquoi un équipement intermédiaire n'a-t-il pas toujours besoin de lire toute la donnée applicative ?
- Pourquoi la passerelle est-elle souvent le premier équipement à vérifier quand le LAN fonctionne mais pas l'accès externe ?
- Quelle commande aide à savoir si une route existe ?
- Quelle commande aide à savoir si un switch apprend bien un terminal ?

---

## Questions d'entretien

1. Peux-tu expliquer le processus de communication de données avec l'analogie d'un colis ?
   - Réponse attendue : expliquer préparation, adressage, transfert par étapes, livraison et ouverture côté destinataire.

2. Quelle est la différence entre data payload et packet ?
   - Réponse attendue : le payload est la donnée utile ; le packet est l'unité transmise qui contient le payload plus des informations de contrôle.

3. À quoi sert un header ?
   - Réponse attendue : il transporte des informations placées avant le payload, comme des adresses, des ports, des types de protocole ou des informations de contrôle.

4. Pourquoi parle-t-on d'encapsulation et de décapsulation ?
   - Réponse attendue : l'encapsulation ajoute des informations autour de la donnée pour la transporter ; la décapsulation retire ces informations côté réception pour remettre la donnée à l'application.

5. Qu'est-ce qu'un gateway dans un réseau ?
   - Réponse attendue : c'est un point de passage entre réseaux ou environnements différents ; ce rôle peut être assuré par différents équipements selon la conception.

6. Si un PC ne peut pas joindre un serveur distant, quelle méthode de diagnostic proposes-tu ?
   - Réponse attendue : vérifier terminal, lien, switch, passerelle, adressage IP, routage, filtrage, serveur et application.

---

## Quiz

1. Dans le processus de communication, que représente le data payload ?
   - A. L'adresse du routeur
   - B. La donnée utile transportée
   - C. Le câble réseau
   - D. Le nom de l'équipement
   - Réponse : B
   - Explication : le payload est le contenu utile que les couches réseau transportent.

2. Quel élément est généralement ajouté avant le payload ?
   - A. Header
   - B. Trailer uniquement
   - C. Mot de passe administrateur
   - D. Nom du fabricant
   - Réponse : A
   - Explication : le header est placé avant le payload et contient des informations de contrôle.

3. Que fait la décapsulation ?
   - A. Elle ajoute un câble réseau
   - B. Elle supprime une route
   - C. Elle retire des informations ajoutées pour récupérer le payload
   - D. Elle désactive une interface
   - Réponse : C
   - Explication : la décapsulation est le processus inverse de l'encapsulation.

4. Quel équipement joue souvent le rôle de point de passage entre un LAN et un autre réseau ?
   - A. Terminal uniquement
   - B. Gateway
   - C. Clavier
   - D. Moniteur
   - Réponse : B
   - Explication : un gateway permet l'échange entre réseaux ou environnements différents.

5. Quelle commande Huawei permet de vérifier la table de routage ?
   - A. `display ip routing-table`
   - B. `display mac-address`
   - C. `display version`
   - D. `display device`
   - Réponse : A
   - Explication : cette commande montre les routes connues par l'équipement.

6. Un switch ne voit pas l'adresse MAC d'un PC. Quelle commande est pertinente ?
   - A. `display mac-address`
   - B. `tracert`
   - C. `display version`
   - D. `display ip routing-table`
   - Réponse : A
   - Explication : la table MAC permet de vérifier si le switch apprend les terminaux connectés.

---

## Flashcards

Q: Qu'est-ce qu'un data payload ?
A: C'est la donnée utile transportée par une unité de communication.

Q: Qu'est-ce qu'un packet ?
A: C'est une unité de données structurée, généralement composée d'informations de contrôle et d'un payload.

Q: À quoi sert un header ?
A: Il porte des informations placées avant le payload, comme des adresses ou des paramètres de protocole.

Q: Tous les packets ont-ils un trailer ?
A: Non. Certains formats utilisent un trailer, d'autres non.

Q: Qu'est-ce que l'encapsulation ?
A: C'est l'ajout d'informations de contrôle autour d'un payload pour permettre sa transmission.

Q: Qu'est-ce que la décapsulation ?
A: C'est le retrait progressif des informations ajoutées pour récupérer le payload.

Q: Qu'est-ce qu'un gateway ?
A: C'est un point de passage entre réseaux ou environnements différents.

Q: Un gateway est-il toujours un type précis d'équipement ?
A: Non. C'est un rôle fonctionnel qui peut être assuré par différents équipements.

Q: Pourquoi le processus de communication est-il important en troubleshooting ?
A: Parce qu'il permet de localiser la panne étape par étape.

Q: Quelle commande vérifie rapidement l'état des interfaces Huawei ?
A: `display interface brief`.

Q: Quelle commande vérifie les routes connues ?
A: `display ip routing-table`.

Q: Quelle commande permet d'observer le chemin vers une destination ?
A: `tracert <destination>`.

---

## Références

- HCIA-Datacom V2.0 Training Material, section "Data Communication Process", pages 31-36.
- HCIA-Datacom V2.0 Training Material, transition "Journey of This Course", pages 36-42 pour replacer le sujet dans le parcours complet.
- HCIA-Datacom V2.0 Lab Guide, à utiliser ensuite pour relier ce concept aux labs de basic operations, routage, VLAN et troubleshooting.
- Huawei Talent Certification page : https://e.huawei.com/en/talent/cert/#/careerCert

---

## Contenus générés

| Canal | Statut | Lien |
|---|---|---|
| Site TianSemi | À générer | |
| Quiz | À générer | |
