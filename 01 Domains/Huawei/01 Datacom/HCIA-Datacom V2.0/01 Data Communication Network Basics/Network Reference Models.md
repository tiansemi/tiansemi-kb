---
id: HUA-HCIA-DC-005
title: "Network Reference Models"
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
  - osi
  - tcp-ip
  - protocols
keywords:
  - OSI reference model
  - TCP/IP reference model
  - equivalent TCP/IP model
  - network protocols
  - standards organizations
  - PDU
prerequisites:
  - "Data Communication Network"
  - "Data Communication Process"
related:
  - "Data Encapsulation and Decapsulation"
  - "Huawei Network Device Operating Systems"
  - "Ethernet Switching Basics"
  - "IP Address and Configuration"
commands:
  - "display interface brief"
  - "display ip interface brief"
  - "display mac-address"
  - "display arp"
  - "display ip routing-table"
  - "ping"
  - "tracert"
labs:
  - "01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Network Reference Models

## Résumé

> Les modèles de référence découpent une communication réseau en couches. Chaque couche fournit un service à la couche supérieure, utilise les services de la couche inférieure et s'appuie sur des protocoles définis. Le modèle OSI sert surtout de cadre conceptuel à sept couches ; le modèle TCP/IP décrit la pile réellement utilisée sur Internet. Le cours Huawei emploie aussi un modèle TCP/IP équivalent à cinq couches pour rapprocher théorie, protocoles et pratique d'ingénierie.

---

## Objectifs officiels couverts

Cette note couvre les objectifs du chapitre Huawei « Network Reference Models » :

- comprendre le lien entre applications, données et protocoles ;
- définir un protocole réseau et l'intérêt des standards ouverts ;
- identifier le rôle de l'IETF, de l'IEEE et de l'ISO ;
- expliquer les avantages d'une architecture en couches ;
- connaître les couches des modèles OSI, TCP/IP et TCP/IP équivalent ;
- associer les principaux protocoles à leur couche ;
- nommer les unités de données : data, segment, packet, frame et bitstream ;
- utiliser les couches comme méthode de lecture et de dépannage d'une communication.

---

## Explication simple

Quand un navigateur ouvre un site, plusieurs problèmes différents doivent être résolus :

- comprendre une requête web ;
- identifier l'application avec des ports ;
- adresser le paquet jusqu'au bon réseau ;
- livrer une trame au prochain équipement ;
- transformer l'information en signaux sur un support.

Un seul protocole ne réalise pas toutes ces fonctions. Les modèles de référence les répartissent en couches. Chaque couche répond à une question précise et peut évoluer sans obliger toutes les autres couches à être redessinées.

```text
Application : quel service réseau utilise-t-on ?
Transport   : quelle application source parle à quelle application destination ?
Réseau      : comment atteindre le réseau et l'hôte distants ?
Liaison     : comment livrer au prochain voisin sur ce lien ?
Physique    : comment transporter les bits sur le média ?
```

Le modèle n'est pas le paquet lui-même. C'est une grille de lecture qui aide à comprendre les protocoles, les équipements et les pannes.

---

## Détails techniques

### Applications et données

Une application répond à un besoin humain ou métier : navigation web, messagerie, transfert de fichiers, jeu en ligne, téléphonie, supervision. Elle produit des données sous différentes formes : texte, image, audio, vidéo ou information structurée.

Pour transporter ces données entre deux équipements, les applications s'appuient sur une pile de protocoles. Chaque protocole définit des règles : format des messages, ordre des échanges, signification des champs et comportement attendu.

### Protocoles et organismes de normalisation

Un protocole réseau est un ensemble de règles et de conventions utilisées par les participants d'une communication. Les protocoles ouverts favorisent l'interopérabilité entre équipements et logiciels de fournisseurs différents.

| Organisme | Rôle général | Exemple lié au cours |
| --- | --- | --- |
| IETF | développe et publie de nombreux standards Internet | RFC décrivant IP, TCP, UDP, HTTP ou d'autres protocoles |
| IEEE | normalise notamment les technologies LAN et WLAN | famille IEEE 802, dont Ethernet et Wi-Fi |
| ISO | produit des normes internationales | modèle de référence OSI défini dans ISO/IEC 7498-1 |

Une RFC peut décrire un standard, un protocole, une pratique ou une proposition technique. Toutes les RFC n'ont pas exactement le même statut normatif ; pour l'examen, il faut surtout retenir leur relation avec les travaux de l'IETF et les protocoles Internet.

### Pourquoi utiliser des couches ?

Le découpage en couches apporte plusieurs bénéfices :

- réduire la complexité en séparant les responsabilités ;
- permettre à une couche d'évoluer tout en conservant des interfaces stables ;
- favoriser l'interopérabilité grâce aux standards ;
- réutiliser un même service de couche inférieure pour plusieurs applications ;
- localiser plus rapidement une panne ;
- faciliter l'apprentissage, la conception et la documentation.

### Le modèle OSI à sept couches

| N° | Couche OSI | Fonction principale | Exemples ou notions |
| --- | --- | --- | --- |
| 7 | Application | fournit des services réseau aux applications | HTTP, FTP, DNS, Telnet, SMTP, SNMP |
| 6 | Présentation | adapte la représentation des données | format, encodage, chiffrement, compression |
| 5 | Session | établit, maintient et termine les dialogues | gestion de session et synchronisation |
| 4 | Transport | assure la communication de bout en bout entre applications | TCP, UDP, ports, segmentation |
| 3 | Réseau | adresse et achemine entre réseaux | IPv4, IPv6, ICMP, routage |
| 2 | Liaison de données | transfère des trames entre voisins d'un même lien | Ethernet, PPP, adresses MAC, FCS |
| 1 | Physique | transporte un flux de bits sur le média | signal électrique, optique ou radio |

Le modèle OSI est un modèle conceptuel complet. Les protocoles Internet courants ne correspondent pas toujours parfaitement à une seule couche OSI, mais ce modèle reste très utile pour raisonner.

### Le modèle TCP/IP à quatre couches

| Couche TCP/IP | Fonction | Correspondance OSI approximative |
| --- | --- | --- |
| Application | services utilisés par les applications | OSI 5 à 7 |
| Transport | communication de bout en bout | OSI 4 |
| Internet | adressage et acheminement IP | OSI 3 |
| Accès réseau | trames et transmission sur le lien | OSI 1 et 2 |

Le modèle TCP/IP est issu de la construction pratique des réseaux Internet. Il est associé à la suite de protocoles dont TCP et IP sont deux éléments majeurs.

### Le modèle TCP/IP équivalent à cinq couches

Pour l'apprentissage et l'ingénierie, le support Huawei sépare la couche d'accès réseau en deux parties. Cette représentation n'est pas un modèle officiel défini par un organisme de normalisation ; c'est un cadre pédagogique qui rapproche OSI et TCP/IP.

```text
OSI                    TCP/IP              TCP/IP équivalent
7 Application  ┐
6 Présentation ├──>    Application    ───> Application
5 Session      ┘
4 Transport    ───>    Transport      ───> Transport
3 Réseau       ───>    Internet       ───> Réseau
2 Liaison      ┐
1 Physique     ┴──>    Accès réseau   ───> Liaison + Physique
```

Le cours HCIA-Datacom s'appuie ensuite sur ce modèle à cinq couches pour présenter les protocoles et l'encapsulation.

### Protocoles courants de la pile TCP/IP

| Couche équivalente | Protocoles ou technologies | Rôle simplifié |
| --- | --- | --- |
| Application | HTTP, DNS, FTP, TFTP, Telnet, SMTP, SNMP, DHCP | services directement utilisés ou sollicités par les applications |
| Transport | TCP, UDP | multiplexage par ports et transport de bout en bout |
| Réseau | IPv4, IPv6, ICMP, IGMP | adressage, acheminement et messages de contrôle |
| Liaison | Ethernet, PPP, PPPoE | livraison de trames sur un lien local ou point à point |
| Physique | Ethernet physique, fibre, cuivre, radio | transmission du flux binaire |

#### Application

- **DNS** traduit notamment un nom en information d'adressage utilisable.
- **HTTP** permet l'échange de ressources web entre client et serveur.
- **FTP/TFTP** servent au transfert de fichiers avec des caractéristiques différentes.
- **Telnet** fournit un accès distant en clair ; un accès sécurisé doit être privilégié en exploitation.
- **SNMP** permet la supervision et la gestion d'équipements.
- **DHCP** fournit automatiquement des paramètres réseau aux clients.

#### Transport

- **TCP** est orienté connexion et fournit des mécanismes de fiabilité et d'ordre.
- **UDP** est sans connexion et privilégie une transmission légère, sans garantie équivalente à TCP.
- Les numéros de port identifient les applications source et destination.

#### Réseau

- **IPv4 et IPv6** portent les adresses logiques et permettent l'acheminement entre réseaux.
- **ICMP** transporte des messages de contrôle et sert notamment à certains diagnostics.
- Les routeurs examinent les informations de couche réseau pour choisir le prochain saut.

#### Liaison et physique

- **Ethernet** est la technologie de liaison la plus courante dans les LAN.
- **PPP** fournit une encapsulation point à point, souvent associée aux environnements WAN.
- La couche physique transforme la trame en bitstream, puis en signal adapté au support.

### Unités de données par couche

| Couche équivalente | Nom de la PDU |
| --- | --- |
| Application | Data |
| Transport | Segment, dans la présentation TCP du cours |
| Réseau | Packet |
| Liaison de données | Frame |
| Physique | Bitstream |

Une PDU contient les informations nécessaires à la couche concernée. Lorsqu'elle descend la pile, elle devient la charge utile de la couche suivante.

---

## À retenir pour l'examen HCIA

- OSI possède sept couches ; TCP/IP en possède quatre dans sa représentation classique.
- Le modèle TCP/IP équivalent à cinq couches est un cadre pédagogique utilisé dans le cours, pas une norme officielle distincte.
- IETF est fortement lié aux protocoles Internet et aux RFC ; IEEE aux technologies 802 ; ISO au modèle OSI.
- Une couche fournit des services à la couche supérieure et utilise ceux de la couche inférieure.
- TCP et UDP appartiennent à la couche transport ; IPv4, IPv6 et ICMP à la couche réseau.
- Ethernet et PPP sont des protocoles de liaison de données.
- Les PDU sont nommées data, segment, packet, frame et bitstream dans le parcours du cours.
- Un switch travaille principalement à la couche liaison ; un routeur prend ses décisions principales à la couche réseau.
- Les couches servent aussi de méthode de troubleshooting : physique, liaison, réseau, transport, puis application.

---

## Commandes Huawei utiles

Les modèles ne se configurent pas directement. Les commandes suivantes permettent d'observer les informations associées à plusieurs couches.

| Couche observée | Commande | Ce qu'elle vérifie |
| --- | --- | --- |
| Physique/Liaison | `display interface brief` | état des interfaces et du protocole de ligne |
| Liaison | `display mac-address` | adresses MAC apprises par le switch |
| Liaison/Réseau | `display arp` | correspondances entre adresses IP et MAC voisines |
| Réseau | `display ip interface brief` | adresses IP et état des interfaces |
| Réseau | `display ip routing-table` | routes disponibles et prochain saut |
| Réseau | `ping <adresse>` | accessibilité IP et réponses ICMP |
| Réseau | `tracert <adresse>` | progression de saut en saut |

Séquence de diagnostic par couches :

```text
display interface brief
display mac-address
display arp
display ip interface brief
display ip routing-table
ping <destination>
tracert <destination>
```

---

## Pratique obligatoire

### Objectif

Associer chaque élément d'une communication à une couche, un protocole, une PDU et une commande de vérification.

### Topologie

```text
PC-A ---- S1 ---- R1 ---- S2 ---- Serveur-B
```

### Étapes

1. Choisir un scénario, par exemple l'ouverture d'une page web.
2. Identifier les protocoles d'application nécessaires, notamment DNS puis HTTP.
3. Associer TCP ou UDP au service concerné.
4. Identifier le rôle d'IP entre les réseaux.
5. Identifier le rôle d'Ethernet sur chaque lien local.
6. Nommer la PDU à chaque couche.
7. Associer S1 et S2 aux informations de liaison, puis R1 aux informations réseau.
8. Proposer une commande Huawei pour vérifier chaque point observable.

### Matrice d'analyse

| Étape | Couche | Protocole | PDU | Équipement ou commande |
| --- | --- | --- | --- | --- |
| Résolution du nom | Application | DNS | Data | client et serveur DNS |
| Connexion web | Transport | TCP | Segment | ports source/destination |
| Acheminement | Réseau | IP | Packet | R1, `display ip routing-table` |
| Livraison locale | Liaison | Ethernet | Frame | S1/S2, `display mac-address` |
| Signal | Physique | technologie du média | Bitstream | interface et câble |

### Résultat attendu

L'apprenant doit pouvoir expliquer pourquoi une panne physique empêche toutes les couches supérieures, alors qu'une panne DNS peut laisser fonctionner un `ping` par adresse IP.

---

## Troubleshooting

| Symptôme | Couche probable | Vérification | Correction |
| --- | --- | --- | --- |
| Interface down | physique | `display interface brief`, câble et alimentation | corriger le support ou activer l'interface |
| Interface up mais aucun voisin local | liaison | table MAC et ARP | corriger VLAN, port ou adressage local |
| Passerelle joignable mais réseau distant inaccessible | réseau | table de routage et `tracert` | corriger route, masque ou prochain saut |
| Adresse IP joignable mais nom inutilisable | application, DNS | tester le nom puis l'adresse | corriger DNS ou la configuration du client |
| Certaines applications échouent seulement | transport ou application | vérifier service, port et politique d'accès | corriger le service ou la règle concernée |
| Diagnostic bloqué par une confusion de couche | méthode incorrecte | classer chaque fait par couche | repartir du bas et progresser méthodiquement |

### Principe de dépannage par couches

1. Vérifier que le média et l'interface fonctionnent.
2. Vérifier la livraison locale : VLAN, MAC et ARP.
3. Vérifier l'adressage et le routage IP.
4. Vérifier le transport et les ports utilisés.
5. Vérifier le service applicatif et ses dépendances.

---

## Mini-lab TianSemi

### Titre

Diagnostiquer une communication avec le modèle TCP/IP équivalent.

### Scénario

PC-A n'accède pas à Serveur-B. L'enseignant introduit une seule erreur parmi les suivantes : câble déconnecté, interface désactivée, mauvaise adresse IP, route absente ou service applicatif indisponible.

### Travail demandé

1. Ne modifier aucune configuration au départ.
2. Construire un tableau des cinq couches.
3. Exécuter les vérifications du bas vers le haut.
4. Noter le premier point non conforme.
5. Corriger uniquement la cause identifiée.
6. Rejouer tous les tests jusqu'à l'application.

### Commandes minimales

```text
display interface brief
display mac-address
display arp
display ip interface brief
display ip routing-table
ping <passerelle>
ping <serveur>
tracert <serveur>
```

### Critère de réussite

La cause doit être identifiée avec une preuve liée à une couche précise, puis la communication doit être validée après correction.

---

## Questions d'entretien

1. Pourquoi les réseaux utilisent-ils des architectures en couches ?
2. Quelle différence existe entre le modèle OSI et la pile TCP/IP ?
3. Pourquoi le cours Huawei utilise-t-il un modèle TCP/IP équivalent à cinq couches ?
4. Quels organismes associez-vous aux RFC, à IEEE 802 et au modèle OSI ?
5. À quelles couches placez-vous TCP, IP et Ethernet ?
6. Quelle différence existe entre un segment, un paquet et une trame ?
7. Pourquoi un ping par IP peut-il fonctionner alors que l'ouverture d'un site par nom échoue ?
8. Comment utilisez-vous les couches pour dépanner un réseau ?

---

## Quiz

### 1. Combien de couches contient le modèle OSI ?

- A. 4
- B. 5
- C. 7
D. 8

**Réponse : C.**

### 2. Quel organisme publie de nombreuses RFC Internet ?

- A. IETF
- B. ISO uniquement
- C. Aucun organisme
D. Un constructeur unique

**Réponse : A.**

### 3. À quelle couche équivalente appartient IP ?

- A. Application
- B. Transport
- C. Réseau
D. Physique

**Réponse : C.**

### 4. Quelle PDU est associée à la liaison de données ?

- A. Segment
- B. Frame
- C. Packet
D. Data uniquement

**Réponse : B.**

### 5. Quel protocole appartient à la couche transport ?

- A. Ethernet
- B. TCP
- C. IPv4
D. ICMP

**Réponse : B.**

### 6. Quelle couche utilise principalement un routeur pour choisir un chemin ?

- A. Physique
- B. Liaison
- C. Réseau
D. Présentation

**Réponse : C.**

### 7. Le modèle TCP/IP équivalent à cinq couches est-il une norme officielle autonome ?

- A. Oui
- B. Non, c'est un cadre pédagogique et pratique
- C. Il remplace toutes les RFC
D. Il ne contient pas IP

**Réponse : B.**

### 8. Quel test aide à distinguer un problème DNS d'un problème IP général ?

- A. Comparer l'accès par nom et le ping par adresse IP
- B. Redémarrer tous les équipements
- C. Effacer la configuration
D. Changer le câble sans vérifier

**Réponse : A.**

---

## Flashcards

**Q : Pourquoi un modèle de référence est-il utile ?**

R : Il sépare les responsabilités, facilite l'interopérabilité, l'apprentissage et le dépannage.

**Q : Quelles sont les sept couches OSI ?**

R : Application, présentation, session, transport, réseau, liaison de données et physique.

**Q : Quelles sont les quatre couches TCP/IP ?**

R : Application, transport, Internet et accès réseau.

**Q : Quelles sont les cinq couches du modèle équivalent utilisé dans le cours ?**

R : Application, transport, réseau, liaison de données et physique.

**Q : À quoi sert l'IETF ?**

R : À développer et promouvoir de nombreux standards et protocoles Internet, publiés notamment sous forme de RFC.

**Q : À quoi associe-t-on IEEE dans ce chapitre ?**

R : Aux standards de réseau de la famille 802, comme Ethernet et WLAN.

**Q : Quelle PDU correspond à la couche réseau ?**

R : Le packet.

**Q : Quelle PDU correspond à la couche physique ?**

R : Le bitstream.

**Q : Où se trouvent les numéros de port ?**

R : Dans les informations de couche transport, notamment TCP ou UDP.

**Q : Quelle commande vérifie les routes Huawei ?**

R : `display ip routing-table`.

---

## Références

- HCIA-Datacom V2.0 Training Material, chapitre « Network Reference Models », pages PDF 46-79 pour applications, données, protocoles, organismes de normalisation, modèles OSI/TCP-IP et protocoles par couche.
- HCIA-Datacom V2.0 Training Material, pages PDF 80-86 pour la transition vers les PDU, l'encapsulation et la décapsulation, détaillées dans la note dédiée.
- HCIA-Datacom V2.0 Lab Guide, lab « Basic Operations on Huawei Network Devices », pages PDF 14-25 pour les commandes CLI de base utilisées dans la pratique.
- Huawei Talent Certification page : https://e.huawei.com/en/talent/cert/#/careerCert

---

## Contenus générés

| Canal | Statut | Lien |
| --- | --- | --- |
| Site TianSemi | À générer | |
| Quiz | Intégré à la note | |
