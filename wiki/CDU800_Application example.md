# 📄 Fiche Synthèse : Étude de refroidissement pour Data Center avec CDU800

---

## ℹ️ Informations Générales

* **Source :** CDU800_Application example.pdf (Journée de veille 2024)
* **Thème de la présentation :** Infrastructure IT et refroidissement des data centers
* **Sujet principal :** Étude technique et budgétaire pour l'implémentation d'un système de refroidissement utilisant le nVent RackChiller CDU800
* **Lieu / Cadre :** Non précisé (contexte professionnel technique)
* **Présentateur / Hôte / intervenants :**Jan**
* 
---

## 🎯 Aperçu et Résumé Global

Cette présentation détaille une étude technique pour concevoir une solution de refroidissement adaptée à un data center, en l'absence de spécifications claires du client. L'objectif est de proposer un devis budgétaire basé sur des hypothèses, en utilisant un système **nVent RackChiller CDU800** (unité de distribution de liquide de refroidissement). Le document couvre les composants techniques du CDU800, ses spécifications, une configuration type avec des racks, ainsi que les calculs de performance thermique et de dimensionnement des tuyauteries. Les données incluent des flux de liquide, des températures, des pressions et des recommandations pour les matériaux et valves.

---

## 📌 Sujets Discutés (Résumé Moyen)

### 1. **Objectifs de l'étude et hypothèses de travail**
* L'étude vise à fournir un devis budgétaire pour un système de refroidissement, faute d'informations complètes du client. Les hypothèses incluent l'utilisation d'une **CDU800** (sans RDCs pour l'instant) et de tuyauteries, avec des longueurs estimées similaires à un cas précédent (Volvo).
* Le client n'a pas défini clairement ses besoins, nécessitant des discussions ultérieures pour affiner la solution.
* **Citation marquant :**
  > *"As Jan says, the customer is not really clear what he wants or needs so there will be further discussion."*

### 2. **Composants majeurs du nVent RackChiller CDU800**
* Le CDU800 est un système modulaire de refroidissement liquide pour data centers, composé de :
  1. **Variateurs de vitesse** (1)
  2. **Pompes secondaires** (2)
  3. **Vanne de contrôle primaire** (3)
  4. **Bypass de débit primaire** (4)
  5. **Bypass de filtre primaire** (5)
  6. **Filtre secondaire** (6)
  7. **Pompe/filtre secondaire avec vanne d'arrêt** (7)
  8. **Échangeur de chaleur** (8)
  9. **Bypass secondaire** (9)
  10. **Lignes d'alimentation/retour secondaires** (10)
  11. **Lignes d'alimentation/retour primaires** (11)

### 3. **Spécifications techniques du CDU800**
* **Dimensions :** 2200 mm (H) × 800 mm (L) × 1200 mm (P)
* **Poids à sec :** 1134 kg
* **Capacité de volume (secondaire) :** 51 litres
* **Alimentation électrique :** 380V–480V, 50/60 Hz, 3 phases, 10A–20A (hardwired ou ATS optionnel)
* **Température de fonctionnement :** ASHRAE A4 (5°C à 45°C)
* **Capacité de refroidissement :** 800 kW (nominale)
* **Débit primaire max. :** 913 L/min (pression max. 150 psi)
* **Débit secondaire nominal :** 850 L/min (pression max. 46 psi)
* **Température minimale d'approche :** 4K
* **Plage de température du liquide secondaire :** ASHRAE W4 (2°C à 45°C avec contrôle du point de rosée)

### 4. **Configuration type : In-Row avec confinement**
* **Besoins en débit de liquide par rack :** 1.25 L/(min·kW)
  * Exemple pour 740 kW : **925 L/min** (débit secondaire).
* **Configuration :**
  - Côté primaire : Alimentation par dry cooler, chiller ou système adiabatique + pompes.
  - Côté secondaire : Distribution vers les racks via un collecteur vertical.
  - Températures :
    - Primaire : 20°C (alimentation) → 35°C (retour)
    - Secondaire : 39°C (alimentation) → 27.5°C (retour)

### 5. **Dimensionnement des tuyauteries**
* **Diamètre des tuyaux principaux (secondaire) :**
  * Calcul basé sur la formule : \( D = \sqrt{\frac{4Q}{\pi V}} \), avec \( Q = 925 \) L/min et \( V = 2 \) m/s.
  * Résultat : **DN100** (99 mm) pour éviter la cavitation.
* **Tuyaux de connexion :** Standard 1 pouce.
* **Résumé du système de tuyauterie pour 740 kW :**
  - **Longueur des tuyaux en anneau :** 120 m (variable selon la taille de la salle).
  - **Nombre de vannes :**
    - 28 vannes d'arrêt DN25 (manuel)
    - 36 vannes d'arrêt DN100 (manuel)
  - **Matériaux recommandés :** Acier inoxydable, brides DN100/PN10.

### 6. **Performance thermique et consommation énergétique**
* **Performance pour 1 CDU800 seul :**
  - Puissance de refroidissement : **740 kW**
  - Débit primaire : 705 L/min (pression différentielle 50 psig)
  - Débit secondaire : 925 L/min
  - Vitesse des pompes : **96%**
  - Consommation électrique : **~10.2 kW**

---
## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **Besoin de clarification client :** L'étude repose sur des hypothèses faute de spécifications claires, nécessitant des échanges supplémentaires.
* 🔹 **Flexibilité du CDU800 :** Le système permet une adaptation à des besoins variables (débit, température) via des composants modulaires (pompes, échangeurs, vannes).
* 🔹 **Performance énergétique optimisée :** Avec une consommation électrique de **~10.2 kW** pour 740 kW de refroidissement, le système offre un bon ratio efficacité/énergie.
* 🔹 **Recommandations techniques :**
  - Utiliser des tuyaux en **acier inoxydable DN100** pour les lignes principales.
  - Privilégier des **vannes manuelles** pour un contrôle simple et fiable.
  - S'appuyer sur des **experts** pour l'installation et la spécification finale des composants.

---
## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

```
1

Data Center and Networking

“From the Edge to the Cloud”

IT Cooling Calculation

2

Goals for the study

As we do not have all information needed to do an proper quote, Jan and I agreed that we will
provide an budgetary quote with assumptions. As Jan says, the customer is not really clear what he
wants or needs so there will be further discussion.

Based on this let us do an attempt to provide a cooling solution with 1x CDU800, no RDCs as of
now and piping. We assume there are CRACs in the room.

Also the piping lengths can only be estimated. It will be similar as for the previous Volvo case.

3

nVent RackChiller CDU800 – Major Components

Variable Speed Drives 1 1

Secondary Pumps 2

2

3 Primary Control Valve

3

4 Primary Flow Bypass

4

5 Primary Filter Bypass

5

6 Secondary Filter

6

7 Secondary Pump / Filter  Shut-Off

7

8 Heat Exchanger

8

9 Secondary Bypass

9

10 Secondary Supply / Return

10

11 Primary Supply / Return

11

4

nVent RackChiller CDU800 – Technical Specifications

GENERAL SPECIFICATION

Height 42U / 78.7 in. / 2200 mm

Width 31.5 inches / 800 mm

Depth 47.2 inches / 1200 mm

Weight dry 2500 lb / 1134 kg

Volume capacity (Secondary) 13.5 gallons / 51 liters

Power Requirement 380V – 480V, 50/60 Hz, 3 Ph, 10A – 20A

Power Supply Hardwired Input, optional ATS

Operational and Performance

Operating Temperature ASHRAE A4 5°C to 45°C

Cooling Capacity 800 kW (rated)

Primary Flow 913 lpm max.

Primary Operating Pressure 150 psi max.

Secondary Flow 850 lpm (rated)

Secondary Operating Pressure* 46 psi

Minimum Approach Temperature 4K

Secondary Coolant Supply Range ASHRAE W4 – 2°C to 45°C w/ dew point control

5

Case 1: In-Row with containment

Assuming server coolant need: 1.25 L/(min *
kW)

Server coolant flow per rack: 1.25 l/(min*kW)

* 740 kW = 925 l/min.

6

CDU800 and Racks Configuration

Primary Side Secondary Side

Dry Cooler, Chiller  or Adiabatic and  Pumps

Vertically-mounted Rack Manifold

Secondary (Internal)  Plumbing

Coolant Distribution

Unit (CDU100)

39°C

27.5°C

20°C

35°C

Secondary flow rate (CDU)= 925 LPM

Primary flow rate (CDU)= 705 LPM

7

CDU800 and Racks piping configuration diagram

Connecting pipes

Main pipes

The main  pipe  Diameter can be caculated according to:

D=√(4𝑄/π𝑉) = √(4∗925/(π ∗60000∗2)) = 0.0990 m ,  where  D, Q, V are the pipe diamter, volume flow rate, and  the flow velocity (assume 2 m/s to save from  caviation condition in pipes)

D = 99 mm ~ DN100

The connecting pipes are from standard and it will  be  1 Inch

8

Thermal Performance Summary

1x CDU800 Single DC

740 kW Performance

20 °C Prim. Supply

35 °C Prim. Return

705 l/min Prim. Flow

50 psig Prim. dP

39 °C Sec. Supply

27.5 °C Sec. Return

925 l/min Sec. Flow

96% Pump speed %

~ 10.2 KW Power consumption

9

Summary for the piping system

N configration per room (740kW)

DN100/DN25 Diameter ring pipes

120 m, Depends on the Room  size Length of the ring pipes

DN 100 Diameter interconnect pipes

64 No. Of valves

Shut-off Valve Type of valves

Stainless steel Pipe material

DN 100/PN10 Flange type

28 Shut-off Valve DN25 (Manual)

36 Shut-off Valve DN100 (Manual)

 The type of the shut-off vale should be manuel Control ( for example DN25: Edelstahl Kugelhahn 1  Zoll DN25 1-tlg Absperrhahn Kugelventil  Absperrventil | Sanitärbedarf, Heizung & Sanitär  Wasser Installation Shop (stabilo-sanitaer.de)). I
recommend to be specified from the company will  install for us the RDC and CDU and piping system.

10

Thank you  Work with experts to get the best fitting solution
```

</details>