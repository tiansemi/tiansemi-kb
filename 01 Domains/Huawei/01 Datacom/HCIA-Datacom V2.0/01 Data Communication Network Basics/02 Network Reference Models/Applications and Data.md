---
id: HUA-HCIA-DC-005
title: "Applications and Data"
official_title: "Applications and Data"
course_unit: "1.2.1"
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
source_pages: "PDF 46-53"
tags: [huawei, hcia, datacom, applications, data]
prerequisites:
  - "[[01 Data Communication Network Basics/Data Communication Process]]"
related:
  - "[[Network Reference Models and Standard Protocols]]"
  - "[[02 Network Reference Models/Data Communication Process]]"
lab_required: false
publication_status: "not-started"
site_url:
---

# Applications et données (Applications and Data)

## Objectifs du cours Network Reference Models

Le cours Huawei consacré aux modèles de référence doit permettre de :

- comprendre la définition des données et leur processus de transmission ;
- comprendre les modèles de référence et leurs avantages ;
- connaître les principaux protocoles standards ;
- maîtriser l'encapsulation et la décapsulation.

Cette première unité se concentre sur la relation entre applications, information et données.

## Origine : les applications

Les applications existent pour répondre à des besoins humains : navigation web, jeux en ligne, diffusion vidéo et autres services numériques.

Leur utilisation produit de l'information sous différentes formes :

- texte ;
- image ;
- son ;
- vidéo.

L'application donne un contexte et une signification à cette information.

## Mise en œuvre des applications : les données

Dans le domaine informatique, les données sont le support de l'information.

Les ordinateurs reconnaissent des données numériques composées de 0 et de 1. Ils ne peuvent pas interpréter directement toutes les formes d'information humaines. Une conversion est donc nécessaire dans les deux sens :

```text
Information compréhensible par l'humain
        -> traduction selon des règles
Données numériques traitables par l'ordinateur
        -> restitution par une application
Information compréhensible par l'humain
```

Deux opérations sont distinguées :

- **génération des données** : l'information est représentée sous une forme numérique ;
- **transmission des données** : les données produites par une application sont transportées entre des équipements.

Huawei souligne que l'ingénieur réseau doit considérer le processus de transmission de bout en bout.

## Processus de transmission

Le support prend l'exemple d'un client web qui envoie des données à un serveur web.

```text
Navigateur -> pile TCP/IP -> pilote de carte réseau
           -> switchs et routeurs
           -> pilote de carte réseau -> pile TCP/IP -> serveur web
```

Plusieurs modules collaborent :

- le navigateur et le programme serveur produisent ou consomment les données applicatives ;
- la pile TCP/IP prépare et traite les données pour la communication ;
- le pilote de carte réseau assure l'interface avec le matériel ;
- les switchs et routeurs transfèrent les données dans le réseau intermédiaire.

Le cours poursuit ensuite l'étude de ces responsabilités avec les modèles de référence et les protocoles standards.

## Résumé fidèle du cours

- Une application répond à un besoin et génère de l'information.
- Les données numériques sont le support informatique de cette information.
- Les données doivent être converties pour être traitées par l'ordinateur puis restituées à l'utilisateur.
- La plupart des applications transmettent leurs données entre plusieurs équipements.
- Une communication web mobilise des applications, des piles TCP/IP, des cartes réseau, des switchs et des routeurs.

## Révision TianSemi

1. Quelle différence le cours établit-il entre information et données ?
2. Pourquoi une conversion est-elle nécessaire entre l'humain et l'ordinateur ?
3. Quels modules participent à la transmission entre un client web et un serveur web ?

## Références

- Huawei, *HCIA-Datacom V2.0 Training Material*, pages PDF 46-53.
- Huawei Talent, HCIA-Datacom V2.0 : https://e.huawei.com/en/talent/#/cert/product-details?certifiedProductId=1316&authenticationLevel=CTYPE_CARE_HCIA&technicalField=IIC&version=2.0
