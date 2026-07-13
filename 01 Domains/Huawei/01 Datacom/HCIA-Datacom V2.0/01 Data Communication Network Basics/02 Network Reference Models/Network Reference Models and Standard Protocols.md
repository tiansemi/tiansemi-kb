---
id: HUA-HCIA-DC-006
title: "Network Reference Models and Standard Protocols"
official_title: "Network Reference Models and Standard Protocols"
course_unit: "1.2.2"
category: "Huawei HCIA-Datacom Topic"
domain: "Datacom"
vendor: "Huawei"
certification: "HCIA-Datacom"
version: "V2.0"
difficulty: "beginner"
status: "draft"
author: "MOULO OHOLO Jean Noel"
reviewed: false
created: 2026-07-13
updated: 2026-07-13
source: "HCIA-Datacom V2.0 Training Material"
source_pages: "PDF 54-79"
tags: [huawei, hcia, datacom, osi, tcp-ip, protocols]
prerequisites:
  - "[[Applications and Data]]"
related:
  - "[[02 Network Reference Models/Data Communication Process]]"
lab_required: false
publication_status: "not-started"
site_url:
---

# Modèles de référence réseau et protocoles standards (Network Reference Models and Standard Protocols)

## Protocoles réseau et organismes de normalisation

Un protocole réseau est un ensemble de règles et de conventions prédéfinies que les équipements doivent respecter pour communiquer.

Huawei distingue :

- les **protocoles ouverts**, définis par des organismes de normalisation ;
- les **protocoles propriétaires**, définis par des fournisseurs d'équipements.

| Organisme | Rôle indiqué dans le cours |
| --- | --- |
| IETF | développe et promeut les protocoles Internet, particulièrement la suite TCP/IP, et publie les RFC |
| IEEE | publie notamment IEEE 802.3 pour Ethernet et IEEE 802.11 pour le Wi-Fi |
| ISO | contribue aux normes de réseau et définit le modèle OSI dans ISO/IEC 7498-1 |
| IEC | traite les normes internationales des domaines électrique et électronique |

Une RFC peut publier un standard, un protocole ou d'autres informations relatives au fonctionnement d'Internet.

## Pourquoi une architecture en couches ?

Les équipements exécutent plusieurs protocoles. Leur organisation en couches :

- facilite le développement indépendant des protocoles ;
- réduit les dépendances entre couches ;
- clarifie les responsabilités ;
- facilite l'apprentissage, la conception et le troubleshooting ;
- favorise la normalisation et la compatibilité entre matériels et logiciels.

## Modèle de référence OSI

L'ISO a proposé dans les années 1980 le modèle OSI, composé de sept couches.

| Couche | Fonction officielle résumée |
| --- | --- |
| 7. Application | fournit aux applications des interfaces vers les services réseau |
| 6. Présentation | convertit les formats et représentations des données |
| 5. Session | établit, gère et termine les sessions de communication |
| 4. Transport | fournit un transport de bout en bout fiable ou efficace, avec contrôle de séquence et de vitesse |
| 3. Réseau | assure l'adressage logique, la sélection de chemin et le transfert entre réseaux |
| 2. Liaison de données | organise les données en trames, fournit la communication sur le lien et détecte les erreurs |
| 1. Physique | transmet les flux de bits et définit les caractéristiques physiques du média |

Le modèle OSI est un cadre théorique qui a fortement contribué au développement et à la compréhension des technologies réseau.

## Modèle de référence TCP/IP

Le modèle TCP/IP provient de la conception et de l'implémentation d'ARPANET, puis des travaux de l'IETF. Contrairement au modèle OSI principalement théorique, il est issu de la pratique et de nombreux protocoles décrits dans les RFC.

| Couche TCP/IP | Fonction |
| --- | --- |
| Application | protocoles fournissant des services aux utilisateurs ou aux fonctions système |
| Transport | communication de bout en bout avec TCP ou UDP |
| Internet | transfert de paquets entre hôtes et réseaux, principalement avec IP |
| Interface réseau | transmission des trames entre nœuds adjacents sur un réseau physique |

Le support associe notamment RFC 793 à TCP, RFC 791 à IP, puis RFC 1122 et RFC 1123 à la formalisation du modèle hôte TCP/IP.

## Modèle TCP/IP équivalent

Le modèle TCP/IP équivalent n'est pas un modèle officiel défini par un organisme de normalisation. Il s'agit d'un cadre pédagogique et pratique qui sépare la couche interface réseau en deux couches : liaison de données et physique.

```text
Application
Transport
Réseau
Liaison de données
Physique
```

Huawei utilise ce modèle à cinq couches dans la suite du cours. Les ingénieurs réseau se concentrent principalement sur les quatre couches basses, alors que les ingénieurs IT s'intéressent davantage à la couche application.

## Protocoles courants de la pile TCP/IP

| Couche | Protocoles cités |
| --- | --- |
| Application | Telnet, FTP, TFTP, SNMP, HTTP, SMTP, DNS, DHCP |
| Transport | TCP, UDP |
| Réseau | IP, ICMP, IGMP |
| Liaison | Ethernet, PPP, PPPoE |

Les couches échangent des PDU. Chaque couche ajoute ou traite des informations adaptées à sa fonction.

## Couche application

La couche application fournit aux logiciels les interfaces permettant d'utiliser les services réseau. Les protocoles d'application désignent notamment le protocole de transport et les ports associés.

| Protocole | Fonction | Port présenté |
| --- | --- | --- |
| HTTP | navigation web | TCP 80 |
| SMTP | courrier électronique | TCP 25 |
| Telnet | administration distante | TCP 23 |
| FTP | transfert de fichiers | TCP 20 et 21 |
| DNS | résolution de noms | UDP 53 |

La PDU de la couche application est appelée **data**.

### DNS

DNS est une application client-serveur qui résout un nom de domaine en adresse IP. Le client envoie une requête au serveur DNS, reçoit l'adresse associée, puis utilise cette adresse pour communiquer avec le serveur demandé.

### HTTP

HTTP est un protocole applicatif entre un navigateur ou un autre client et un serveur web. Le client résout d'abord le nom avec DNS si nécessaire, puis demande une ressource identifiée par une URL. Le serveur localise cette ressource et renvoie son contenu.

## Couche transport

La couche transport reçoit les données de l'application, ajoute son en-tête et fournit une communication de bout en bout entre ports. La PDU est appelée **segment** dans le cours.

| Protocole | Caractéristiques | Scénarios cités |
| --- | --- | --- |
| TCP | orienté connexion, fiable, livraison ordonnée sans perte ni duplication selon la présentation du cours | web, fichiers, e-mail |
| UDP | sans connexion, faible surcharge et faible latence, sans garantie de fiabilité | appels vidéo, jeux en ligne, DNS |

TCP et UDP utilisent les ports source et destination pour identifier les applications qui communiquent.

## Couche réseau

La couche réseau transmet les données d'un hôte à un autre. Elle fournit l'adressage logique et le routage des paquets.

- La PDU est appelée **packet**.
- IPv4 et IPv6 identifient les hôtes avec des adresses logiques.
- ICMP fournit des messages de contrôle et aide au diagnostic.
- IGMP gère l'appartenance des hôtes aux groupes multicast directement connectés.

### Processus IP

1. La couche réseau reçoit les données de la couche transport.
2. Elle ajoute un en-tête IP contenant les adresses source et destination.
3. Un routeur lit l'adresse destination et consulte sa table de routage.
4. Il transmet le paquet selon l'entrée correspondante.
5. L'hôte destination vérifie l'adresse et accepte le paquet qui lui est destiné.

Les protocoles de routage comme OSPF ou BGP aident les routeurs à construire leurs tables ; ICMP contribue au contrôle et au diagnostic.

## Couche liaison de données

La couche liaison se situe entre les couches réseau et physique. Elle fournit une communication à l'intérieur d'un segment, réalise le framing, l'adressage physique et la détection d'erreurs. La PDU est appelée **frame**.

### Ethernet

Ethernet est la technologie LAN la plus courante. Son évolution présentée par Huawei va des travaux inspirés d'ALOHAnet et du CSMA/CD à la normalisation IEEE 802.3, puis au passage des topologies bus aux topologies en étoile et aux débits élevés.

Une adresse MAC :

- est une adresse de couche liaison ;
- est aussi appelée adresse Ethernet, physique ou matérielle ;
- mesure 48 bits, soit 6 octets ;
- guide le transfert des trames par les switchs Ethernet.

### PPP

PPP est un protocole de liaison WAN point à point sur liaison full-duplex. Le cours le présente notamment pour relier une agence au siège.

Avantages cités :

- prise en charge des liaisons synchrones et asynchrones ;
- extensibilité, notamment vers PPPoE ;
- négociation par LCP ;
- authentification PAP ou CHAP ;
- négociation des protocoles réseau par NCP ;
- absence de mécanisme de retransmission propre à PPP.

### Établissement d'une liaison PPP

1. **Dead** : la liaison n'est pas active.
2. **Establish** : LCP négocie le mode, la MRU, l'authentification et d'autres paramètres.
3. **Authenticate**, si configuré : PAP ou CHAP authentifie les pairs.
4. **Network** : NCP sélectionne et configure le protocole réseau ; IPCP peut négocier les adresses IP.
5. **Terminate** : les ressources sont libérées avant le retour à l'état Dead.

## Couche physique

La couche physique convertit les données numériques en signaux électriques, optiques ou électromagnétiques. Sa PDU est appelée **bitstream**. Elle normalise notamment câbles, connecteurs, niveaux électriques, débits et interfaces.

### Médias de transmission

| Média | Caractéristiques présentées |
| --- | --- |
| Paire torsadée | câbles Cat 5, 5e ou 6 avec connecteur RJ45, portée maximale courante de 100 m ; versions UTP et STP |
| Fibre monomode | un seul mode, grande bande passante et longues distances |
| Fibre multimode | plusieurs modes, dispersion plus importante et distances plus courtes |
| Module optique | conversion entre signaux électriques et optiques |
| Câble hybride | combine fibre et cuivre pour transporter données et alimentation |
| Onde électromagnétique | transporte les signaux sans fil entre AP ou routeur sans fil et terminaux |

Huawei distingue également les câbles hybrides 1.0 et 2.0 selon les connecteurs et l'intégration des fonctions optiques et électriques.

## Résumé fidèle de l'unité

- OSI et TCP/IP appliquent une organisation en couches.
- Le cours utilise un modèle TCP/IP équivalent à cinq couches.
- Les protocoles standards permettent l'interopérabilité entre équipements.
- Chaque couche remplit une fonction définie et manipule une PDU spécifique.
- Les principales PDU sont data, segment, packet, frame et bitstream.
- Ethernet domine les LAN ; PPP est présenté comme protocole WAN point à point.

## Révision TianSemi

1. Quelles sont les sept couches OSI et les quatre couches TCP/IP ?
2. Pourquoi le modèle TCP/IP équivalent n'est-il pas un standard officiel ?
3. Quelle différence essentielle existe entre TCP et UDP ?
4. Comment un routeur utilise-t-il l'adresse IP destination ?
5. Quelles négociations interviennent dans l'établissement d'une liaison PPP ?
6. Quels médias la couche physique peut-elle utiliser ?

## Références

- Huawei, *HCIA-Datacom V2.0 Training Material*, pages PDF 54-79.
- Huawei Talent, HCIA-Datacom V2.0 : https://e.huawei.com/en/talent/#/cert/product-details?certifiedProductId=1316&authenticationLevel=CTYPE_CARE_HCIA&technicalField=IIC&version=2.0
