# 📄 Fiche Synthèse : Spirent Landslide - Solution de Test et Émulation pour les Réseaux Mobiles 5G

---

## ℹ️ Informations Générales

* **Source :** [20250924_CERT-Tunisia_Landslide-Overview.pdf](20250924_CERT-Tunisia_Landslide-Overview.pdf)
* **Thème de la présentation :** Réseaux mobiles et télécommunications
* **Sujet principal :** Présentation de la solution **Spirent Landslide** pour l'émulation, le test et l'automatisation des réseaux 5G, 4G et Wi-Fi
* **Lieu / Cadre :** Journée de veille 2025 (contexte Tunisien)
* **Présentateur / Hôte :** Non précisé
* 

---

## 🎯 Aperçu et Résumé Global
Cette présentation détaille la solution **Spirent Landslide**, une plateforme avancée conçue pour l'émulation, le test et l'automatisation des réseaux mobiles (5G, 4G, Wi-Fi). Elle couvre des fonctionnalités clés comme l'isolation, l'adjacence et les tests de bout en bout pour des nœuds critiques (AMF, SMF, UPF, etc.). La solution s'adapte aux déploiements sur site ou dans le cloud et propose des bibliothèques de tests préconstruits pour accélérer la validation des réseaux. Des témoignages d'industriels soulignent son rôle clé dans la réduction des coûts et l'amélioration de l'efficacité des tests 5G.

---

## 📌 Sujets Discutés (Résumé Moyen)

### 1. **Fonctionnalités et Couverture de Spirent Landslide**
* **Développement de l'idée :**
  Spirent Landslide permet d'émuler et tester à grande échelle les fonctions réseau (NF), les nœuds et les interfaces pour valider la **fonctionnalité**, l'**interopérabilité**, la **conformité** et les **performances**. La solution couvre des architectures **on-premises** ou **cloud-based**, avec une compatibilité étendue aux réseaux 5G natifs, 4G et Wi-Fi.
  Elle supporte des tests d'**isolation**, d'**adjacence** et de bout en bout pour plus de 15 fonctions nodales (AMF, SMF, UPF, NRF, PCF, AUSF, etc.).
* **Chiffres & Données clés :**
  * 📈 **200+ bibliothèques de tests préconstruits** (conformité, capacité, performance).
  * 📊 **15+ fonctions nodales testées** (ex: AMF, SMF, UPF).
* **Citation / Point marquant :**
  > *"Spirent is a leader in 5G testing and automation and offers us the security & confidence to introduce our state-of-the-art 5G network."*

### 2. **Architecture et Méthodologie de Test**
* **Développement de l'idée :**
  Landslide propose une **architecture modulaire** avec des serveurs physiques (MTP C50, C100) ou virtuels (ESXi, KVM, Azure, AWS, GCP). Les tests peuvent être exécutés via :
  - **GUI** (interface graphique),
  - **TEX** (runtime execution),
  - **TCL** (automatisation),
  - **REST-API** (orchestration).
  La méthodologie inclut l'**émulation des éléments réseau** (ex: AMF) et des **tests de charge** (jusqu'à des millions de connexions 5G).
* **Chiffres & Données clés :**
  * 📈 **Jusqu'à 32 serveurs de test (TS) par TAS** pour une échelle massive.
  * 📊 **Modélisation du trafic utilisateur réel** (voix, vidéo, applications).

### 3. **Cas d'Usage et Valeur Ajoutée**
* **Développement de l'idée :**
  Les principaux cas d'usage incluent :
  - Tests du **plan utilisateur**,
  - Validation des architectures **NSA/SA O-RAN**,
  - Tests d'**architecture basée sur les services (SBA)**,
  - Automatisation des tests du **cœur 5G**.
  La solution permet de **réduire les coûts** (60-95% d'économies) et d'**accélérer la mise sur le marché** des nouveaux services 5G.
* **Citation / Point marquant :**
  > *"Nokia’s 5G Core Validation team is using Spirent due to its industry-leading capabilities & wide variety of automation possibilities."*

### 4. **Support des Plateformes et Évolutivité**
* **Développement de l'idée :**
  Landslide est compatible avec des environnements **virtuels** (Docker, Kubernetes) et **matériels** (OTA Testing). Il supporte les déploiements **multi-vendeurs** et les architectures **CaaS** (Cloud-as-a-Service) pour une évolutivité optimale.

---

## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **Solution tout-en-un** : Émulation, test et automatisation des réseaux 5G/4G/Wi-Fi avec une couverture étendue (15+ fonctions nodales).
* 🔹 **Réduction des coûts et du temps** : 60-95% d'économies grâce à des tests en laboratoire vs. déploiement réel.
* 🔹 **Flexibilité** : Déploiement sur site ou cloud, avec support des architectures modernes (Kubernetes, OpenShift).
* 🔹 **Validation industrielle** : Utilisé par des leaders comme Nokia, Ericsson et des opérateurs télécoms pour la validation des réseaux 5G.

---

## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

Spirent Promise Assured Proprietary and Confidential

Mobile Core Networks

1

Spirent  Promise Assured 2 Proprietary and Confidential

Landslide Overview

SPIRENT LANDSLIDE

Isolation

AMF

AMF SMF

AMF

SMF

UPF

Adjacency

End-to-End

Live  5G Core

Emulation & Testing Automation Coverage

Lab Pre-Production

Landslide

Spirent  Promise Assured 3 Proprietary and Confidential

Emulation and Testing

SPIRENT LANDSLIDE

Emulate and test at scale with the most comprehensive coverage of Network Functions, Nodes, Interfaces

Functionality

Interoperability

Compliance

Isolation

AMF

Adjacency

AMF SMF

Capacity

Performance

End-to-End

AMF

SMF

UPF

Applications (400+)

Spirent  Promise Assured 4 Proprietary and Confidential

Coverage for On-Premises or Cloud-Based Deployments

SPIRENT LANDSLIDE

Proprietary and Confidential 6 Spirent Promise Assured 6

MRFP

IMS-MGW

MRFC

HSS SLF

IBCF

IMS

BGCF

P-CSCF

MGCF

I-CSCF

S-CSCF

UPF UPF

S-GW-C

ePDG

Offload GW

S11

S5-C

HSS

AAA

EIR

CBC

Evolved Packet Core Registers

S10

S13

SBc

S6a

S6b

SWx

S2a

S2b

SS7

PCRF

PCRF

LTE

S9

IP Network /

Internet

Operator IP

Services

SGi

Application

Servers

TDM PSTN

Rx

Gx

Gm

X2

Uu

S1-MME

S1-U

Radio Access Network Core Network Services/Application Network

S-GW-U S-GW-U S-GW-U S-GW-U S-GW-U P-GW-U

Sxa Sxb S5-U SGi

P-GW-C

CUPS

5G (Native)

gNodeB

Xn

Uu

X2-U

AUSF UDM AF

5G Core

N7

N5

N4

N15

N10

N11

N8 N12

N13

N2

N1

N9

N14

AMF

UPF

NEF

NRF

MEC

N3

Network Slices

SDSF

UDSF

N19

N18

Common Functions

N24

PCF

NSSF N17

N6

N16

SMF

Dual  Connect

Uu X2-C

S6t

T6a

Rx

IoT

CSGN T6a

S1-MME

MEC

5G NSA

Xn

Uu

gNodeB

eNodeB

IoT  Application

Server

SCEF S1-U

Wi-Fi AP 802.11 Trusted

Untrusted

MME

MME

EIR

N22

Landslide 5G, LTE, and Wifi

Test & Emulate Emulate Only Test Only

Test Coverage Legend:

Spirent  Promise Assured 7 Proprietary and Confidential

Change & Complexity

The multi-vendor, massively virtualized 5G world requires an evolution in testing methodologies

SPIRENT LANDSLIDE

0.2 0.3 0.4 … 1.0 0.1

5G Network - 12 Month View

1.1 1.2 1.3

4.6 4.7 4.8 4.9 OpenShift

4.10 5.0 5.1

CaaS

1.16 1.17 1.18 1.19 1.20 1.21 1.22

Service Mesh

5G Core

4G Network - 12 Month View

Single  Vendor

SW R2 SW R3 SW R1

Spirent  Promise Assured 8 Proprietary and Confidential

✓Faster time to market for new

technologies

✓Develop superior functionality

Automation

Bring 5G offerings to market with speed and confidence

Test Libraries: 200+ pre-built compliance, capacity, and performance tests

Test Coverage: Isolation, adjacency, and end-to-end testing of over 15 nodal functions including  AMF, SMF, UPF, NRF, PCF, and AUSF

SPIRENT LANDSLIDE

Proprietary and Confidential 9 Spirent Promise Assured 9

Landslide Hardware and Architecture

Landslide Test Server Deployment

Proprietary and Confidential 10 Spirent Promise Assured 10

Different ways to access and control Landslide

Landslide GUI TEX (runtime execution)

TCL (automation) REST-API (automation and orchestration)

Spirent  Promise Assured 11 Proprietary and Confidential

Landslide testing Methodology

Landslide Tests and Emulate Network Elements in a Mobile Network

SPIRENT LANDSLIDE

AMF Nodal Test Type AMF Node Test Type

Testing the AMF by emulating the surrounding Network Elments Testing the Network Elemnts surrounding the AMF by emulating the AMF

Proprietary and Confidential Spirent Promise Assured

Platforms Support

SPIRENT LANDSLIDE

12

MTP C50 C100

Virtual

Medium Scale Up to 2 TS per TAS

ESXi, KVM, Azure,

AWS, and GCP

Software Agents

Hardware Appliances

Container

Docker, Kubernetes SRiOV & CNI support Use Cases: Orchestrated Testing, Portability, Resiliency, vNF Sandbox, ..

Massive Scale Up to 32 TS per TAS OTA Testing

Millions of Any-G Connections with Full Mobility

Real World User Traffic (Voice, Video, Internet, Apps…)

Carrier and Smartphone Call Modeling

Node and Network Emulation

Line Rate Traffic Generation

Spirent  Promise Assured 20 Proprietary and Confidential

Primary Use Cases

✓User Plane testing

✓NSA and SA ORAN testing

✓Service Based Architecture testing

✓End-to-end performance and capacity testing

✓5G Core test automation

SPIRENT LANDSLIDE

Spirent  Promise Assured 21 Proprietary and Confidential

Driving Tangible Value

SPIRENT LANDSLIDE

Reduce costs with pre-

built test libraries and

automation

Avoid costs by finding  issue in the lab vs. the

live network

Decrease time to

revenue for new  products & services

60% 80% 95%

Proprietary and Confidential

Trusted by the industry

23

“Spirent is a leader in 5G testing  and automation and offers us the  security & confidence to introduce

our state-of-the-art 5G network.”

“Integration of Spirent has led to a  3x improvement in the time it takes  to test and validate [our] 5G private

network stack.”

“Nokia’s 5G Core Validation team is

using Spirent due to its industry- leading capabilities & wide variety of

automation possibilities.”

“Spirent has played an integral role

in our network test planning,

validation and deployment.”

“Emulation is a critical element of  any O-RAN testbed and Spirent is

the market leader in this area.”

“Spirent is a golden reference  globally for validating 5G core

networks for functionality and

performance.”

“Spirent is a leader in C-V2X  protocols conformance testing...we

successfully validated the test

solution by using the latest

C-V2X devices.”

“Combining Spirent’s best-in-class  methodology with NI’s versatile and

powerful product lineup is a critical  step in standardizing and accelerating

O-RAN O-RU development.”

Spirent Promise Assured Proprietary and Confidential 24

Spirent 5G Report

Slide 25

Spirent Promise Assured 25

5G Engagements by  Numbers

Spirent® Communications, Inc. and its related company names, branding, product names and logos referenced herein,

and more specifically “Spirent” are either registered trademarks or pending registration within relevant national laws.

</details>