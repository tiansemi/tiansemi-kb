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
status: "draft"
author: "MOULO OHOLO Jean Noel"
reviewed: false
last_review:
created: 2026-07-03
updated: 2026-07-04
tags: [cisco, networking, ccna]
keywords: []
prerequisites: []
related: []
references: []
assets: []
labs: []
blog:
site_url:
publication_status: "not-started"
---

# OSI Model

## Résumé

> Le modèle OSI est un modèle de référence qui organise la communication réseau en 7 couches.
> Il aide à comprendre comment une donnée passe d'une application au support physique.
> Il sert surtout à apprendre, expliquer et diagnostiquer les problèmes réseau.
> Sur Internet, l'implémentation pratique suit plutôt le [[TCP-IP Model]].

---

## Définition

OSI signifie **Open Systems Interconnection**.

Le modèle OSI est un **modèle de référence** créé pour décrire les fonctions nécessaires à une communication entre systèmes ouverts. Il découpe la communication réseau en sept couches, de la couche physique jusqu'à la couche application.

Il ne décrit pas toujours l'implémentation exacte d'Internet. En pratique, Internet utilise surtout le [[TCP-IP Model]], qui regroupe certaines fonctions OSI différemment. Le modèle OSI reste cependant très utile pour apprendre le réseau, structurer un diagnostic et expliquer clairement où se situe un problème.

Point important pour éviter la confusion : OSI n'est pas un protocole à installer ou à configurer. C'est une grille de lecture. Les protocoles réels, comme Ethernet, IP, TCP, UDP, DNS, HTTP ou TLS, peuvent parfois toucher plusieurs couches selon l'angle d'analyse.

---

## Pourquoi c'est important ?

Le modèle OSI donne une méthode de raisonnement. Au lieu de chercher une panne au hasard, on peut avancer couche par couche :

- couche 1 : le signal circule-t-il ?
- couche 2 : la machine est-elle dans le bon VLAN et connaît-elle les adresses MAC ?
- couche 3 : l'adressage IP et le routage sont-ils corrects ?
- couche 4 : le port TCP ou UDP est-il ouvert ?
- couche 7 : le service applicatif répond-il ?

Pour un étudiant CCNA, ce modèle sert de carte mentale pour relier [[Ethernet]], [[MAC Address]], [[ARP]], [[IPv4]], [[IPv6]], TCP/UDP, DNS, HTTP et HTTPS.

---

## Objectif pédagogique

À la fin de cette note, l'apprenant doit pouvoir :

- citer les 7 couches OSI dans l'ordre ;
- expliquer le rôle général de chaque couche ;
- différencier le modèle OSI du [[TCP-IP Model]] ;
- expliquer [[Encapsulation]], [[Decapsulation]] et [[PDU]] ;
- utiliser le modèle OSI comme méthode simple de diagnostic réseau.

---

## Fonctionnement

Le modèle OSI sépare une communication réseau en couches. Chaque couche fournit un service à la couche située au-dessus et utilise les services de la couche située en dessous.

Lorsqu'une application envoie des données, l'information descend les couches OSI. Chaque couche ajoute les informations nécessaires à son rôle : port TCP/UDP, adresse IP, adresse MAC, puis transmission sous forme de bits.

Lorsque la machine destinataire reçoit les données, le processus inverse se produit. Les informations sont lues et retirées progressivement jusqu'à livrer les données à l'application.

---

## Concepts clés

- [[OSI Layer 1 - Physical]]
- [[OSI Layer 2 - Data Link]]
- [[OSI Layer 3 - Network]]
- [[OSI Layer 4 - Transport]]
- [[OSI Layer 5 - Session]]
- [[OSI Layer 6 - Presentation]]
- [[OSI Layer 7 - Application]]
- [[Encapsulation]]
- [[Decapsulation]]
- [[PDU]]
- [[TCP-IP Model]]
- [[Ethernet]]
- [[MAC Address]]
- [[IPv4]]
- [[IPv6]]
- [[ARP]]

---

## Les 7 couches OSI

| Couche | Nom | Rôle | Exemple | PDU / unité de données |
| ------ | --- | ---- | ------- | ---------------------- |
| 7 | Application | Fournit les services réseau visibles par les applications utilisateur. | HTTP, HTTPS, DNS, SMTP | Données |
| 6 | Presentation | Gère le format des données, l'encodage, la compression et le chiffrement. | TLS, formats texte, encodage | Données |
| 5 | Session | Établit, maintient et termine les dialogues logiques entre applications. | Session applicative, reprise de dialogue | Données |
| 4 | Transport | Assure la communication de bout en bout entre processus. | TCP, UDP, ports | Segment TCP ou datagramme UDP |
| 3 | Network | Gère l'adressage logique et le routage entre réseaux. | [[IPv4]], [[IPv6]], routeur | Paquet |
| 2 | Data Link | Gère la livraison locale sur le même lien réseau. | [[Ethernet]], [[MAC Address]], VLAN | Trame |
| 1 | Physical | Transporte les bits sur le support physique. | Câble cuivre, fibre, ondes radio | Bits |

Note CCNA : [[ARP]] est souvent étudié à la frontière entre la couche 2 et la couche 3, car il associe une adresse [[IPv4]] à une adresse [[MAC Address]] pour permettre la livraison locale.

---

## Encapsulation et décapsulation

Quand une donnée part d'une application vers le réseau, elle descend les couches OSI : application -> présentation -> session -> transport -> réseau -> liaison de données -> physique.

Ce processus s'appelle l'[[Encapsulation]]. Chaque couche ajoute ses propres informations :

- la couche 4 ajoute par exemple les ports TCP ou UDP ;
- la couche 3 ajoute les adresses IP ;
- la couche 2 ajoute les adresses MAC ;
- la couche 1 transmet les bits sur le support.

L'unité manipulée par une couche est appelée [[PDU]]. Selon la couche, on parle de données, segment, paquet, trame ou bits.

À la réception, le processus inverse s'appelle la [[Decapsulation]]. La machine destinataire lit les informations couche par couche et remonte jusqu'à l'application.

---

## OSI vs TCP/IP

Le modèle OSI est un modèle de référence en 7 couches. Il est très utile pour apprendre, expliquer et diagnostiquer.

Le [[TCP-IP Model]] est le modèle utilisé pratiquement sur Internet. Il est plus proche des protocoles réellement déployés. Certaines couches OSI sont regroupées dans TCP/IP : par exemple, les fonctions application, présentation et session sont souvent représentées ensemble dans la couche application TCP/IP.

Il ne faut donc pas voir OSI et TCP/IP comme deux réseaux différents. OSI est surtout une grille d'analyse ; TCP/IP décrit plus directement la pile de protocoles utilisée dans les communications modernes.

| Modèle OSI | Équivalent courant dans TCP/IP |
| ---------- | ------------------------------ |
| Application, Presentation, Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link, Physical | Network Access |

---

## Architecture

Vue logique descendante lors de l'envoi :

```text
Application        Données applicatives
Presentation       Format, chiffrement, encodage
Session            Dialogue logique
Transport          TCP/UDP, ports
Network            IP, routage
Data Link          Ethernet, MAC, VLAN
Physical           Bits sur câble, fibre ou radio
```

Vue logique remontante lors de la réception :

```text
Physical -> Data Link -> Network -> Transport -> Session -> Presentation -> Application
```

---

## Exemple concret

Un utilisateur ouvre `https://tiansemi.github.io/` dans son navigateur.

| Couche OSI | Ce qui se passe |
| ---------- | --------------- |
| 7 Application | Le navigateur utilise HTTP/HTTPS pour demander la page web. |
| 6 Presentation | Le chiffrement TLS protège les données échangées. |
| 5 Session | La logique de session est généralement prise en charge par l'application ou par les bibliothèques utilisées. |
| 4 Transport | TCP établit une connexion fiable vers le serveur, généralement sur le port 443. |
| 3 Network | IP transporte les paquets entre le réseau de l'utilisateur et le serveur. |
| 2 Data Link | [[Ethernet]] ou Wi-Fi livre les trames sur le lien local avec des adresses [[MAC Address]]. |
| 1 Physical | Les bits passent sur un câble, une fibre optique ou des ondes radio. |

Si la page ne s'ouvre pas, le modèle OSI aide à poser les bonnes questions : le câble est-il connecté ? Le VLAN est-il correct ? L'adresse IP est-elle valide ? Le DNS répond-il ? Le port 443 est-il bloqué ? Le service web est-il disponible ?

---

## Cisco CLI

Non applicable directement : le modèle OSI est un modèle conceptuel. En revanche, certaines commandes permettent de diagnostiquer des problèmes associés à certaines couches. Ces commandes ne configurent pas le modèle OSI ; elles aident seulement à vérifier des symptômes classés par couche.

| Couche OSI | Objectif de diagnostic | Commande Cisco utile |
| ---------- | ---------------------- | -------------------- |
| Layer 1 | Vérifier l'état physique et opérationnel des interfaces. | `show interfaces` ou `show interfaces status` sur switch |
| Layer 2 | Vérifier l'apprentissage des adresses MAC. | `show mac address-table` |
| Layer 2 | Vérifier les VLANs présents et les ports associés. | `show vlan brief` |
| Layer 3 | Vérifier les interfaces IP et leur état. | `show ip interface brief` |
| Layer 3 | Vérifier les routes connues par l'équipement. | `show ip route` |
| Layer 4 | Vérifier si une ACL peut bloquer TCP ou UDP. | `show access-lists` |

Pour la couche 4, `show access-lists` ne prouve pas qu'un service écoute sur un port. La commande aide surtout à vérifier si une règle peut bloquer un flux TCP ou UDP. Il faut compléter avec un test de connectivité de bout en bout si nécessaire.

---

## Huawei CLI

Non applicable directement : le modèle OSI est un modèle conceptuel. En revanche, certaines commandes Huawei permettent de diagnostiquer des problèmes associés à certaines couches. Elles ne configurent pas le modèle OSI ; elles servent à observer l'état du réseau.

| Couche OSI | Objectif de diagnostic | Commande Huawei utile |
| ---------- | ---------------------- | --------------------- |
| Layer 1 | Vérifier l'état physique et opérationnel des interfaces. | `display interface` ou `display interface brief` |
| Layer 2 | Vérifier l'apprentissage des adresses MAC. | `display mac-address` |
| Layer 2 | Vérifier les VLANs présents. | `display vlan` |
| Layer 3 | Vérifier les interfaces IP et leur état. | `display ip interface brief` |
| Layer 3 | Vérifier les routes connues par l'équipement. | `display ip routing-table` |
| Layer 4 | Vérifier si une ACL peut bloquer TCP ou UDP. | `display acl all` |

Comme côté Cisco, `display acl all` sert à inspecter les règles de filtrage. Cette commande ne remplace pas un test applicatif ou un test de port depuis un hôte.

---

## Wireshark

Wireshark permet d'observer une partie des couches OSI selon le trafic capturé. On peut généralement analyser les couches 2 à 7 : trames Ethernet, paquets IP, segments TCP, datagrammes UDP et protocoles applicatifs comme DNS, HTTP ou TLS.

Attention : si le trafic est chiffré avec TLS, Wireshark peut montrer la négociation TLS et les métadonnées visibles, mais pas forcément le contenu applicatif en clair.

Exemples de filtres utiles :

```text
arp
ip
tcp
udp
dns
http
tls
```

Wireshark ne remplace pas les commandes réseau. Il complète le diagnostic en montrant ce qui circule réellement sur le réseau.

---

## Troubleshooting

| Couche OSI | Problème | Cause probable | Solution |
| ---------- | -------- | -------------- | -------- |
| Layer 1 | Interface down | Câble débranché, port désactivé, problème de support | Vérifier câble, LED, port, état interface |
| Layer 2 | Mauvais VLAN | Port placé dans un VLAN incorrect | Vérifier l'association port/VLAN |
| Layer 2 | Problème MAC | Adresse MAC non apprise ou table MAC incohérente | Vérifier la table MAC et le chemin de commutation |
| Layer 3 | Mauvaise IP, mauvais masque ou mauvaise passerelle | Paramètres IP incorrects sur l'hôte | Vérifier IP, masque, gateway et plan d'adressage |
| Layer 3 | Route manquante | Le routeur ne connaît pas le réseau de destination | Vérifier la table de routage et les routes statiques/dynamiques |
| Layer 4 | Port TCP/UDP bloqué | ACL, pare-feu ou service qui n'écoute pas | Vérifier ACL, pare-feu et port applicatif |
| Layer 7 | Service applicatif indisponible | Serveur web, DNS ou application en panne | Vérifier service, DNS, logs et disponibilité serveur |

---

## Bonnes pratiques

- Commencer par une hypothèse simple avant d'exécuter des commandes.
- Vérifier les couches basses avant de conclure à une panne applicative.
- Distinguer clairement adresse [[MAC Address]], adresse [[IPv4]] ou [[IPv6]], port TCP/UDP et protocole applicatif.
- Utiliser le modèle OSI comme méthode de diagnostic, pas comme une configuration.
- Croiser les observations : état interface, table MAC, table de routage, ACL et capture Wireshark.

---

## Erreurs fréquentes

1. Confondre OSI et TCP/IP.
2. Croire que chaque protocole correspond toujours parfaitement à une seule couche.
3. Analyser la couche 3 alors que le problème est en couche 1.
4. Confondre adresse MAC et adresse IP.
5. Ignorer le rôle du VLAN.
6. Oublier la passerelle par défaut.
7. Utiliser des commandes sans hypothèse de diagnostic.

---

## Questions d'entretien

1. **Question : Que signifie OSI ?**  
   Réponse attendue : OSI signifie Open Systems Interconnection. C'est un modèle de référence qui décrit la communication réseau en 7 couches.

2. **Question : Pourquoi le modèle OSI est-il utile en troubleshooting ?**  
   Réponse attendue : Il permet de structurer le diagnostic couche par couche, depuis le support physique jusqu'à l'application, au lieu de chercher au hasard.

3. **Question : Quelle est la différence entre OSI et TCP/IP ?**  
   Réponse attendue : OSI est un modèle de référence en 7 couches ; TCP/IP est le modèle pratique utilisé sur Internet, avec des couches regroupées différemment.

4. **Question : Quelle couche OSI est associée au routage IP ?**  
   Réponse attendue : La couche 3, Network, car elle gère l'adressage logique et le routage entre réseaux.

5. **Question : Quelle couche OSI est associée aux adresses MAC et aux VLANs ?**  
   Réponse attendue : La couche 2, Data Link, car elle gère la livraison locale des trames sur un même lien réseau.

---

## Quiz

1. **Quel est le rôle principal du modèle OSI ?**
   - A. Configurer automatiquement les routeurs
   - B. Décrire les fonctions réseau sous forme de couches
   - C. Remplacer le protocole TCP/IP
   - D. Chiffrer les communications web
   - Réponse : B
   - Explication : OSI est un modèle de référence qui aide à comprendre et diagnostiquer les communications réseau.

2. **Quelle couche OSI est principalement liée aux adresses IP ?**
   - A. Layer 1 Physical
   - B. Layer 2 Data Link
   - C. Layer 3 Network
   - D. Layer 7 Application
   - Réponse : C
   - Explication : La couche Network gère l'adressage logique et le routage, notamment avec IPv4 et IPv6.

3. **Quelle unité de données est associée à la couche Data Link ?**
   - A. Bit
   - B. Trame
   - C. Paquet
   - D. Segment
   - Réponse : B
   - Explication : La couche 2 manipule des trames, par exemple des trames Ethernet.

4. **Un PC a une bonne adresse IP, mais il est dans le mauvais VLAN. Quelle couche faut-il examiner en priorité ?**
   - A. Layer 1 Physical
   - B. Layer 2 Data Link
   - C. Layer 4 Transport
   - D. Layer 7 Application
   - Réponse : B
   - Explication : Le VLAN appartient à la couche Data Link. Un mauvais VLAN peut empêcher la communication même si l'adresse IP semble correcte.

5. **Si un câble est débranché, quelle couche faut-il vérifier en premier ?**
   - A. Layer 1 Physical
   - B. Layer 3 Network
   - C. Layer 4 Transport
   - D. Layer 7 Application
   - Réponse : A
   - Explication : Le câble, le signal et l'état physique d'une interface relèvent de la couche Physical.

---

## Flashcards

Q: Que signifie OSI ?  
A: Open Systems Interconnection.

Q: Combien de couches possède le modèle OSI ?  
A: 7 couches.

Q: Quelle couche OSI gère les bits sur le support physique ?  
A: Layer 1 Physical.

Q: Quelle couche OSI gère les adresses MAC ?  
A: Layer 2 Data Link.

Q: Quelle couche OSI gère le routage IP ?  
A: Layer 3 Network.

Q: Quelle couche OSI utilise TCP et UDP ?  
A: Layer 4 Transport.

Q: Quelle couche OSI est associée à HTTP et DNS ?  
A: Layer 7 Application.

Q: Qu'est-ce que l'encapsulation ?  
A: Le processus qui ajoute des informations de couche lorsque les données descendent la pile réseau.

Q: Qu'est-ce qu'une PDU ?  
A: L'unité de données manipulée par une couche OSI.

Q: Pourquoi utiliser OSI en dépannage ?  
A: Pour isoler un problème réseau couche par couche.

Q: Le modèle OSI est-il une configuration réseau ?  
A: Non. C'est un modèle conceptuel utilisé pour comprendre et diagnostiquer.

Q: Quel modèle décrit le plus directement les protocoles utilisés sur Internet ?  
A: Le modèle TCP/IP.

---

## Labs

Mini-lab Packet Tracer : diagnostic OSI simple.

### Topologie

- 2 PCs
- 1 switch
- 1 routeur

### Objectif

Diagnostiquer une panne réseau en suivant les couches OSI, sans partir directement sur une commande au hasard.

### Étapes

1. Construire une topologie avec deux PCs connectés au switch, et le switch connecté au routeur.
2. Configurer un adressage IP simple sur les PCs et l'interface du routeur.
3. Introduire volontairement une panne simple : câble déconnecté, mauvais VLAN, mauvaise passerelle ou mauvais masque.
4. Diagnostiquer en partant de la couche 1 :
   - câble connecté ?
   - interface up ?
   - VLAN correct ?
   - adresse IP correcte ?
   - passerelle correcte ?
   - ping local puis ping passerelle ?
5. Corriger la panne.
6. Documenter la couche où se trouvait le problème.

### Pannes simples à tester

| Panne | Couche principale | Indice attendu |
| ----- | ----------------- | -------------- |
| Câble déconnecté | Layer 1 | Interface down ou lien rouge dans Packet Tracer |
| Mauvais VLAN | Layer 2 | Les hôtes ne communiquent pas malgré un câblage correct |
| Mauvais masque | Layer 3 | L'hôte croit que la destination est locale ou distante à tort |
| Mauvaise passerelle | Layer 3 | Le ping local fonctionne, mais pas la sortie vers un autre réseau |

### Questions de validation

- Quelle couche OSI était concernée par la panne ?
- Quelle commande ou observation a permis de confirmer l'hypothèse ?
- Pourquoi fallait-il vérifier les couches basses avant d'accuser l'application ?

---

## Références

- Cisco CCNA 200-301 Official Cert Guide.
- Cisco Networking Academy — CCNA Introduction to Networks.
- ISO/IEC 7498-1, à vérifier si nécessaire.

---

## Contenus générés

| Canal         | Statut     | Lien |
| ------------- | ---------- | ---- |
| Site TianSemi | À générer  |      |
| Blog          | À générer  |      |
| Newsletter    | À générer  |      |
