---
id: HUA-HCIA-DC-007
title: "Data Communication Process"
aliases:
  - "Data Encapsulation and Decapsulation"
official_title: "Data Communication Process"
course_unit: "1.2.3"
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
updated: 2026-07-13
source: "HCIA-Datacom V2.0 Training Material"
source_pages: "PDF 80-86"
tags: [huawei, hcia, datacom, encapsulation, decapsulation]
prerequisites:
  - "[[Network Reference Models and Standard Protocols]]"
related:
  - "[[01 Data Communication Network Basics/Data Communication Process]]"
lab_required: false
publication_status: "not-started"
site_url:
---

# Processus de communication de données (Data Communication Process)

## Position dans le cours

Huawei nomme cette troisième partie « Data Communication Process ». Elle détaille le processus introduit dans l'unité 1.1 en le décrivant avec le modèle TCP/IP équivalent : encapsulation chez l'émetteur, traitement dans le réseau intermédiaire et décapsulation chez le récepteur.

## Encapsulation chez l'émetteur

Le support prend l'exemple d'un utilisateur qui saisit l'adresse du site Huawei dans son navigateur.

### Couche application

Le navigateur appelle HTTP pour préparer les données applicatives. Le schéma simplifie le contenu et ne montre pas explicitement l'en-tête HTTP.

La PDU est appelée **data**.

### Couche transport

HTTP utilise TCP dans l'exemple. Le module TCP ajoute un en-tête contenant notamment les ports source et destination.

La PDU devient un **segment**.

### Couche réseau

Sur un réseau IPv4, le segment est remis au module IPv4 ; sur un réseau IPv6, il est remis au module IPv6. Le module ajoute l'en-tête IP.

La PDU devient un **packet**.

### Couche liaison de données

Ethernet reçoit le paquet IP, ajoute un en-tête Ethernet et un trailer Frame Check Sequence.

La PDU devient une **frame**.

### Couche physique

Selon le média, la couche physique convertit les données numériques en :

- signaux électriques ;
- signaux optiques ;
- ondes électromagnétiques.

La PDU transmise est un **bitstream**.

```text
Application : Data
    -> Transport : TCP header + Data = Segment
        -> Réseau : IP header + Segment = Packet
            -> Liaison : Ethernet header + Packet + FCS = Frame
                -> Physique : Bitstream et signal
```

## Transmission dans le réseau intermédiaire

Les données complètement encapsulées traversent les équipements intermédiaires.

Huawei simplifie leur traitement de la manière suivante :

- un équipement de couche 2, comme un switch, retire ou lit les informations de couche 2 nécessaires et effectue une opération de commutation ;
- un équipement de couche 3, comme un routeur, traite les informations de couche 3 nécessaires et effectue une opération de routage.

Les détails de la commutation et du routage sont renvoyés aux cours « Ethernet Switching Basics » et « IP Routing Basics ».

## Décapsulation chez le récepteur

Lorsque les données atteignent le serveur destination, les couches effectuent le processus inverse :

1. la couche physique reçoit le signal et restitue le bitstream ;
2. la couche liaison traite la trame et retire ses informations ;
3. la couche réseau traite le paquet IP ;
4. la couche transport traite le segment TCP ;
5. la couche application reçoit les données destinées au programme serveur.

Les informations des différents headers permettent de traiter et de remettre les données au bon module, couche après couche.

## Quiz officiel

1. Quels sont les avantages d'un modèle en couches ?
2. Quels protocoles courants appartiennent aux couches application, transport, réseau et liaison de données ?

### Éléments de réponse du support

- application : HTTP, DNS, FTP et Telnet ;
- transport : UDP et TCP ;
- réseau : IP et ICMP ;
- liaison : Ethernet et PPP.

## Résumé fidèle du cours

- Les modèles OSI et TCP/IP adoptent une conception en couches.
- La séparation des fonctions facilite le développement, la conception et le troubleshooting.
- La définition des fonctions de chaque couche favorise la normalisation.
- Les interfaces entre couches améliorent la compatibilité entre matériels, logiciels et réseaux.
- La génération et la transmission des données nécessitent la collaboration de plusieurs modules, chacun responsable de sa propre fonction.

## Références

- Huawei, *HCIA-Datacom V2.0 Training Material*, pages PDF 80-86.
- Huawei Talent, HCIA-Datacom V2.0 : https://e.huawei.com/en/talent/#/cert/product-details?certifiedProductId=1316&authenticationLevel=CTYPE_CARE_HCIA&technicalField=IIC&version=2.0
