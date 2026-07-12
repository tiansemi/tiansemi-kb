---
id: HUA-HCIA-DC-007
title: "Huawei Network Device Operating Systems"
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
  - vrp
  - yunshan-os
  - cli
  - configuration-management
keywords:
  - Huawei VRP
  - YunShan OS
  - console login
  - STelnet
  - command views
  - file system
  - configuration file
  - startup configuration
prerequisites:
  - "Data Communication Network Devices"
  - "Network Engineering and Network Engineers"
related:
  - "Logging In to Network Devices"
  - "Configuring Network Devices"
  - "Network Reference Models"
commands:
  - "display version"
  - "system-view"
  - "sysname"
  - "display current-configuration"
  - "display saved-configuration"
  - "display startup"
  - "display this"
  - "dir"
  - "pwd"
  - "save"
  - "startup saved-configuration"
  - "reboot"
labs:
  - "01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Huawei Network Device Operating Systems

## Résumé

> Un système d'exploitation réseau gère les ressources matérielles et logicielles d'un équipement et fournit les fonctions de configuration, de supervision, de sécurité et de maintenance. Les équipements Huawei Datacom utilisent notamment YunShan OS ou VRP. L'administrateur y accède par console, Telnet, STelnet ou interface web, puis travaille dans des vues CLI hiérarchiques. Maîtriser les fichiers, la configuration courante, la sauvegarde et la configuration du prochain démarrage est indispensable pour éviter les pertes de service.

---

## Objectifs officiels couverts

Cette note couvre les objectifs du chapitre Huawei « Network Device Operating Systems » :

- comprendre le rôle d'un système d'exploitation et d'un système d'exploitation réseau ;
- identifier YunShan OS et VRP dans l'écosystème Huawei Datacom ;
- distinguer connexion locale, connexion distante et interface web ;
- configurer une session console avec les paramètres série corrects ;
- comprendre les interfaces console et VTY ;
- utiliser la structure des commandes, les vues, l'aide et les commandes d'annulation ;
- connaître les niveaux de privilège et leurs implications ;
- effectuer les opérations de base sur les fichiers et répertoires ;
- distinguer configuration courante, sauvegardée, prédéfinie et prochain démarrage ;
- sauvegarder, vérifier et sélectionner un fichier de configuration ;
- appliquer les procédures du lab officiel « Basic Operations on Huawei Network Devices ».

---

## Explication simple

Un routeur ou un switch est un ordinateur spécialisé. Son matériel fournit des ports, de la mémoire et des capacités de transfert ; son système d'exploitation coordonne ces ressources et expose une interface d'administration.

```text
Administrateur
    -> console / STelnet / interface web
        -> CLI ou GUI Huawei
            -> YunShan OS ou VRP
                -> matériel, interfaces, protocoles, fichiers et configuration
```

La CLI organise les commandes par contexte. Le prompt indique la vue actuelle :

```text
<HUAWEI>              vue utilisateur
[HUAWEI]              vue système
[HUAWEI-GE1/0/1]      vue d'interface
[HUAWEI-ospf-1]       vue de protocole
```

Une modification est d'abord active dans la configuration courante. Elle doit être vérifiée puis sauvegardée pour survivre à un redémarrage.

---

## Détails techniques

### Rôle d'un système d'exploitation

Un système d'exploitation gère et coordonne les ressources matérielles et logicielles. Sur un équipement réseau, il fournit notamment :

- la gestion des interfaces et du matériel ;
- l'exécution des protocoles réseau ;
- la configuration et la supervision ;
- le contrôle des accès et des privilèges ;
- la gestion des fichiers, journaux, correctifs et logiciels ;
- les interfaces CLI et web destinées aux administrateurs.

### YunShan OS et VRP

Huawei présente YunShan OS et VRP comme des systèmes d'exploitation de ses équipements Datacom. Selon la gamme et la version, le nom et certaines fonctions peuvent varier. Il faut donc toujours relever le modèle et la version avant d'appliquer une procédure.

```text
display version
```

Le support de cours montre notamment une sortie YunShan OS sur un routeur de lab et une sortie VRP sur un switch. Les commandes fondamentales suivent une logique cohérente, mais la documentation du modèle reste la référence en cas de différence.

### Méthodes de connexion

| Méthode | Type | Usage | Sécurité et prérequis |
| --- | --- | --- | --- |
| Console | local | première mise en service, récupération, maintenance locale | câble console et accès physique |
| Telnet | distant | accès CLI historique | trafic non chiffré ; à éviter en production |
| STelnet | distant | accès CLI sécurisé sur SSH | adresse de gestion, routage, comptes et clés/configuration SSH |
| Interface web | local ou distant selon le réseau | administration graphique | adresse de gestion, service web et authentification |

Les connexions distantes utilisent des interfaces utilisateur virtuelles VTY. Le support indique jusqu'à 21 utilisateurs VTY dans l'exemple présenté. L'interface console correspond à l'accès local et un seul utilisateur s'y connecte à la fois.

### Connexion initiale par console

La console est la méthode normale lors de la première mise en service. Le terminal est relié au port console de l'équipement, directement ou avec un adaptateur USB-série.

Paramètres série par défaut présentés par Huawei :

| Paramètre | Valeur |
| --- | --- |
| Débit | 9600 bit/s |
| Bits de données | 8 |
| Bits d'arrêt | 1 |
| Parité | aucune |
| Contrôle de flux | aucun |

Lors de la première connexion, l'équipement demande de définir un mot de passe de connexion. Le support de lab affiche une longueur attendue de 8 à 16 caractères. Utiliser un secret unique et conforme à la politique de l'organisation ; ne pas recopier le mot de passe d'exemple du support.

Après la première connexion, les paramètres essentiels à établir sont notamment le nom de l'équipement, l'heure et l'adresse de gestion adaptée au modèle et au plan réseau.

### Structure d'une commande Huawei

Une commande peut contenir :

- un **mot de commande**, par exemple `display` ou `reboot` ;
- un ou plusieurs **mots-clés** qui précisent l'action ;
- des **paramètres** et leurs valeurs.

Exemple du cours :

```text
display ip interface GE1/0/1
```

Les éléments sont séparés par des espaces. La syntaxe disponible dépend de la vue, du niveau de privilège, du modèle et de la version logicielle.

### Vues de commande

| Vue | Prompt type | Usage |
| --- | --- | --- |
| Utilisateur | `<HUAWEI>` | consultation, outils de diagnostic et opérations de maintenance |
| Système | `[HUAWEI]` | paramètres globaux et accès aux vues de configuration |
| Interface | `[HUAWEI-GE1/0/1]` | paramètres propres à une interface |
| Protocole | `[HUAWEI-ospf-1]` | paramètres d'un protocole ou d'un processus |
| Zone OSPF | `[HUAWEI-ospf-1-area-0.0.0.0]` | paramètres d'une zone OSPF |

Navigation de base :

```text
<HUAWEI> system-view
[HUAWEI] interface GE1/0/1
[HUAWEI-GE1/0/1] quit
[HUAWEI] return
<HUAWEI>
```

- `quit` revient à la vue immédiatement supérieure ;
- `return` revient directement à la vue utilisateur ;
- le prompt constitue une preuve importante de la vue dans laquelle la commande sera appliquée.

### Aide, complétion et annulation

La CLI fournit une aide contextuelle :

- `?` affiche les commandes ou paramètres possibles ;
- `Tab` complète un mot-clé lorsqu'il est non ambigu ou parcourt les possibilités ;
- une commande précédée de `undo` annule généralement la configuration correspondante ;
- `display this` montre la configuration effective de la vue courante ;
- `display current-configuration` montre la configuration courante de l'équipement.

Exemple du lab :

```text
[HUAWEI] interface GE0/0/1
[HUAWEI-GE0/0/1] display this
[HUAWEI-GE0/0/1] quit
```

Ne pas supposer qu'un `undo` est sans impact. Vérifier la vue et la fonction avant de l'exécuter.

### Niveaux de privilège

Le cours présente quatre niveaux par défaut, de 0 à 3 :

| Niveau | Catégorie générale | Exemples de capacités |
| --- | --- | --- |
| 0 | visite | certains diagnostics comme `ping`, `tracert` et quelques affichages |
| 1 | monitoring | maintenance et commandes d'affichage |
| 2 | configuration | configuration de services réseau |
| 3 | management | opérations système, fichiers, transferts et débogage |

Les droits exacts peuvent varier selon le produit et la version. Huawei déconseille de modifier les niveaux de privilège par défaut sans besoin précis, car une mauvaise délégation augmente le risque de sécurité.

### Système de fichiers

Le système de fichiers stocke et organise plusieurs catégories de fichiers :

| Type | Rôle | Extensions citées dans le cours |
| --- | --- | --- |
| Logiciel système | démarrage et fonctions de l'équipement | `.cc` |
| Correctif | correction ciblée compatible avec le logiciel | `.pat` |
| Configuration | commandes et données de démarrage | `.cfg`, `.zip`, `.dat`, `.defcfg` selon l'usage |

Les supports possibles incluent SDRAM, NVRAM, flash, carte SD et support USB selon l'équipement. La flash est non volatile et stocke couramment logiciels et configurations.

Commandes locales de base :

| Opération | Commande |
| --- | --- |
| afficher le répertoire courant | `pwd` |
| lister les fichiers | `dir` |
| changer de répertoire | `cd <répertoire>` |
| créer un répertoire | `mkdir <répertoire>` |
| afficher un fichier texte | `more <fichier>` |
| copier un fichier | `copy <source> <destination>` |
| déplacer ou renommer | `move ...` ou `rename ...` |

Les suppressions et restaurations de fichiers doivent être réalisées avec prudence, après vérification du chemin, de l'espace disponible et d'une sauvegarde.

### Méthodes de gestion et de transfert de fichiers

Huawei distingue la gestion locale et plusieurs protocoles de transfert : TFTP, FTP, SFTP et SCP. TFTP et FTP ne fournissent pas le même niveau de sécurité que SFTP ou SCP. Pour un environnement réel, choisir une méthode sécurisée conforme à la politique d'exploitation.

### États de configuration

| État | Signification |
| --- | --- |
| Paramètres usine | configuration fournie par défaut avec l'équipement |
| Configuration prédéfinie | paramètres issus d'un fichier `.defcfg` prévu pour l'initialisation |
| Configuration courante | commandes actuellement actives en mémoire |
| Configuration sauvegardée | contenu écrit dans un fichier de configuration |
| Configuration du prochain démarrage | fichier que le système chargera au redémarrage |

La distinction la plus importante est celle-ci :

```text
configuration courante --save--> fichier sauvegardé
fichier sélectionné --redémarrage--> configuration du prochain démarrage
```

### Vérifier et sauvegarder la configuration

| Commande | Fonction |
| --- | --- |
| `display current-configuration` | affiche la configuration active |
| `display this` | affiche la configuration active de la vue courante |
| `display saved-configuration` | affiche la configuration sauvegardée |
| `display startup` | affiche les logiciels et fichiers prévus au prochain démarrage |
| `dir` | confirme la présence des fichiers dans le stockage |
| `save` | sauvegarde la configuration courante |
| `save <fichier>` | sauvegarde vers un fichier nommé compatible |
| `startup saved-configuration <fichier>` | choisit le fichier du prochain démarrage |

Avant un redémarrage, vérifier au minimum :

```text
display current-configuration
save
display saved-configuration
display startup
```

### Commandes à impact élevé

Les commandes suivantes ne doivent pas être exécutées dans un réseau de production sans procédure approuvée :

- `reboot` ou `reboot fast` redémarre l'équipement ;
- `reset saved-configuration` efface la configuration prévue pour le prochain démarrage ;
- `reset factory-configuration` restaure les paramètres usine et efface un périmètre plus large de données et configurations.

Le lab officiel les présente dans un environnement contrôlé. Leur étude ne constitue pas une autorisation d'usage sur un équipement actif.

---

## À retenir pour l'examen HCIA

- YunShan OS et VRP sont des systèmes d'exploitation de produits Huawei Datacom.
- La console fournit un accès local, notamment pour la première configuration.
- Les paramètres console sont 9600 bit/s, 8 bits de données, 1 bit d'arrêt, sans parité et sans contrôle de flux.
- Telnet n'est pas chiffré ; STelnet fournit une connexion plus sûre.
- La vue utilisateur utilise `< >` ; les vues de configuration utilisent `[ ]`.
- `system-view` entre dans la vue système, `quit` remonte d'une vue et `return` revient à la vue utilisateur.
- `?` fournit l'aide et `Tab` la complétion contextuelle.
- `undo` annule généralement la configuration correspondante.
- La configuration courante n'est pas automatiquement persistante ; `save` est indispensable après validation.
- `display startup` permet de vérifier le fichier prévu au prochain démarrage.
- Les fichiers logiciels, correctifs et configurations ont des rôles et extensions différents.
- Les commandes de reset et de reboot ont un impact élevé et exigent une procédure maîtrisée.

---

## Commandes Huawei utiles

### Identification et navigation

```text
display version
system-view
sysname <nom-equipement>
quit
return
```

### Vérification de configuration

```text
display this
display current-configuration
display saved-configuration
display startup
```

### Fichiers et persistance

```text
pwd
dir
more <fichier>
save
startup saved-configuration <fichier>
```

### Bon réflexe

Toujours vérifier le prompt, la syntaxe avec `?`, l'état courant et l'espace de stockage avant une opération de fichier, une sauvegarde ou un redémarrage.

---

## Pratique obligatoire

### Objectif

Se connecter par console, naviguer dans la CLI, appliquer une configuration de base, la vérifier et la sauvegarder.

### Topologie

```text
PC d'administration ---- câble console ---- Routeur Huawei
                                      |
                                      +---- GE0/0/1 ---- réseau de test
```

### Préparation

1. Identifier le bon port COM dans le gestionnaire de périphériques.
2. Configurer la session série en 9600-8-N-1, sans contrôle de flux.
3. Ouvrir la session et appuyer sur Entrée.
4. Définir un mot de passe initial conforme à la politique du lab.

### Configuration et vérification

```text
<HUAWEI> display version
<HUAWEI> system-view
[HUAWEI] sysname Datacom-Router
[Datacom-Router] interface GE0/0/1
[Datacom-Router-GE0/0/1] display this
[Datacom-Router-GE0/0/1] quit
[Datacom-Router] display current-configuration
[Datacom-Router] return
<Datacom-Router> save
<Datacom-Router> display startup
```

L'adressage exact et la commande nécessaire pour transformer une interface de couche 2 en interface routée dépendent du modèle utilisé dans le lab. Suivre la procédure du Lab Guide correspondant à l'équipement.

### Vérification

- le nom du prompt doit refléter le `sysname` ;
- `display current-configuration` doit contenir la modification ;
- `save` doit confirmer la sauvegarde ;
- `display startup` doit identifier le fichier prévu au prochain démarrage.

### Résultat attendu

L'apprenant doit être capable de quitter et retrouver chaque vue sans confusion, d'expliquer la différence entre courant et sauvegardé, puis de fournir une preuve de persistance sans redémarrer l'équipement.

---

## Troubleshooting

| Symptôme | Cause probable | Vérification | Correction |
| --- | --- | --- | --- |
| Aucun prompt console | mauvais port COM, câble ou paramètres série | gestionnaire de périphériques et paramètres 9600-8-N-1 | sélectionner le port et les paramètres corrects |
| Caractères illisibles | débit ou format série incorrect | comparer les paramètres du terminal | corriger la session série |
| Commande inconnue | mauvaise vue, syntaxe ou version | observer le prompt, utiliser `?` et `display version` | entrer dans la bonne vue ou adapter la syntaxe |
| Accès refusé à une commande | niveau de privilège insuffisant | vérifier le compte et la politique d'accès | utiliser un compte autorisé sans élargir inutilement les droits |
| Configuration visible mais perdue après redémarrage | `save` non exécuté ou mauvais fichier de startup | `display saved-configuration`, `display startup` | sauvegarder et sélectionner le bon fichier |
| STelnet inaccessible | adresse, route, service SSH ou VTY incorrect | tester l'IP, la route et la configuration d'accès | corriger la gestion réseau et l'authentification |
| Espace insuffisant pour une copie ou une sauvegarde | stockage plein | `dir` et informations de stockage | archiver ou supprimer uniquement selon procédure |
| Mauvais fichier chargé au démarrage | sélection de startup incorrecte | `display startup` | choisir le fichier validé et revérifier avant reboot |

### Méthode de récupération prudente

1. Ne pas redémarrer tant que l'état courant n'est pas compris.
2. Collecter `display version`, `display current-configuration`, `display saved-configuration` et `display startup`.
3. Vérifier la présence et le nom des fichiers avec `dir`.
4. Comparer courant, sauvegardé et prochain démarrage.
5. Corriger la sélection ou sauvegarder après validation.
6. Ne redémarrer que dans une fenêtre approuvée avec rollback disponible.

---

## Mini-lab TianSemi

### Titre

Baseline et persistance d'un équipement Huawei.

### Scénario

Un routeur neuf doit être préparé pour une équipe d'exploitation. L'objectif n'est pas de déployer un service avancé, mais d'obtenir un équipement identifiable, accessible localement et correctement sauvegardé.

### Travail demandé

1. Se connecter par console.
2. Relever le modèle, le logiciel et le temps de fonctionnement.
3. Configurer un `sysname` respectant la convention du site.
4. Explorer l'aide contextuelle avec `?` et la complétion avec `Tab`.
5. Entrer dans une vue d'interface puis revenir à la vue utilisateur.
6. Comparer `display this` et `display current-configuration`.
7. Lister les fichiers avec `dir`.
8. Sauvegarder avec `save`.
9. Vérifier `display saved-configuration` et `display startup`.
10. Documenter les résultats sans exécuter de commande de reset ou de reboot.

### Critères de réussite

- aucune commande destructive n'est utilisée ;
- chaque commande est exécutée dans la vue correcte ;
- le nom de l'équipement et la sauvegarde sont vérifiés ;
- le fichier du prochain démarrage est identifié ;
- la fiche de baseline permet une reprise par un autre ingénieur.

---

## Questions d'entretien

1. Quel est le rôle d'un système d'exploitation réseau ?
2. Que sont YunShan OS et VRP ?
3. Quelle différence existe entre console, Telnet et STelnet ?
4. Quels paramètres utilisez-vous pour une connexion console Huawei par défaut ?
5. Comment reconnaissez-vous la vue système et la vue utilisateur ?
6. Quelle différence existe entre `quit` et `return` ?
7. Comment vérifiez-vous la configuration courante et la configuration sauvegardée ?
8. Pourquoi `save` est-il critique ?
9. Que vérifie `display startup` ?
10. Pourquoi faut-il traiter `reset factory-configuration` comme une commande à impact élevé ?

---

## Quiz

### 1. Quel accès est normalement utilisé pour une première mise en service locale ?

- A. Console
- B. HTTP public
- C. FTP anonyme
D. Aucun accès

**Réponse : A.**

### 2. Quel protocole distant est plus sûr que Telnet ?

- A. TFTP
- B. STelnet
- C. ICMP
D. ARP

**Réponse : B.**

### 3. Quels sont les paramètres série par défaut présentés dans le cours ?

- A. 9600, 8 bits, 1 stop, sans parité, sans contrôle de flux
- B. 1000, 7 bits, 2 stops, parité paire
- C. DHCP automatique
D. Aucun paramètre

**Réponse : A.**

### 4. Quel prompt représente la vue utilisateur ?

- A. `[HUAWEI]`
- B. `<HUAWEI>`
- C. `(HUAWEI)`
D. `{HUAWEI}`

**Réponse : B.**

### 5. Quelle commande entre dans la vue système ?

- A. `system-view`
- B. `save`
- C. `dir`
D. `ping`

**Réponse : A.**

### 6. Quelle commande affiche la configuration active de la vue courante ?

- A. `display this`
- B. `reset saved-configuration`
- C. `reboot fast`
D. `mkdir`

**Réponse : A.**

### 7. Pourquoi exécute-t-on `save` ?

- A. Pour rendre la configuration persistante
- B. Pour effacer le logiciel
- C. Pour ouvrir une session Telnet
D. Pour changer le câble

**Réponse : A.**

### 8. Quelle commande vérifie le fichier du prochain démarrage ?

- A. `display startup`
- B. `sysname`
- C. `ping`
D. `undo`

**Réponse : A.**

### 9. Quel type de fichier contient couramment une configuration Huawei ?

- A. `.cfg` ou `.zip` selon le format
- B. `.jpg` uniquement
- C. `.mp3`
D. Aucun fichier

**Réponse : A.**

### 10. Quelle commande doit être étudiée mais jamais lancée sans procédure contrôlée ?

- A. `display version`
- B. `pwd`
- C. `reset factory-configuration`
D. `display this`

**Réponse : C.**

---

## Flashcards

**Q : Quel est le rôle de VRP ou YunShan OS ?**

R : Gérer le matériel, les protocoles, la configuration, la sécurité et la maintenance de l'équipement.

**Q : Quelle méthode permet la première connexion locale ?**

R : La connexion par le port console.

**Q : Quels sont les paramètres console par défaut du cours ?**

R : 9600 bit/s, 8 bits de données, 1 bit d'arrêt, sans parité et sans contrôle de flux.

**Q : Qu'est-ce qu'une interface VTY ?**

R : Une interface utilisateur virtuelle utilisée pour les connexions CLI distantes comme Telnet ou STelnet.

**Q : Quelle commande entre en vue système ?**

R : `system-view`.

**Q : Quelle commande revient directement en vue utilisateur ?**

R : `return`.

**Q : Quelle commande affiche la configuration active complète ?**

R : `display current-configuration`.

**Q : Quelle commande affiche la configuration de la vue courante ?**

R : `display this`.

**Q : Quelle commande sauvegarde la configuration ?**

R : `save`.

**Q : Quelle commande indique le fichier du prochain démarrage ?**

R : `display startup`.

**Q : Quelle différence existe entre courant et sauvegardé ?**

R : Le courant est actif en mémoire ; le sauvegardé est écrit dans un fichier persistant.

**Q : Pourquoi privilégier STelnet ?**

R : Parce qu'il protège mieux la connexion distante grâce à SSH, contrairement à Telnet en clair.

---

## Références

- HCIA-Datacom V2.0 Training Material, chapitre « Network Device Operating Systems », pages PDF 87-152 : systèmes d'exploitation, YunShan OS/VRP, méthodes de connexion, CLI, vues, privilèges, fichiers et configurations.
- HCIA-Datacom V2.0 Lab Guide, lab « Basic Operations on Huawei Network Devices », pages PDF 14-25 : connexion initiale, `display version`, vues, configuration de base, aide, `display this`, sauvegarde, fichiers et redémarrage en environnement contrôlé.
- Huawei Talent Certification page : https://e.huawei.com/en/talent/cert/#/careerCert

---

## Contenus générés

| Canal | Statut | Lien |
| --- | --- | --- |
| Site TianSemi | À générer | |
| Quiz | Intégré à la note | |
