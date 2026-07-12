---
id: HUA-HCIA-DC-004
title: "Network Engineering and Network Engineers"
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
  - network-engineering
  - network-engineer
keywords:
  - network planning
  - network design
  - implementation
  - acceptance testing
  - maintenance
  - troubleshooting
  - optimization
prerequisites:
  - "Data Communication Network"
  - "Data Communication Network Devices"
related:
  - "Data Communication Process"
  - "Network Reference Models"
  - "Huawei Network Device Operating Systems"
commands:
  - "display version"
  - "display device"
  - "display interface brief"
  - "display ip interface brief"
  - "display current-configuration"
  - "display ip routing-table"
  - "ping"
  - "tracert"
  - "save"
labs:
  - "01 Basic Operations on Huawei Network Devices"
assets: []
publication_status: "not-started"
site_url:
---

# Network Engineering and Network Engineers

## Résumé

> L'ingénierie réseau transforme un besoin métier en une infrastructure exploitable. Elle ne se limite pas à configurer des routeurs et des switchs : elle couvre la planification, la conception, l'implémentation, les tests, la mise en service, la maintenance, le dépannage et l'optimisation. L'ingénieur réseau combine donc des compétences techniques, une méthode de projet, une capacité de communication et une discipline de preuve.

---

## Objectifs officiels couverts

Cette note couvre les objectifs introduits par Huawei dans la section consacrée à l'ingénierie réseau et aux ingénieurs réseau :

- définir l'ingénierie réseau et son périmètre ;
- identifier les principales phases d'un projet réseau ;
- comprendre le rôle et les responsabilités d'un ingénieur réseau ;
- distinguer connaissance théorique, savoir-faire opérationnel et capacité à piloter un projet ;
- comprendre le chemin de progression technique, du « quoi » vers le « comment », puis vers les mécanismes de protocole et l'analyse des paquets ;
- relier une exigence métier à une conception, une configuration, une vérification et une preuve d'acceptation.

---

## Explication simple

Construire un réseau ressemble à construire un bâtiment.

Avant de poser le premier câble, il faut savoir qui utilisera le réseau, quelles applications devront fonctionner, quel niveau de disponibilité est attendu, quelles contraintes de sécurité existent et quel budget est disponible. Ensuite seulement viennent le plan, le choix des équipements, l'installation et les tests.

L'ingénieur réseau est la personne qui maintient cette continuité entre le besoin et le résultat :

```text
Besoin métier
    -> exigences techniques
        -> architecture et plan d'adressage
            -> configuration et intégration
                -> tests et acceptation
                    -> exploitation et amélioration
```

Une configuration qui « semble fonctionner » n'est pas suffisante. Elle doit être documentée, vérifiée avec des commandes adaptées et comparée aux critères d'acceptation définis avant le déploiement.

---

## Détails techniques

### Les phases principales de l'ingénierie réseau

| Phase | Question centrale | Livrables typiques | Risque si elle est négligée |
| --- | --- | --- | --- |
| Planification | Pourquoi construire ou faire évoluer le réseau ? | besoins, périmètre, contraintes, calendrier, budget | solution techniquement correcte mais inutile ou trop coûteuse |
| Conception | Comment satisfaire les exigences ? | architecture logique et physique, adressage, protocoles, sécurité, redondance | incohérences, points uniques de panne, croissance difficile |
| Implémentation | Comment déployer sans interrompre le service ? | plan de migration, configurations, sauvegardes, procédure de retour arrière | panne, erreur de configuration, indisponibilité prolongée |
| Test et acceptation | Comment prouver que le résultat répond au besoin ? | plan de test, résultats, écarts, procès-verbal d'acceptation | réseau déclaré opérationnel sans preuve |
| Exploitation et maintenance | Comment maintenir le service ? | supervision, sauvegardes, procédures, inventaire, journal des changements | incidents répétés et diagnostic lent |
| Dépannage | Où se situe la défaillance et quelle est sa cause ? | collecte de faits, hypothèses, correction, validation | modifications au hasard et aggravation de l'incident |
| Optimisation | Comment améliorer performance, disponibilité ou simplicité ? | mesures avant/après, recommandations, plan d'amélioration | complexité croissante et ressources mal utilisées |

### Le rôle de l'ingénieur réseau

Un ingénieur réseau est un professionnel capable de comprendre les technologies, de construire une solution et de collaborer avec les parties prenantes. Son travail se répartit en quatre familles de capacités.

| Capacité | Exemples concrets |
| --- | --- |
| Technique | Ethernet, IP, routage, WLAN, sécurité, services, automatisation |
| Opérationnelle | configurer, vérifier, sauvegarder, diagnostiquer, restaurer |
| Projet | estimer, planifier, gérer les risques, documenter, valider |
| Relationnelle | écouter le client, expliquer un choix, coordonner une intervention, rendre compte |

La qualité professionnelle complète ces capacités : respect des procédures, traçabilité, gestion prudente des accès, protection des données de configuration et communication claire pendant les incidents.

### Le modèle de progression technique

Huawei présente une progression dans laquelle l'ingénieur approfondit progressivement sa compréhension :

1. **Quoi ?** Identifier la fonction : routage, commutation, VLAN, OSPF, ACL.
2. **Comment ?** Savoir configurer, afficher et vérifier cette fonction.
3. **Mécanisme du protocole.** Comprendre pourquoi les voisins se forment, comment une route est choisie ou comment une trame est transférée.
4. **Paquets et mécanismes sous-jacents.** Lire les en-têtes, les états et les échanges qui expliquent le comportement.
5. **Vue globale.** Replacer le mécanisme dans la conception, l'exploitation, le dépannage et l'optimisation du réseau.

Cette progression évite deux pièges : réciter une théorie sans savoir l'appliquer, ou mémoriser des commandes sans comprendre leurs effets.

### Des exigences mesurables

Une exigence utile doit être vérifiable.

| Formulation vague | Reformulation mesurable |
| --- | --- |
| « Le réseau doit être rapide » | Les postes du LAN doivent atteindre le serveur avec une latence inférieure au seuil convenu |
| « Le réseau doit toujours fonctionner » | Le service critique doit disposer d'un chemin de secours et d'un test de bascule documenté |
| « Les utilisateurs doivent être isolés » | Les groupes définis doivent être placés dans des segments distincts avec des règles d'accès vérifiées |
| « La configuration doit être sûre » | Les accès d'administration, les sauvegardes et les comptes doivent respecter la politique validée |

### La preuve d'acceptation

Un test d'acceptation contient au minimum :

- une condition initiale connue ;
- une action reproductible ;
- une commande ou une mesure de vérification ;
- un résultat attendu ;
- un résultat observé ;
- une conclusion : conforme, non conforme ou à corriger.

---

## À retenir pour l'examen HCIA

- L'ingénierie réseau couvre le cycle complet : planifier, concevoir, implémenter, tester, maintenir, dépanner et optimiser.
- Un ingénieur réseau ne se limite pas aux commandes CLI ; il relie besoins, technologies, projet et communication.
- La conception logique décrit notamment les services, protocoles, segments et adresses ; la conception physique décrit notamment les équipements, ports, câbles et emplacements.
- Un changement doit prévoir une sauvegarde, une fenêtre d'intervention, des vérifications et un retour arrière.
- Les commandes `display` fournissent des preuves d'état ; `ping` et `tracert` testent la connectivité et le chemin.
- La progression technique va du concept vers la configuration, les mécanismes de protocole et l'analyse détaillée des paquets.
- Une exigence qui ne peut pas être testée est difficile à accepter formellement.
- Le troubleshooting efficace part de faits observables, pas de modifications improvisées.

---

## Commandes Huawei utiles

| Commande | Utilité dans un projet | Preuve obtenue |
| --- | --- | --- |
| `display version` | inventorier le modèle et la version logicielle | contexte matériel et logiciel |
| `display device` | contrôler l'état des composants | disponibilité matérielle |
| `display interface brief` | vérifier rapidement les liens | état physique et protocolaire |
| `display ip interface brief` | vérifier l'adressage des interfaces | adresse et état IP |
| `display current-configuration` | documenter la configuration active | état de référence avant/après |
| `display ip routing-table` | confirmer les chemins connus | présence et origine des routes |
| `ping <adresse>` | tester l'accessibilité IP | succès, perte et délai de réponse |
| `tracert <adresse>` | observer les sauts jusqu'à la destination | localisation approximative d'une rupture |
| `save` | sauvegarder la configuration courante | persistance après redémarrage |

Collecte minimale avant une modification :

```text
display version
display device
display interface brief
display ip interface brief
display current-configuration
display ip routing-table
```

Le résultat doit être enregistré dans le dossier du projet avec la date, le nom de l'équipement et l'objectif de l'intervention.

---

## Pratique obligatoire

### Objectif

Transformer une demande simple en plan d'implémentation et en plan de test.

### Scénario

Une petite agence possède deux services, Administration et Technique. Elle demande une connectivité locale, un accès à une passerelle et une documentation permettant à une autre personne de reprendre l'exploitation.

### Topologie

```text
PC-ADMIN ----\
              S1 ---- R1 ---- Réseau amont
PC-TECH  -----/
```

### Travail demandé

1. Recueillir les besoins : nombre d'utilisateurs, applications, croissance, disponibilité et sécurité.
2. Dessiner la topologie logique et la topologie physique.
3. Proposer un plan d'adressage simple.
4. Établir la liste des configurations à appliquer.
5. Préparer une sauvegarde et une procédure de retour arrière.
6. Écrire au moins six tests d'acceptation.
7. Associer une commande de vérification à chaque test.

### Exemple de matrice d'acceptation

| Test | Commande ou action | Résultat attendu |
| --- | --- | --- |
| Équipement identifié | `display version` | modèle et version conformes à l'inventaire |
| Interfaces actives | `display interface brief` | ports utilisés en état opérationnel |
| Adressage correct | `display ip interface brief` | adresses conformes au plan |
| Passerelle joignable | `ping <passerelle>` | réponses reçues sans perte anormale |
| Route disponible | `display ip routing-table` | réseau destination présent |
| Configuration persistante | `save`, puis contrôle planifié | sauvegarde confirmée |

### Résultat attendu

Le livrable doit permettre à un autre ingénieur de comprendre le besoin, de reproduire le déploiement, de vérifier le résultat et de revenir à l'état précédent en cas d'échec.

---

## Troubleshooting

| Symptôme | Cause probable | Vérification | Correction |
| --- | --- | --- | --- |
| Le projet respecte le schéma mais pas le besoin | exigences incomplètes ou non validées | relire les critères d'acceptation avec le demandeur | reformuler les exigences et corriger la conception |
| Une interface reste down | câble, port, négociation ou configuration | `display interface brief`, puis détail de l'interface | corriger le lien ou la configuration concernée |
| Le ping local fonctionne mais pas le réseau distant | route ou passerelle absente | `display ip routing-table`, `tracert` | corriger l'adressage ou le routage |
| La modification fonctionne puis disparaît après redémarrage | configuration non sauvegardée | comparer configuration courante et configuration de démarrage | exécuter `save` après validation |
| Impossible d'expliquer une panne | état initial non collecté | rechercher les preuves avant/après | établir une baseline et un journal de changement |
| Le retour arrière échoue | procédure non testée ou sauvegarde absente | vérifier le fichier et les étapes de restauration | préparer et tester le rollback avant la fenêtre |

### Méthode TianSemi

1. Reformuler le symptôme et son impact.
2. Identifier ce qui a changé.
3. Collecter l'état sans modifier le réseau.
4. Comparer avec la conception et la baseline.
5. Tester une hypothèse à la fois.
6. Corriger la cause, pas seulement le symptôme.
7. Rejouer les tests d'acceptation.
8. Documenter le résultat et la prévention.

---

## Mini-lab TianSemi

### Titre

Préparer et accepter la mise en service d'un routeur Huawei.

### Matériel

- un routeur Huawei ou un environnement de lab compatible ;
- un PC d'administration ;
- une connexion console ;
- le HCIA-Datacom V2.0 Lab Guide.

### Étapes

1. Se connecter par console.
2. Relever le modèle et la version avec `display version`.
3. Passer en vue système et définir un nom explicite.
4. Configurer une interface de test selon le plan fourni.
5. Vérifier l'état et la configuration.
6. Sauvegarder avec `save`.
7. Compléter la matrice d'acceptation.

```text
<HUAWEI> display version
<HUAWEI> system-view
[HUAWEI] sysname Agence-R1
[Agence-R1] display current-configuration
[Agence-R1] display ip interface brief
[Agence-R1] return
<Agence-R1> save
```

### Critère de réussite

Le lab est réussi si un second apprenant peut vérifier la conformité uniquement avec la documentation et les commandes fournies.

---

## Questions d'entretien

1. Quelle différence faites-vous entre planification, conception et implémentation ?
2. Pourquoi faut-il définir les tests d'acceptation avant le déploiement ?
3. Quelles informations collectez-vous avant de modifier un équipement ?
4. Comment préparez-vous une procédure de retour arrière ?
5. Comment expliquez-vous un incident réseau à une personne non technique ?
6. Quelle différence existe entre une topologie logique et une topologie physique ?
7. Pourquoi une commande connue sans compréhension du protocole peut-elle être dangereuse ?
8. Comment prouvez-vous qu'une optimisation a réellement amélioré le réseau ?

---

## Quiz

### 1. Quelle phase transforme les besoins en architecture ?

- A. Maintenance
- B. Conception
- C. Sauvegarde
D. Escalade

**Réponse : B.**

### 2. Quelle commande fournit une vue rapide de l'état des interfaces ?

- A. `save`
- B. `display interface brief`
- C. `reboot`
D. `undo`

**Réponse : B.**

### 3. Quel élément rend une exigence exploitable ?

- A. Une formulation vague
- B. Un critère mesurable
- C. Une commande choisie au hasard
D. Une absence de seuil

**Réponse : B.**

### 4. Que faut-il faire avant une modification importante ?

- A. Redémarrer immédiatement
- B. Supprimer la configuration
- C. Collecter l'état et préparer le rollback
D. Modifier plusieurs paramètres à la fois

**Réponse : C.**

### 5. Laquelle est une capacité relationnelle ?

- A. Configurer OSPF
- B. Lire une table MAC
- C. Expliquer un risque au client
D. Calculer un sous-réseau

**Réponse : C.**

### 6. Pourquoi exécuter `save` après validation ?

- A. Pour changer le modèle du routeur
- B. Pour rendre la configuration persistante
- C. Pour effacer les routes
D. Pour fermer une interface

**Réponse : B.**

### 7. Quel est le meilleur point de départ d'un troubleshooting ?

- A. Modifier la configuration
- B. Collecter les faits
- C. Restaurer l'usine
D. Remplacer tous les câbles

**Réponse : B.**

### 8. L'analyse des paquets appartient surtout à quel niveau de progression ?

- A. Identification du « quoi » uniquement
- B. Compréhension des mécanismes sous-jacents
- C. Inventaire administratif uniquement
D. Aucun niveau technique

**Réponse : B.**

---

## Flashcards

**Q : Qu'est-ce que l'ingénierie réseau ?**

R : L'ensemble des activités qui permettent de planifier, concevoir, implémenter, tester, exploiter, dépanner et optimiser un réseau.

**Q : Quel est le rôle central d'un ingénieur réseau ?**

R : Transformer un besoin en solution vérifiable et exploitable.

**Q : Que décrit une conception logique ?**

R : Les segments, adresses, protocoles, services et politiques du réseau.

**Q : Que décrit une conception physique ?**

R : Les équipements, ports, liaisons, câbles et emplacements.

**Q : Qu'est-ce qu'un test d'acceptation ?**

R : Une procédure reproductible qui compare un résultat observé à un résultat attendu.

**Q : Pourquoi créer une baseline ?**

R : Pour disposer d'un état de référence avant un changement ou un incident.

**Q : Que doit contenir un plan de changement ?**

R : Le périmètre, les étapes, les risques, les vérifications et le retour arrière.

**Q : Quelle commande sauvegarde la configuration Huawei ?**

R : `save` depuis la vue utilisateur.

**Q : Quelle progression technique est recommandée ?**

R : Quoi, comment, mécanisme de protocole, analyse des paquets, puis vue globale.

**Q : Pourquoi documenter un incident ?**

R : Pour transmettre la connaissance, prévenir la répétition et prouver la résolution.

---

## Références

- HCIA-Datacom V2.0 Training Material, section « Network Engineering and Network Engineers », pages PDF 37-45.
- HCIA-Datacom V2.0 Lab Guide, lab « Basic Operations on Huawei Network Devices », pages PDF 14-25 pour la connexion console, les commandes de base, la sauvegarde et la vérification.
- Huawei Talent Certification page : https://e.huawei.com/en/talent/cert/#/careerCert

---

## Contenus générés

| Canal | Statut | Lien |
| --- | --- | --- |
| Site TianSemi | À générer | |
| Quiz | Intégré à la note | |
