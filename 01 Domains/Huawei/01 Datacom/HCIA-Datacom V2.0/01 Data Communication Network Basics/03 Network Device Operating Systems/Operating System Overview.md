---
id: HUA-HCIA-DC-008
title: "Operating System Overview"
official_title: "Operating System Overview"
course_unit: "1.3.1"
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
source_pages: "PDF 87-95"
tags: [huawei, hcia, datacom, yunshan-os, vrp]
prerequisites:
  - "[[01 Data Communication Network Basics/Data Communication Network Devices]]"
related:
  - "[[Logging In to Network Devices]]"
  - "[[Configuring Network Devices]]"
lab_required: false
publication_status: "not-started"
site_url:
---

# Vue d'ensemble des systèmes d'exploitation (Operating System Overview)

## Objectifs du cours Network Device Operating Systems

À la fin du cours, l'apprenant doit être capable de :

- comprendre les concepts fondamentaux des systèmes d'exploitation ;
- maîtriser les modes de connexion aux équipements réseau ;
- effectuer des opérations CLI de base ;
- gérer les systèmes de fichiers et les fichiers de configuration.

Cette première unité se concentre sur la définition et les fonctions des systèmes d'exploitation.

## Qu'est-ce qu'un système d'exploitation ?

Un système d'exploitation est un logiciel système qui gère et contrôle les ressources matérielles et logicielles. Huawei le compare au cerveau humain, qui coordonne plusieurs fonctions :

- traitement de plusieurs tâches ;
- allocation des ressources ;
- contrôle du matériel ;
- fourniture d'une interface avec l'utilisateur.

## Système d'exploitation d'un ordinateur

Le système d'exploitation d'un ordinateur sert de pont entre l'utilisateur et la machine. Il coordonne :

- les ressources matérielles : processeur, mémoire, stockage, périphériques d'entrée-sortie et carte réseau ;
- les ressources logicielles : pilotes, logiciels système et applications.

L'utilisateur accède aux applications et aux ressources par une interface, notamment une interface graphique.

Huawei propose deux classifications générales :

| Critère | Catégories citées |
| --- | --- |
| Domaine d'application | desktop, serveur, embarqué, distribué |
| Ouverture du code source | open source, comme Linux et Unix ; closed source, comme Windows et macOS |

## Système d'exploitation d'un équipement réseau

Le système d'exploitation réseau est le « cerveau de gestion » installé sur les routeurs, switchs et firewalls. Il contrôle le matériel, traite le transfert des données et permet la communication entre équipements.

Ses fonctions comprennent :

- gestion des ressources matérielles ;
- transfert et routage des données ;
- prise en charge des protocoles réseau ;
- sécurité et contrôle d'accès ;
- configuration et supervision de l'équipement.

## Huawei YunShan OS et VRP

Huawei utilise notamment deux familles de systèmes pour ses produits Datacom :

- **YunShan OS** ;
- **Versatile Routing Platform (VRP)**.

Selon le cours, ces systèmes :

- fournissent une interface utilisateur et une interface de gestion cohérentes ;
- mettent en œuvre les fonctions du plan de contrôle ;
- définissent les interfaces du plan de transfert ;
- permettent la communication entre les plans de contrôle et de transfert ;
- proposent une CLI et une interface web pour la connexion, la configuration et l'administration.

Le support utilise principalement un switch CloudEngine S5755-H exécutant YunShan OS pour présenter les modes de connexion et les commandes de base.

La commande suivante permet d'identifier le système et sa version :

```text
<HUAWEI> display version
```

La sortie varie selon la plateforme et peut indiquer YunShan OS ou VRP, ainsi que la version logicielle correspondante.

## Résumé fidèle du cours

- Un système d'exploitation coordonne les ressources matérielles et logicielles.
- Un système d'exploitation réseau gère le matériel, le transfert, les protocoles, la sécurité et la configuration.
- YunShan OS et VRP sont utilisés sur les équipements Huawei Datacom.
- Ils fournissent des interfaces CLI et web pour administrer les équipements.

## Révision TianSemi

1. Quelles ressources un système d'exploitation coordonne-t-il ?
2. Quelles fonctions supplémentaires sont essentielles sur un équipement réseau ?
3. Que sont YunShan OS et VRP ?
4. Pourquoi faut-il relever la version avant d'appliquer une procédure ?

## Références

- Huawei, *HCIA-Datacom V2.0 Training Material*, pages PDF 87-95.
- Huawei Talent, HCIA-Datacom V2.0 : https://e.huawei.com/en/talent/#/cert/product-details?certifiedProductId=1316&authenticationLevel=CTYPE_CARE_HCIA&technicalField=IIC&version=2.0
