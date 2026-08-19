# 📄 Fiche Synthèse : Mobile Network Benchmarking for 5G

---

## ℹ️ Informations Générales

* **Source :** [Mobile Network Benchmarking for 5G (1).pdf](Mobile Network Benchmarking for 5G (1).pdf)
* **Thème de la présentation :** Télécommunications et Réseaux Mobiles
* **Sujet principal :** Benchmarking des réseaux mobiles 5G pour optimiser l'expérience utilisateur et différencier les services
* **Lieu / Cadre :** Non précisé (document technique)
* **Présentateur / Hôte /invités / Intervenants  :**Dharen Ells** — Spirent (contact technique)


---

## 🎯 Aperçu et Résumé Global
Ce document technique de **Spirent** présente une méthodologie avancée pour évaluer l'expérience utilisateur (QoE) sur les réseaux mobiles 5G. L'objectif est de fournir aux opérateurs et fabricants d'équipements des outils pour mesurer, optimiser et différencier leurs services en se basant sur des critères quantitatifs (latence, débit, qualité vidéo/voix, etc.). Spirent propose une approche scientifique et automatisée, couvrant des scénarios variés (drive tests, tests en intérieur, tests stationnaires) et des technologies comme le **mmWave**, le **DSS** (Dynamic Spectrum Sharing) et le **SA/NSA**. Des études de cas illustrent l'impact concret de ces benchmarks sur la prise de décision et le marketing des opérateurs.

---

## 📌 Sujets Discusés (Résumé Moyen)

### 1. **Portfolio d'Expérience Mobile de Spirent**
* **Développement de l'idée :**
  Spirent propose une gamme de solutions (Umetrix) pour évaluer la qualité d'expérience (QoE) sur les **appareils mobiles**, les **réseaux**, les **services de communication** et le **contenu**. Leur approche couvre :
  - **Validation des appareils** avant leur lancement (tests QoE sur voix, vidéo, données, localisation).
  - **Benchmarking des réseaux** pour optimiser les services et se différencier (tests nationaux/régionaux, évaluation de la concurrence).
  - **Validation des mises à niveau réseau** (5G SA/NSA, DSS, MEC, IoT massif).
  - **Tests spécifiques** : gaming cloud, réseaux sociaux, VoWiFi, etc.

* **Chiffres & Données clés :**
  * 📈 **98,33%** de temps passé sur le réseau 5G (vs 1,67% en LTE) pour un appareil Samsung SM-N976U lors d'un test Spirent.
  * 📊 **120 marchés** testés aux États-Unis (2 fois par an) pour un opérateur nord-américain.

### 2. **Méthodologie de Benchmarking 5G**
* **Développement de l'idée :**
  Spirent utilise des **tests en conditions réelles** (drive, walk, stationnaire) et en laboratoire, avec des appareils commerciaux ou des prototypes. Leur technologie **Umetrix** permet de :
  - Mesurer des KPIs critiques : débit, latence, qualité vidéo (MOS), taux de décrochage, etc.
  - Corréler les données RF (niveau signal, interférences) avec les performances applicatives.
  - Automatiser les tests pour une reproductibilité et une analyse statistique robuste.
  - Adapter les scénarios aux **classes de trafic 5G** : eMBB (large bande), URLLC (latence ultra-faible), mMTC (IoT massif).

* **Chiffres & Données clés :**
  * 📊 **10 Gbps** : débit maximal testé via des serveurs cloud Spirent.
  * 📈 **5G mmWave** : tests ciblant des bandes haute fréquence (24 GHz+) pour évaluer la couverture et la QoE dans des environnements urbains denses.

### 3. **Tests Spécifiques par Cas d'Usage**
* **Développement de l'idée :**
  Spirent détaille des méthodologies pour évaluer des services spécifiques :
  - **Données mobiles** : tests de débit (HTTP, FTP, UDP), latence, et fiabilité (cycles de succès/échecs).
  - **Vidéo en streaming** : analyse de la qualité (MOS), temps de démarrage, buffering, et détection d'artefacts (compression, CGI).
  - **Voix** : évaluation de la qualité vocale (POLQA MOS), handover, et performances VoLTE/VoNR.
  - **Gaming cloud** : métriques de latence, perte de paquets, et score d'expérience agrégé (ITU-T G.1072).
  - **Réseaux sociaux** : mesure de la QoE pour le partage d'images, le chat, et le streaming vidéo.

* **Citation / Point marquant :**
  > *"The Service Provider with the best user experience wins!"* — Mise en avant de l'importance stratégique de la QoE pour la rétention des abonnés et l'ARPU (Average Revenue Per User).

### 4. **Outils et Livrables**
* **Développement de l'idée :**
  Spirent fournit des **rapports détaillés** (sous 1 semaine) incluant :
  - Analyses statistiques (moyennes, percentiles, intervalles de confiance).
  - Cartes de couverture et de QoE par opérateur.
  - Fichiers de logs RF (Umetrix LM) pour un post-traitement personnalisé.
  - **Exemples de livrables** :
    - Rapports par marché (ex: comparaison Samsung vs Apple).
    - Cartes thermiques des zones problématiques (ex: parkings, stades).
    - Benchmarks de venues critiques (ex: centres commerciaux, aéroports).

* **Chiffres & Données clés :**
  * 📈 **95e percentile** : échantillonnage statistique pour garantir la fiabilité des résultats.

### 5. **Études de Cas Concrètes**
* **Développement de l'idée :**
  Deux cas illustrent l'application pratique des solutions Spirent :
  1. **Opérateur nord-américain** :
     - **Défi** : Besoin de rapports semestriels pour prioriser les optimisations réseau et valider des claims marketing 5G.
     - **Solution** : Déploiement de l'Umetrix suite (données, voix, vidéo) sur 120 marchés.
     - **Impact** : Données utilisées pour optimiser les investissements et justifier des campagnes marketing.
  2. **Opérateur avant le lancement 5G** :
     - **Défi** : Vérifier la performance 5G avant le lancement pour revendiquer la meilleure offre.
     - **Solution** : Tests comparatifs (3 villes, 3 opérateurs, 10 lieux) avec Umetrix Data.
     - **Impact** : Identification des faiblesses backend → améliorations → validation des claims post-lancement.

---

## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **L'expérience utilisateur (QoE) est le critère clé** pour différencier les opérateurs 5G et fidéliser les abonnés. Spirent propose une méthodologie scientifique pour la mesurer objectivement.
* 🔹 **Les benchmarks 5G vont au-delà des tests 4G** : intégration du mmWave, du DSS, et des classes de trafic (eMBB, URLLC, mMTC).
* 🔹 **Automatisation et analyse avancée** : outils comme Umetrix LM permettent de corréler les données RF avec les performances applicatives, et de générer des rapports actionnables en temps réel.
* 🔹 **Cas d'usage variés** : Spirent couvre tous les services (voix, vidéo, gaming, réseaux sociaux) avec des KPIs adaptés (MOS, latence, débit, fiabilité).
* 🔹 **Impact business prouvé** : les opérateurs utilisent ces données pour optimiser leurs réseaux, justifier des investissements, et renforcer leur positionnement marketing.

---

## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

```
Proprietary and Confidential Spirent Promise Assured

Mobile Network  Benchmarking for 5G

Measuring User Experience to Drive  Service Optimization and Differentiation

1 Proprietary and Confidential Spirent Promise Assured

Dharen.Ells@spirent.com

Measure success against the standard that matters to your end users -

a positive experience

Spirent’s Mobile Experience Portfolio assures the promise of a quality user experience

across mobile devices, networks, communication services and content.

Proprietary and Confidential 3 Spirent Promise Assured

Mobile Experience Portfolio Overview

Mobile Device

Launch

Mobile Network

Benchmarking Mobile Service

Validation

Ensure quality of user experience on

mobile devices before launch

• Decades-long program with leading  operators (e.g., T-Mobile, AT&T)

• Assure voice, video, data, and location  services QoE

• Generally paid for by device supplier

Measure user experience to drive  service optimization & differentiation

• Nationwide or regional coverage;  ongoing or project-based

• Industry-leading expertise to define 5G  service test criteria and methodology

• Assess competition; validate claims;  drive improvements

Ensure quality of user experience  throughout network or service upgrade

• Validate and optimize your 5G network  as it grows and evolves (NSA/SA, DSS,  etc.)

• Ensure QoE during new service launch  (MEC, Augmented Reality, Machine- Machine, etc.)

Proprietary and Confidential 4 Spirent Promise Assured

Measure What Matters

Voice Calling

• Quality (MOS) • Completions • Drops • Acoustic & Noise  Cancellation

Streaming  Video

• Quality (MOS) • Start time • Buffering • Freezing

Video Calling

• Frame Delivery  • A/V Sync

Mobile  Gaming

• Telemetry Lag/Latency • Video frame quality • Freezing • Gaming Score

Apps and  Web

• Page load time • Emulated App Data • Reliability

General  Data

• Speed  • Bandwidth • Latency • Reliability

Location

• Lat-Lon Accuracy • Z-axis • Time to first fix • Yield

Coverage  and Quality

• Signal Strength • Quality • Interference • Resourcing • Band usage

Proprietary and Confidential 5 Spirent Promise Assured

Spirent’s Mobile Experience Approach

• Quantify the user experience in a repeatable, scientific  way – “Measure what matters”
• Measurements taken primarily on live networks through  drive, walk, and stationary testing
• Augment with lab testing where appropriate
• Uses proven Quality of Experience (“QoE”) testing  methodologies to tackle different use cases
• Tailor solution to each customer’s requirements
• Enabled by Spirent’s industry-leading Umetrix  technology

• Use COTS devices or engineering prototypes

Proprietary and Confidential 6 Spirent Promise Assured

Challenges in Getting Real Answers

The Service  Provider  with the  best user  experience  wins!

• Gains  Subscribers • Commands  higher ARPU

Challenge 1:   Define Benchmarking Criteria

Challenge 2:  Execute Benchmarking

Critical Insights

required to

Prioritize  Optimization

Efforts

Validated  Marketing

Claims

Objective Outputs

Conditions

Location  Criteria

User  Experience  Criteria

Competitors

Detailed Test  Planning

Automation  and  Logistics

Analysis

Test  Technology  Selection

Proprietary and Confidential 7 Spirent Promise Assured

5G Benchmarking Will Go Well Beyond 4G

and  below

Target Customers Traffic Classes Applications

Consumer &  Business  smartphone

Consumer &  Business  smartphone

Enterprise

Fixed  Wireless  Access

Same for all traffic Voice, Video, Data

Limited IoT

Enhanced Mobile  Broadband (eMBB)

Ultra-Reliable Low- Latency Communications  (URLLC)

Massive Machine-Type  Communications (mMTC)

Coverage

• Low Band • Medium Band

• Low Band • Medium Band • High Band (mmWave)

• Dynamic Spectrum  Sharing • Handoffs

Voice, Video, Data

Massive IoT (10  times devices per  square km)

Augmented Reality

Coverage

Bandwidth

Coverage

Bandwidth

Cloud Gaming

Proprietary and Confidential 8 Spirent Promise Assured

Spirent’s Approach

Decades of QoE measurement experience to give you quantified, repeatable assessments

• Spirent uses our Umetrix QoE Solutions for  Data, Voice, Video, Cloud Gaming testing  and RF Logging
• Centrally controlled test definitions
• E2E: apps/clients to Cloud- and Edge-based servers
• Approach
• Use same device model on all target operators
• Ensure equal treatment in vehicles and at stationary  locations
• Routes and locations chosen for unbiased  comparison
• Simultaneous RF logging & QoE testing

Walk  Tests

Drive  Tests

Stationary

Tests

Proprietary and Confidential 9 Spirent Promise Assured

Mobility and Stationary Scenarios

5G-DSS/Sub-6/4G-LTE and mmWave

• Markets broken out into large, medium, small
• Each with target location, mileage & sample  count for 95th percentile confidence interval
• DSS/Sub-6/4G and mmWave 5G – mix of  morphologies, low/mid/high band 5G
• Select Android Devices (iOS available)
• Video, Data, Web, Voice assessment
• Focus on QoE and coverage per access  network

Deliverables
• Market report delivered within one week of  collection, including statistical analysis
• Quarterly aggregated nationwide report
• DM Logfiles
• Insights and Trends Analysis

Provider 1 Provider 2 Provider 3

Samsung SM-N976U

(5G REF)

Samsung SM-A716U

(5G DUT) 5G 98.33% 97.41%

LTE 1.67% 2.59%

0%

25%

50%

75%

100%

% of Time on Serving Network -

Overall mmWave

• Multiple locations per operator per market
• Focus on Data QoE

Proprietary and Confidential 10 Spirent Promise Assured

Venue / Walk Testing

Stay ahead of your competition at critical venues

• Provider versus competitors throughout  the venue and in parking structure
• Periodic benchmarking of major venues
• Test kits adapted for indoor testing
• User experience KPI’s reported on actual  venue maps/plans

Deliverables
• Venue report delivered within one week of  collection, including statistical analysis
• DM Logfiles

Proprietary and Confidential 11 Spirent Promise Assured

Data Experience Testing

Used by major mobile operators, chipset suppliers and device manufacturers

• Emulate actual end user with Umetrix Data
• Cover full 5G spectrum including mmWave
• Test to Spirent-managed 10 Gbs cloud locations and  Spirent edge servers
• Focus on connection rate, latency, throughput and  reliability in mobility and stationary scenarios
​• Able to run “typical user” tests plus “fill the pipe”  tests
• Test multiple protocols UDP, HTTP, HTTPS, FTP  (expect routing differences)
• Record underlying RR assignment (MIMO, CA, etc.)  for info on competitive differences​ (put as last bullet)

Proprietary and Confidential 12 Spirent Promise Assured

Video Experience Testing

Industry-leading Over-the-Top (OTT) Technology

• Multi-pronged methodology for  complementary views of QoE
• OTT (Netflix, Hulu, Prime or others)
• Spirent-controlled stress test
• Buffering, Freezing, Over-compression​  (MOS), Time-to-first frame, frame  statistics
• OTT algorithms provide unique  competitive insight into streaming apps
• Smart capture and processing – filter out  CGI, graphical tickers, black bars that  can impact scoring​, region of interest

Any streaming or

chat services

Streaming video

Optional benchmark

device

Display device Smart device, media player, set-top box, etc.

USB

Umetrix Video UI and algorithms (laptop or server configurations)

Umetrix Video

universal hub

HDMI, MHL or

DisplayLink

LTE/3G Wi-Fi 5G

Live or simulated network with IP and/or RF impairments

and diagnostics

Proprietary and Confidential 13 Spirent Promise Assured

Voice Experience Testing

Decades of voice testing from 2G thru 5G

• Evaluate the user experience of voice  services in the live network using actual  consumer mobile devices
• Speech Quality
• Call Performance
• Handover before/after
• Uses POLQA for latest speech quality MOS
• VoWiFi, VoLTE, VoNR, EPSFB
• Mobile-to-mobile and mobile-to-server  calling

Umetrix

Cloud

Proprietary and Confidential 14 Spirent Promise Assured

Cloud Gaming Experience Testing

Investing in new and growing services and applications

• Spirent uses an emulated approach to  measure the cloud gaming experience
• Key KPI components
• Uplink and downlink telemetry latency and loss
• Video frame: freezing, MOS, loss
• These components are aggregated  into a single gaming experience score derived from ITU-T G.1072

Proprietary and Confidential 15 Spirent Promise Assured

Social Media Experience Testing

Aggregated methods for Quality of Experience

• Spirent measures individual data, video and  voice actions offered in social media apps
• Key activities and KPI components
• Image sharing
• File sharing
• Video clip upload and streaming
• App download
• Chat
• Web/HTTP gets & puts
• Quality. Transfer Time. Latency. Reliability.
• These components are aggregated  into a single social media experience score

Proprietary and Confidential 16 Spirent Promise Assure

VoWiFi Experience Testing

Drawn from decades of lab speech testing

• Spirent uses a lab-based approach to measure the VoWiFi  experience
• Compare user experience over a range of WiFi/Cellular call  conditions using Spirent Octoscope and Umetrix
• Selected business-class access points
• Tests
• Audio Quality with packet loss and jitter impairments
• Handover between cellular and WiFi
• KPIs: POLQA MOS (before/after), handover success rate,  speech latency, dropped calls, blocked calls
• Fully automated for repeatability

Proprietary and Confidential 17 Spirent Promise Assured

KPIs

• 5G – 5G connection rate / availability – 5G reliability
• HTTP Download/Upload – Upload / Download mean throughput rates – Reliability: cycles (aborted, failed, passed)
• Bandwidth Download/Upload – Upload / Download mean throughput rates – Reliability: cycles (aborted, failed, passed) – Bandwidth score
• FTP Download/Upload – Upload / Download mean & instantaneous t’put rates – Reliability: cycles (aborted, failed, passed)
• UDP Download/Upload – Reliability: cycles (aborted, failed, passed) – One-way latency – Jitter – Instantaneous, mean & % of ideal throughput
• Web Browsing – Reliability: cycles (aborted, failed, passed) – Page load time
• Ping – Reliability: cycles (aborted, failed, passed) – Latency: Round trip time – Packet loss %
• Diagnostics Logging – Dedicated logging task to gather RF based KPIs from the UE
• Mobile Originated Call with Multi-RAB – Voice call performed with a simultaneous throughput test to stress the UE
• Video KPIs – Video MOS – Freezing and buffering rate – Packet Loss Impairments – SI, TI A/V Sync
• Voice KPIs – MOS – Reliability: call completion rate, dropped call rate – Mean setup time
• Gaming KPIs – Aggregate QoE – Uplink and downlink telemetry latency – Video frame – latency, loss, freezing, MOS

Proprietary and Confidential 18 Spirent Promise Assured

We’re Here to Help | A trusted partner

Expertise and Experience for the mobile industry

Experience and Best Practices Spirent is a valued partner to global operators, OEMs, and chipset vendors who rely on us to  deliver methodologies, solutions and services to test new technologies

• Decades long device quality services for large national operators
• National-scale benchmarking programs for large national operators
• Solid relationships with all major mobile device and chipset suppliers

Investment and Innovation Spirent invests in technology and solutions to assess what matters today and tomorrow

• Evolution to 5G and mmWave testing
• Market-leading OTT video and gaming solutions
• Focus on helping customers improve the mobile quality of experience

Continuous Improvement Spirent invests in new approaches to QoE test solutions

• Remote execution, automation and monitoring; this improves device and service time to market  and reduces costs while also increasing effectiveness
• Centralized control over complete test process – proactive monitoring of devices in the field

PROPRIETARY AND CONFIDENTIAL 19

The User Experience Promise. Assured.

Any Device

Any Network

Anywhere

Proprietary and Confidential 20 Spirent Promise Assured

CHALLENGE

• A major North American service provider wanted nationwide  reports twice a year to help prioritize optimization efforts and  feed marketing claims for 5G and video.

SOLUTION

• Spirent’s Managed Solutions team deployed the entire Umetrix  suite to measure 5G data, voice and OTT video quality of  experience.The customer is also using Spirent’s Customer  Experience Management (CEM) system inside their network,  and this data is correlated with the drive tests to provide insight  on how to optimize spending to improve the user experience.  Spirent is driving 120 markets in the USA twice a year.

IMPACT

• Program received glowing reviews from the customer who now uses  this data to prioritize optimization. The customer is also expected to  make marketing claims based on the data produced.

20

Benchmarking 5G Network  Performance

Spirent Your Promise Assured

CASE STUDY

Proprietary and confidential 21 Spirent Your Promise Assured

CHALLENGE

• A major carrier wanted to know how they measured against  the competition prior to launching their 5G network so they  could verify and promote that they had the best 5G offering  for their customers

SOLUTION

• Umetrix Data was used to measure HTTP download,  upload, and latency during peak hours and non-peak hours  across 3 cities, 3 carriers, and 3 devices in 10 locations

IMPACT

• Initial test results were disappointing, so the carrier worked on  their backend to make improvements then retested; they were  able to improve their 5G network performance before launch  and substantiate their claims

21

Benchmarking 5G Network  Performance

Spirent  Your Promise Assured

CASE STUDY

Proprietary and Confidential 22 Spirent Promise Assured

Legend

Customer

Spirent

Joint  Define Methodology

Kick – Off

Meeting

DT Tools Preparation

Project Planning

DT Tools Testing and Mock report

Overall Structure

Post Processing (Reports)

RAN On-Air

report

Delivery of

DT work

For Approval and Fine tuning

Define Scope of Work (SOW)

On – Site

Pre - DT checks

After DT, check no alarms during DT

Confirmation/

Acceptance

Planning Preparation Execution Documentation

Spirent Benchmarking Process

Each project customized to your benchmarking objectives

Umetrix LM Logging and Analysis

SECTION 5

Spirent  Promise Assured 24 Proprietary and Confidential

Umetrix LM

• 5G-capable logging solution in the Umetrix portfolio
‒ Supports QCOM , Samsung, and MTK  5G chipsets
‒ Integrates directly with Umetrix Data (Android)
‒ Smaller, portable hardware form factor (USB-C connections)
‒ Simultaneous voice/ call/ data logging for up to 12 devices
‒ Integrates with the Umetrix Voice Server Cloud

• Use cases supported
‒ Correlate RF and signaling information with voice and call QoE  metrics for up to 12 devices simultaneously
‒ Execute Umetrix Data test campaigns with logging to collect layer  1 and layer 3 data to determine possible sources of application  throughput bottlenecks
‒ Performs field based MCPTT measurements on real subscriber  devices (FirstNet, and others) compliant with 3GPP TS 22.179

Spirent  Promise Assured 25 Proprietary and Confidential

Umetrix LM

Logging

• Collect L1 - L3 data directly from the  device chipset
• Voice, Data, and Call monitoring  views
• Real-time mapping with trace lines to  the serving cell sectors
                                                              
• Full playback capability
• Export collected logs to common  interface exchange formats for use in  3rd party post-processing tools
• Integrates directly with Umetrix Data  and Spirent's Voice Cloud

Spirent  Promise Assured 26 Proprietary and Confidential

Umetrix Analysis

Post Processing Solution

• Analyze data collected via the LM air interface logging  software
                                                       
        ‒ User definable filters or threshold limits narrow analysis to
         focus in on network or device performance areas of interest
                                             
        ‒ Isolate device/ network issues for individual or multiple test  UEs
                                             
        ‒ Full drive test replay and one-click synchronization
                                             
        ‒ Functional analysis: call events, signal strength, neighbor  information, full messaging windows
                                             
• One-click standardized reporting engine
                                             
                                             
                                             
                                             
                                             
A trusted partner
```
</details>