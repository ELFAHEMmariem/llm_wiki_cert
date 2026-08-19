# 📄 Fiche Synthèse : Présentation nVent DNS Cooling Overview

---

## ℹ️ Informations Générales

* **Source :** [20220105_DNS_Cooling_Overview.pdf](20220105_DNS_Cooling_Overview.pdf)
* **Thème de la présentation :** Solutions de refroidissement pour centres de données
* **Sujet principal :** Présentation des solutions de refroidissement liquide et hybride de nVent (RackChiller, CDU, immersion cooling) et leurs applications
* **Lieu / Cadre :** Présentation interne (confidentielle)
* **Présentateur / Hôte :** Stefan Djuranec (DNS Cooling Overview)
* 

---

## 🎯 Aperçu et Résumé Global
Cette présentation détaillée de **nVent** (anciennement nVent Hoffman) explore les **solutions de refroidissement avancées** pour les centres de données, avec un focus sur les **technologies liquides et hybrides**. L'objectif est de répondre aux besoins croissants en refroidissement des serveurs haute densité, où le refroidissement par air devient insuffisant. Les solutions présentées incluent des **unités de distribution de liquide (CDU)**, des **systèmes hybrides** combinant air et liquide, et des **solutions d'immersion cooling**. Les innovations clés incluent des **CDU haute capacité** (jusqu'à 800 kW), des **manifolds configurables**, et des partenariats stratégiques pour des solutions intégrées (ex : Iceotope pour l'immersion chassis-level).

---

## 📌 Sujets Discutés (Résumé Moyen)

### 1. **Portfolio complet de refroidissement nVent**
* **Développement de l'idée :**
  nVent propose une gamme complète de solutions de refroidissement, allant des **PDU intelligents** (avec monitoring énergétique) aux systèmes **liquides haute densité** (jusqu'à 800 kW). Les solutions sont classées par **puissance cible** (2–4 kW à 40–800+ kW) et incluent des **rack avec ventilation intégrée**, des **CDU en rack**, et des **solutions hybrides**. Les technologies couvrent l'**air cooling**, le **liquid cooling direct-to-chip**, et l'**immersion cooling** (monophasée et diphasée).
* **Chiffres & Données clés :**
  * 📈 **800 kW** : Capacité maximale du CDU800.
  * 📊 **40 kW** : Capacité du CDU40 (approche à 10°C).
  * 📊 **125 kW** : Capacité du CDU100 (approche à 6°C).

### 2. **Solutions de refroidissement liquide et hybride**
* **Développement de l'idée :**
  Les **CDU (Coolant Distribution Units)** sont au cœur des solutions liquides, avec des modèles comme le **CDU40**, **CDU100**, et **CDU800**. Ces unités gèrent la circulation du liquide de refroidissement (plage ASHRAE W17–W45) et intègrent des **pompes redondantes**, des **filtres**, et des **systèmes de détection de fuites**. Les **solutions hybrides** combinent des **rear door coolers** (échangeurs air-eau) avec des CDU pour optimiser l'efficacité énergétique. Par exemple, un système hybride peut atteindre **100 kW de capacité combinée** (75% liquide, 25% air).
* **Chiffres & Données clés :**
  * 📈 **100 kW** : Capacité combinée d'un système hybride (exemple : Operating Point 1).
  * 📊 **75%** : Part du refroidissement liquide dans un système hybride optimisé.

### 3. **Immersion Cooling : Solutions monophasées et diphasées**
* **Développement de l'idée :**
  L'**immersion cooling** est présentée comme une solution pour les **serveurs ultra-dense**, avec deux approches :
  - **Monophasée** : Utilisation de liquides diélectriques (ex : Novec) avec des **châssis étanches** et des **CDU intégrées**. Avantages : simplicité, faible empreinte, mais nécessite des **racks spécialisés**.
  - **Diphasée** : Évaporation du liquide pour évacuer la chaleur, mais limitée par des **contraintes de pression** et de **perte de fluide**.
  *nVent collabore avec Iceotope* pour des solutions **chassis-level immersion cooling**, intégrant des **pompes et échangeurs** directement dans le châssis serveur.

### 4. **Innovations et partenariats stratégiques**
* **Développement de l'idée :**
  nVent mise sur des **partenariats** pour étendre son offre :
  - **Technotrans** : Fournisseur de **chillers compacts** pour les applications edge (800 × 800 mm).
  - **Iceotope** : Collaboration pour l'**immersion chassis-level** (solution Ku:l2).
  - **Pompes hot-swap** : Nouveau concept de **RPU (Reservoir Pump Unit)** avec modules interchangeables sans outil.
* **Citation / Point marquant :**
  > *"Water cooling is becoming more mainstream and no CDU vendors with single IT rack footprint CDUs have addressed the increasing flow, pressure, and heat requirements of current and next-gen solutions."*

---

## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **Le refroidissement liquide devient incontournable** pour les centres de données haute densité, avec des **CDU haute capacité** (jusqu'à 800 kW) et des **solutions hybrides** combinant air et liquide.
* 🔹 **Les innovations clés** incluent des **CDU modulaires**, des **systèmes hot-swap**, et des **partenariats** pour des solutions intégrées (ex : immersion cooling avec Iceotope).
* 🔹 **L'immersion cooling** (monophasée/diphasée) est une solution d'avenir pour les serveurs ultra-dense, mais nécessite des **infrastructures adaptées** (racks étanches, gestion des fluides).
* 🔹 **L'efficacité énergétique** est au cœur des solutions, avec des **approches à haute température** (ASHRAE W4) et des **systèmes redondants** pour minimiser les temps d'arrêt.

---

## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

```
1 Confidential – For Internal Use Only

Stefan Djuranec DNS Cooling Overview

Jan 27th, 2022

2 Confidential – For Internal Use Only 2

Overview

4 Confidential – For Internal Use Only

Investing inorganically to deliver complete solutions portfolio

Acquisitions and Strategic Partnerships

5 Confidential – For Internal Use Only

CIS Acquisition

Intelligent Rack PDUs Security Access Control and Environmental Management

Energy Meters – Inline Meters

Metered and switched solutions in single and three  phase versions

RP6000 RP2000 RP5000 RP1000

Input Metered Yes Yes Yes Yes

Monitored Switched Yes Yes

Monitored Outlet Yes Yes

 Input metered:

Monitors input power of the entire PDU,
provides unit level monitoring metrics V,A,VA, W, kWh, PF and CB

 Monitored switched:

Remote switching of individual outlets
Control and Manage - On / On Delay, Off / Off Delay, State on Startup, Recycle.

 Monitored outlet

Providing detailed outlet level monitoring

RackPower Series

Single input/output, same function as Input
Metered, typically used for standalone equipment
or legacy PDUs with no intelligence.

7 Confidential – For Internal Use Only

nVent Continuum Of Cooling

COMPLETE PORTFOLIO

Row Aisle Containment

(Active w/IRC) Row Aisle Containment (Passive) Server Rack Server Rack w/Fans Server Rack w/AC

2-4 kW 8-12 kW

15-25  kW

4-6 kW 6-8 kW

25-55  kW

300 mm 600 mm

15 - 35  kW

10-25  kW 10-25 kW

40-800+

kW 40-800+

kW

AIR AND LIQUID COOLING SOLUTIONS

Rack w/Integrated LX Cooling (MicroEdge) In Row Cooling – LX Rear Door Cooling (Passive/Active) Row Coolant Distribution  Unit (CDU)

>25kW

Rack Manifolds

8 Confidential – For Internal Use Only

AIR COOLING SOLUTION

8

Primary Side

Dry Cooler, Chiller  or Adiabatic and  Pumps

Primary (Facility)  Plumbing

RackChiller

Rear Door

Air Loop

9 Confidential – For Internal Use Only

DIRECT TO CHIP COOLING

9

Primary Side Secondary Side

Dry Cooler, Chiller  or Adiabatic and  Pumps

Vertically-mounted Rack Manifold

Primary (Facility)  Plumbing

Secondary (Internal)  Plumbing

Coolant  Distribution

Unit (CDU)

10 Confidential – For Internal Use Only

HYBRID COOLING SOLUTION

10

Primary Side Secondary Side

Dry Cooler, Chiller  or Adiabatic and  Pumps

Vertically-mounted Rack Manifold

Primary (Facility)  Plumbing Secondary (Internal)  Plumbing

Coolant  Distribution

Unit (CDU)

RackChiller

Rear Door

Air Loop

11 Confidential – For Internal Use Only

LIQUID TO AIR COOLING SOLUTION – RPU and RDC (liquid to air)

11

Vertically-mounted Rack Manifold

Secondary (Internal)  Plumbing

Pumping Unit

(RPU)

RackChiller  Rear Door LLC Air Loop

IT Loop

12 Confidential – For Internal Use Only 12

Standard Products

40 Confidential – For Internal Use Only 40

Direct Liquid Cooling

42 Confidential – For Internal Use Only

What were key takeaways? • Water cooling is becoming more mainstream and no CDU vendors with single IT rack footprint CDUs have addressed the  increasing flow, pressure, and heat requirements of current and next-gen solutions • High flow and pressure delivery from the CDU enable more server sub-systems to be cooled with direct liquid cooling • Below chart is from ASHRAE 2020 Winter meeting – chip power roadmap shows majority of chip power will be increasing  past the limit of air cooling within the next 24 months

‒ No "new" technology on the roadmap to move this trend back down to majority of chips able to be air cooled

• As IT OEM vendors target increasingly dense systems, they need a CDU with more capacity to cool ‒ This comes in the form of delivering more flow and pressure

43 Confidential – For Internal Use Only

Architecture Trends – IT System Architecture

Using air to move heat (energy) is expensive and inefficient

Data Center owners increase the coolant temperatures to higher values for better efficiency

High-Density or Direct Liquid Cooling has traditionally focused on  cooling the processors only • Processors typically make up only 35-60% of total IT system power/heat loads

Next generation IT Systems • “Other” ASICs will make up 70% of total IT system power/heat loads  • Processors will be less than 15% of total power/heat load • Focus on HDLC picking up more of the heat-producing  components, such as memory, storage, and power supplies

43

44 Confidential – For Internal Use Only

nVent Hoffman RackChiller CDU800 – Overview

45 Confidential – For Internal Use Only

nVent RackChiller Manifold Platform

Value Prop

- Configurable manifold platform designed to

meet varied customer requirements without  sacrificing velocity.

Benefits

- Design flexibility with multiple configurable  options
- Configurable quantity of quick disconnects
- High flow capabilities
- Stainless and nickel-plated brass quick  disconnects from multiple vendors
- Ease of installation
- Compatible with nVent and/or multiple third- party modular cabinets

46 Confidential – For Internal Use Only *Currently only for hose whip model, expanded offering in development **Some items still in development

nVent RackChiller Manifold Platform

Dimensions

- Compatible with 42U, 48U and 52U racks
- Height will not exceed 1.8m, up to 42 ports
- Standard profile = 1.5” x 1.5”
- Custom sizes available for various applications
- Hose lengths are configurable

Configuration

Supply / Return

Hose Length

Supply / Return  Hose Connector

Number of  Connectors

Connector Type

Hose Whip

Length

Configurable Attributes

Connectors

- Standard
 Parker NSP06
 Staubli SCG06*
- Non-std**
 UQD Series
 Alternate SCG & NSP sizes

Hose Whip
Standard

47 Confidential – For Internal Use Only

nVent Hoffman RackChiller CDU40 In-Rack CDU – Technical Specifications

GENERAL SPECIFICATION CDU

Height 4U / 6.97 in. / 177 mm
Width 16.93 in. / 430 mm
Depth 39.13 in. / 994 mm
Weight - Dry 141 lb / 64 kg
Weight - Filled 164 lb / 74.4 kg
Volume capacity (Secondary) 2.51 gallons / 9.5 liters
Pump Redundancy 3 Pumps for N+1 Redundancy
Power Requirement 100V – 240V 50/60 Hz
Current Consumption 4.44A – 2.47A
Power Supply 2, N+N   970W

OPERATIONAL AND PERFORMANCE

Operating Temperature (coolant) 10°C to 70°C
Cooling Capacity 40 kW at 10°C approach
Primary Flow 80 lpm maximum
Primary Operating Pressure 232 psi maximum
Secondary Flow 65 lpm / 80 lpm maximum
Secondary Operating Pressure* 20 psi
Minimum Approach Temperature 5K
Secondary Coolant Supply Range ASHRAE W17 to W45 (previous W1 to W4)

* Secondary bypass opens at 20 psi, over pressure valve opens at 30 psi

0 5 10 15 20 25 30 35 40 45
0
0,4
0,8
1,2
1,6
2
2,4
2,8
3,2

-10 10 30 50 70 90

Differential Pressure [psi]

Differential Pressure [bar]

Coolant Flow [lpm]

Secondary P-Q Curve (Water) with Tri-Clamp

Default Pump Mode Maximum Pump Performance Mode

48 Confidential – For Internal Use Only

nVent Hoffman RackChiller CDU100 In-Rack CDU – Technical Specifications

GENERAL SPECIFICATION CDU

Height 4U / 6.97 in. / 177 mm
Width 16.93 in. / 430 mm
Depth 37.4 in. / 950 mm
Weight - Dry 137 lb / 62 kg
Weight – Filled 167 lb / 76 kg
Volume capacity (Secondary) 4.12 gallons / 15.6 liters
Pump Redundancy 2 Pumps for N+1 Redundancy
Power Requirement 100V – 240V 50/60 Hz
Current Consumption 15A – 10A
Power Supply 1 x 2500W

OPERATIONAL AND PERFORMANCE

Operating Temperature (coolant) 10°C to 70°C
Cooling Capacity 125 kW at 6°C approach
Primary Flow 170 lpm maximum
Primary Operating Pressure 232 psi maximum
Secondary Flow 115 lpm / 125 lpm maximum
Secondary Operating Pressure* 40 psi
Minimum Approach Temperature 4K
Secondary Coolant Supply Range ASHRAE W17 to W45 (previous W1 to W4)

* Secondary bypass opens at 40 psi, over pressure valve opens at 50 psi

0
5
10
15
20
25
30
35
0
0,4
0,8
1,2
1,6
2
2,4
0 50 100 150

Differential Pressure [psi]

Differential Pressure [bar]

Coolant Flow [lpm]

Secondary P-Q Curve (Water) with Tri-Clamp

Default Pump Mode Maximum Pump Performance Mode

49 Confidential – For Internal Use Only

RackChiller CDU800

GENERAL SPECIFICATION

Height 42U / 78.7 in. / 2000 mm
Width 31.5 inches / 800 mm
Depth 47.2 inches / 1200 mm
Weight dry 2650 lb / 1200 kg
Volume capacity (Secondary) 13.5 gallons / 51 liters
Power Requirement 208V, 50/60Hz, 3 Ph, 11A – 22A
380V – 480V, 50/60 Hz, 3 Ph, 10A – 20A
Power Supply Hardwired Input, optional ATS

Operational and Performance

Operating Temperature ASHRAE A4 5°C to 45°C
Cooling Capacity 800 kW maximum
Primary Flow 913 lpm maximum
Primary Operating Pressure 150 psi maximum
Secondary Flow 850 lpm
Secondary Operating Pressure* 46 psi
Minimum Approach Temperature 4K
Secondary Coolant Supply Range ASHRAE W4 – 2°C to 45°C w/ dew point control

50 Confidential – For Internal Use Only

800+kW of cooling capacity at 4K approach throughout operating range

nVent Hoffman RackChiller CDU800 – Features

Features
- Up to 800kW of cooling capacity @ 4K approach
- Redundant high-performance, leak-free pump system
- Integrated variable speed drives
- Primary (250 micron) and secondary (44 micron) flow filtration
- Coolant connection through top or bottom panels
- Hot-serviceable pumps and motors, filters, and sensors for maximum uptime
- Integrated 10” touch panel display (HMI)
- Remote control features: Ethernet, SNMP v3, Modbus, BACnet with on-board web server for  complete remote control
- On-board leak detection with optional external leak detection
- Integrates with nVent Guardian Management Gateway and sensors portfolio

Benefits
- Unrivaled power density – fits standard data center footprint of 800 mm x 1200 mm (31 in. X 47 in.)
- Serviceable during operation – motors, pumps, sensors, filters, electronics - no need for shut down  during maintenance
- Redundant system layout minimizes risk for single points of failure
- Modular standard design – easy to adapt to customer requirements

51 Confidential – For Internal Use Only

nVent Hoffman RackChiller CDU800 – Major Components

Secondary Supply
Secondary Return
Input Power Feed
Primary Supply
Primary Return
Secondary Bypass
Secondary Filtration
Primary Filtration
Pressure Transducers
Air Vents
Primary Bypass
Redundant Main Pumps
Main Electrical Box
VFD
Electrical Box
Fill Pump
Expansion
Tanks
Heat Exchanger

52 Confidential – For Internal Use Only

RackChiller CDU800

54 Confidential – For Internal Use Only

HYBRID COOLING SOLUTION

An nVent Schroff RackChiller Rear Door Cooler is combined with a Direct Contact Liquid Cooling  Distribution Unit to achieve new levels of rack-level cooling efficiency.

combines

AIR to WATER  HEAT EXCHANGER

and

DIRECT TO CHIP

COOLING

DCLC Rack Manifold
Cooling Distribution Unit

55 Confidential – For Internal Use Only

HYBRID COOLING SOLUTION

Primary Side Secondary Side

Dry Cooler, Chiller  or Adiabatic and  Pumps

Vertically-mounted Rack Manifold

Primary (Facility)  Plumbing Secondary (Internal)  Plumbing

Coolant  Distribution

Unit (CDU)

RackChiller
Rear Door
Air Loop

56 Confidential – For Internal Use Only

Hybrid Cooling Layouts with Temperatures

20 °C
24 °C
60 °C
40.4 °C
38.8 °C
33 °C
25 °C

57 Confidential – For Internal Use Only

RackChiller Rear Door Operating Parameters

Tair,in :  Rear Door Cooler air intake temperature equals the  Server return air temperature

Tair,out : Rear Door Cooler air out temperature equals the  Server supply air temperature equals the  data center room temperature

RackChiller Rear Door 800mm x 2,000mm

Operating Point 1 Operating Point 2 Operating Point 3 Operating Point 4

Operating Point 1 Operating Point 2 Operating Point 3 Operating Point 4

Operating Point 1

Operating Point 3

Operating Point 4

Operating Point 2

58 Confidential – For Internal Use Only

CDU40 Operating Parameters based on Rear Door Operating Points

Server Supply/Return liquid temperatures

CHx80 Performance

ASHRAE W4 (45°C); 25% PG Secondary

59 Confidential – For Internal Use Only

Summary: Example Operating Points Hybrid Cooling Solution

Parameter Unit Operating
Point 1
Operating
Point 2
Operating
Point 3
Operating
Point 4

Server return water temp. [°C] 60 60 60 60
Facilty supply water temp. [°C] 15 20 30 40
Room temp. [°C] 22,5 25 33 41.5
Rear Door Cooler capacity [kW] 25,5 17 11 5,7
RackChiller Rear Door return / CHx80 primary supply temp.
[°C] 21 24 32 41
CHx80 approach temp. diff. [°C] 18,1 16,7 12,7 8,6
CHx80 capacity [kW] 74,8 69 52,5 35,6
Combined capacity [kW] 100.3 86 63.6 41.3
Percentage air-cooled [%] 25 20 17 14
Percentage liquid-cooled [%] 75 80 83 86

60 Confidential – For Internal Use Only

Air-Assist Liquid Cooling – Liquid-To-Air (LTA)

Single-Rack LTA

Sidecar LTA Enables direct-to-chip liquid cooling in air-cooled data centers

No need to retrofit facility water cooling cycle, extend life of existing CRAC
/ CRAH units and aisle containments

Cold aisle air is used to cool the warm liquid returning from equipment

Single-Rack LTA: use pump unit (RPU) and rear door heat exchanger
directly at the equipment rack

Sidecar LTA: integrate pumps and heat exchanger into separate in-row
cooler

61 Confidential – For Internal Use Only

System consisting of
- nVent or customer rack
- nVent or custom manifold (manual or blind mate)
- nVent RDHx
- Reservoir and pump unit (RPU)
- Accessories (PSUs, Monitoring, etc.)

Benefits
- Engineered solution – all components designed for
optiomal interoperability
- RDHx with tool-less hot-swap fan modules with blind-
mate connectors
- Up to 60 kW cooling capacity @
35 °C cold aisle
10 K approach 45 °C coolant supply
Negative 1 inWC pressure from servers

Single-Rack LTA Solution

62 Confidential – For Internal Use Only

Completely integrated Heat Rejection Unit
- nVent rack
- Power supplies
- Heat exchanger
- Fan modules
- Redundant pumps, reservoir
- Leak detection
- Hose package (upon request)
- Manifolds (upon request)

Benefits
- Cooling integrated into separate rack
- Integrated redundant hot-serviceable pumps
- Tool-less hot-swap fan modules with blind-mate
connectors, serviceable from cold aisle
- Up to 80 kW cooling capacity @
35 °C cold aisle
15 K approach 50 °C coolant supply

Sidecar LTA Solution

63 Confidential – For Internal Use Only 63

Immersion Cooling

64 Confidential – For Internal Use Only

Tank Immersion Chassis Immersion

Single-Phase

• Works without pumps within limits • Simple to apply • Ambient pressure operation • Loss of coolant only in case of service
• Large footprint • Requires high amount of coolant • Special immerison racks (tanks) • High media flow

• Low amount of coolant required • Low footprint / standard 19“ • Simpler, water-tight enclosure • Medium complexity to apply • Minimized loss of dielectric
• High media flow

Two-Phase

• Works without pumps within limits • Simple to apply • Low media flow
• Large footprint • Requires high amount of coolant • Evaporation leads to over-pressure • Special, gas-tight immerison racks (tanks) • Loss of dielectric media with time • Dry-boil limit ~ 1 kW per chip

• Low amount of coolant required • Low Footprint / standard 19“ • Low media flow
• Evaporation leads to over-pressure • Special, gas-tight immerison racks (tanks) • Loss of dielectric media with time • High complexity to apply • Dry-boil limit ~ 1 kW per chip

Immersion Cooling Landscape

65 Confidential – For Internal Use Only

Two-stage approach to service customers now and optimize in next evolution

Chassis Level Immersion Cooling

Partnership with Iceotope
- Partnership with Iceotope to leverage „Ku:l2“ chassis design
- Standard server in special, sealed chassis with dry and wet compartments
- Cooling infrastructure (pumps, coolant to water heat exchanger, coolant
distribution) directly inside the chassis
- Requires 21“ rack, fits within standard Varistar CP, lose 1U per server
- nVent Hoffman manifolds
- CDU or RPU where required
- Chillers / Dry Coolers
- Combines with nVent LTA solution

66 Confidential – For Internal Use Only

Stage 2 Concept

67 Confidential – For Internal Use Only

Chassis Level Immersion Cooling (Data Center Application with Chiller)

Primary Side

Secondary Side

Vertically-mounted Rack Manifold

Primary (Facility)  Plumbing Secondary (Internal)  Plumbing

Coolant  Distribution

Unit (CDU)

Chassis Level  Immersion Cooling

Dry Cooler, Chiller

68 Confidential – For Internal Use Only

Chassis Level Immersion Cooling (Data Center Application with Sidecar)

Vertically-mounted Rack Manifold

Secondary (Internal)  Plumbing

Chassis Level  Immersion Cooling

Heat transfered to the air and blown in the room

69 Confidential – For Internal Use Only

Chassis Level Immersion Cooling (Edge Application)

Vertically-mounted Rack Manifold

Secondary (Internal)  Plumbing

Chassis Level  Immersion Cooling

Chiller / Dry Cooler

73 Confidential – For Internal Use Only 73

Cold Water Supply

74 Confidential – For Internal Use Only

Perfect extension to nVent rack-based cooling products

Facility Water for Edge Applications

Partnership with Technotrans
- Comprehensive portfolio of small to mid-size chillers for supply of cold water to single or
multiple racks
- Completely integrated unit, including pump and reservoir no additional facility
installation required
- Small footprint starting from 800 x 800 mm
- Can be combined with dry coolers for superior performance and efficiency
- RS485 for integration with Guardian Management Gateway
- Fully outdoor capable and low temperature rated

75 Confidential – For Internal Use Only

Ongoing Work

76 Confidential – For Internal Use Only

New Controller Platform

New concept for future control platform
Two-component approach
- Passive interface board (green)
- Main microcontroller (gray)
Main controller will be hot-swappable
Support modern communications
protocols, interfaces, features

77 Confidential – For Internal Use Only

RPU With Hot-Swap Pumps

Reservoir Pump Unit (RPU) with
reservoir and redundant pumps
Toolless hot swappable pump modules
Serviceable from front (cold aisle)
Including new hot-swap controller
generation

78 Confidential – For Internal Use Only

THANK YOU!
```
</details>

**Nom du fichier / Source :** 20220105_DNS_Cooling_Overview.pdf
**Contexte / Événement :** Journée de veille 2024