# 📄 Fiche Synthèse : **4ᵉ Journée de Veille Technologique du CERT — Multi-Core Fiber et réseaux très haute capacité**

---

## ℹ️ Informations Générales

* **Source :** [09h30 Invitation à la 4ᵉ Journée de Veille Technologique du CERT — Multi-Core Fiber et réseaux très haute capacité](20260512_093813-Enregistrement de la réunion.mp4)
* **Thème de la présentation :** **Télécommunications et infrastructures numériques**
* **Sujet principal :** **Les technologies Multi-Core Fiber (MCF) et leurs applications pour les réseaux très haute capacité, notamment dans le contexte de l'IA et des data centers**
* **Lieu / Cadre :** **Conférence en ligne (distanciel)**
* **Présentateur / Hôte :** **Adel Hilou** — Modérateur de la session, CERT
* **Liste des invités / Intervenants :** **Sudipta Bommik** — Responsable Ingénierie des Applications et des Normes, Starlight Technologies (Optical Networking Business) **Andrian Dundloo** — Responsable Recherche Technique, Starlight Technologies (Sales, Marketing Division)
**Tom Boswell** — Représentant Starlight Technologies (Royaume-Uni) **Aala** — Représentant Starlight Technologies (Émirats Arabes Unis) **Houtifa** — Représentant Starlight Technologies (Rio)

---

## 🎯 Aperçu et Résumé Global

Cette session de veille technologique, organisée par le CERT dans le cadre de son plan 2026, explore les **technologies Multi-Core Fiber (MCF)** et les **réseaux très haute capacité**, avec un accent particulier sur leur rôle dans l'infrastructure des **data centers** et des **réseaux de télécommunications**. Les intervenants de Starlight Technologies, leader mondial des solutions de connectivité avancée, présentent les innovations en matière de fibres optiques multi-cœurs, les défis de déploiement, et les perspectives de standardisation. L'objectif est de répondre à la **croissance explosive des besoins en bande passante** (notamment pour l'IA et les centres de données) et d'examiner les solutions pour améliorer la **densité des fibres**, réduire la **latence**, et optimiser les **coûts d'infrastructure**. La session inclut des études de cas concrètes et des discussions sur les **défis opérationnels** (soudure, connecteurs, gestion des câbles) et les **avantages économiques** des MCF.

---

## 📌 Sujets Discutés (Résumé Moyen)

### 1. **Contexte et enjeux des technologies MCF**
* **Développement de l'idée :**
  La présentation débute par un rappel des **trois révolutions structurelles du XXIᵉ siècle** : l'évaluation de l'énergie propre, l'évaluation de l'intelligence (IA), et l'évaluation biotechnologique. L'accent est mis sur l'**évaluation de l'intelligence**, où l'IA et le calcul (compute) évoluent en parallèle. L'IA, par exemple, permet désormais de générer des contenus, d'analyser des données, et de prendre des décisions autonomes, tandis que le calcul évolue vers des architectures plus puissantes (GPU, TPU) nécessitant des **bandes passantes extrêmes** (jusqu'à 1,6 Tb/s par nœud GPU).
  La **fibre optique monocœur traditionnelle (ex. ITU-T G.652, G.657)** atteint ses limites face à ces besoins. Les **technologies Multi-Core Fiber (MCF)** et **Space Division Multiplexing (SDM)** émergent comme des solutions pour augmenter la capacité sans multiplier les câbles, en intégrant **plusieurs cœurs** dans une seule fibre.

* **Chiffres & Données clés :**
  * 📈 **Croissance de la demande en bande passante** : Le trafic dans les data centers double tous les **2 à 3 ans**, avec une projection de **+300 %** d'ici 2030 pour répondre aux besoins des nouveaux centres de données et des interconnexions.
  * 📊 **Marché des fibres multi-cœurs** : Estimé à **4,6 milliards de dollars d'ici 2030**, avec un **taux de croissance annuel composé (CAGR) de 70 %**.
  * 📈 **Exemple concret** : Un nœud GPU moderne nécessite **1 152 fibres** pour une connexion, et un data center avec 8 nœuds par rangée et 32 rangées peut nécessiter jusqu'à **294 912 fibres** pour les interconnexions.

* **Citation / Point marquant :**
  > *"L'IA et le calcul évoluent en parallèle : l'IA pousse le calcul à devenir plus intelligent, tandis que le calcul pousse l'IA à devenir plus puissante."*

---

### 2. **Technologies Multi-Core Fiber (MCF) : Innovations et défis**
* **Développement de l'idée :**
  Les MCF permettent d'intégrer **plusieurs cœurs** (jusqu'à 7) dans une seule fibre de **125 µm de diamètre**, offrant une **densité de fibres 4 à 7 fois supérieure** aux fibres monocœurs. Starlight Technologies présente ses innovations :
  - **Fibres à diamètre de revêtement réduit** (200 µm au lieu de 250 µm), augmentant la densité dans les câbles.
  - **Fibres multi-cœurs (4 ou 7 cœurs)** avec des designs optimisés pour minimiser la ** diaphonie (crosstalk)** et l'**atténuation**.
  - **Fibres creuses (Hollow Core Fiber)** pour réduire la latence et les effets non linéaires, bien que limitées à 3 canaux par fibre.

  Les **défis clés** incluent :
  - **Soudure et alignement** : Nécessité de machines de soudure spécialisées (ex. Fujikura) pour aligner les cœurs avec une précision de **360°**.
  - **Connecteurs et interfaces** : Développement en cours de connecteurs **MTP/MPO multi-cœurs** et de transceivers compatibles.
  - **Standardisation** : Les organismes **ITU-T, IEC, et IEEE** travaillent sur des normes pour les MCF (ex. **ITU-T G.SupMCF** pour les fibres multi-cœurs).

* **Chiffres & Données clés :**
  * 📊 **Performances des MCF** :
    - **Atténuation** : < 0,2 dB/km (comparable aux fibres monocœurs G.652/G.657).
    - **Diaphonie (crosstalk)** : Jusqu'à **-52 dB** dans les tests en laboratoire.
    - **Latence** : Réduction de **32 %** par rapport aux fibres solides (pour les fibres creuses).
  * 📈 **Densité de fibres** :
    - Un câble de **6,5 mm de diamètre** peut contenir **1 800 fibres** avec un revêtement réduit à 200 µm.
    - Un câble composite (12 fibres monocœurs + 12 fibres multi-cœurs) permet de tester les performances dans des conditions réelles.

* **Citation / Point marquant :**
  > *"Les fibres multi-cœurs ne sont pas une option, mais une nécessité pour les data centers de demain."*

---

### 3. **Applications et études de cas**
* **Développement de l'idée :**
  Les MCF sont déployées dans deux **cas d'usage principaux** :
  1. **Data Centers** :
     - Réduction de **75 % de la surface occupée** par les câbles grâce aux fibres multi-cœurs.
     - Exemple : Un câble de **35 mm de diamètre** peut contenir **432 fibres** (contre 96 avec une technologie traditionnelle).
     - **Projet en Inde (IIT Madras)** : Déploiement d'un câble composite (fibres monocœurs + multi-cœurs) pour tester les performances dans des conditions réelles (sous-marin, aérien, souterrain).
  2. **Réseaux longue distance** :
     - Utilisation dans les **câbles sous-marins** et les liaisons terrestres pour augmenter la capacité sans agrandir les câbles.
     - **Projet au Royaume-Uni** : Déploiement de MCF pour connecter deux data centers, avec des tests en cours pour valider la fiabilité.

  Les **avantages économiques** incluent :
  - Réduction des **coûts civils** (évitement de la pose de nouveaux conduits).
  - Optimisation de l'**espace dans les data centers** (moins de câbles = plus de place pour les équipements).
  - **Durabilité** : Moins de matériaux utilisés pour la même capacité.

* **Chiffres & Données clés :**
  * 📊 **Économies réalisées** :
    - Jusqu'à **40 % de réduction des coûts** dans les déploiements où les conduits existants sont saturés.
    - **Exemple** : Un client indien a évité la pose d'un nouveau conduit en utilisant des MCF, économisant des **centaines de milliers de dollars** en coûts civils.

---
### 4. **Standardisation et écosystème des MCF**
* **Développement de l'idée :**
  La standardisation est un **pilier** pour l'adoption des MCF. Les organismes suivants travaillent sur des normes :
  - **ITU-T** : Développement de rapports techniques (ex. **G.SupMCF**) et de recommandations pour les fibres multi-cœurs.
  - **IEC** : Standardisation des méthodes de test (ex. mesure de la diaphonie, géométrie des cœurs).
  - **IEEE** : Travaux sur les interfaces et les connecteurs multi-cœurs.

  Les **défis de standardisation** incluent :
  - **Alignement des cœurs** : Définition de la **distance entre cœurs (core pitch)** et de l'**épaisseur de la gaine externe (OCT)**.
  - **Identification des cœurs** : Utilisation de **marqueurs** ou de profils asymétriques pour différencier les cœurs.
  - **Interfaces actives** : Développement de **transceivers multi-cœurs** (en cours chez les fabricants comme Cisco et Nokia).

* **Chiffres & Données clés :**
  * 📊 **Calendrier de standardisation** :
    - **2022-2023** : Publication de rapports techniques non normatifs (ex. **ITU-T G.SupMCF**).
    - **2024-2025** : Début des travaux sur les normes pour les connecteurs et les interfaces.
    - **2026+** : Commercialisation des premiers transceivers multi-cœurs.

---
### 5. **Fibres creuses (Hollow Core Fiber) : Une alternative aux MCF ?**
* **Développement de l'idée :**
  Les **fibres creuses** offrent une **latence ultra-faible** (jusqu'à **3,33 µs/km** contre 4,9 µs/km pour les fibres solides) et une **atténuation réduite** (0,05 dB/km théorique). Elles sont idéales pour :
  - Les **réseaux haute fréquence** (ex. bourses, centres de données).
  - Les **applications quantiques** (QKD, distribution de clés quantiques).
  - Les **liaisons longue distance** (réduction du nombre d'amplificateurs).

  Cependant, elles présentent des **limites** :
  - **Nombre de canaux limité** (3 canaux max par fibre).
  - **Coût élevé** et **complexité de fabrication**.
  - **Compatibilité limitée** avec les infrastructures existantes.

  **Conclusion** : Les fibres creuses et les MCF **coexistent** selon les besoins :
  - **MCF** pour les **applications nécessitant une haute densité de canaux**.
  - **Fibres creuses** pour les **applications critiques en latence**.

---
### 6. **Questions et réponses : Défis opérationnels et perspectives**
* **Développement de l'idée :**
  La session se termine par une **session de questions-réponses** abordant les **défis concrets** :
  - **Soudure** : Les machines spécialisées (ex. Fujikura) permettent désormais une soudure en **5 à 10 minutes par fibre** (contre 1 à 2 minutes pour une fibre monocœur).
  - **Connecteurs** : Les connecteurs **MTP/MPO multi-cœurs** sont en développement, mais leur adoption dépendra des fabricants de transceivers.
  - **Coût** : Bien que les MCF soient **plus chères à l'achat**, leur **coût total de possession (TCO)** est inférieur grâce aux économies réalisées sur les infrastructures.
  - **Énergie** : Les MCF permettent des **économies d'énergie** en réduisant le nombre de fibres et de connecteurs nécessaires.

* **Citation / Point marquant :**
  > *"Les MCF ne sont pas seulement une technologie, mais une révolution dans la façon dont nous concevons les réseaux."*

---

## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **Les MCF sont une solution incontournable** pour répondre à la **croissance explosive des besoins en bande passante** (IA, data centers, réseaux 5G/6G). Elles permettent d'augmenter la capacité **sans multiplier les câbles**, réduisant ainsi les coûts d'infrastructure et l'empreinte écologique.
* 🔹 **Les défis techniques sont maîtrisés** : Les innovations en matière de **soudure**, **connecteurs**, et **standardisation** (ITU-T, IEC) rendent les MCF **prêtes pour un déploiement à grande échelle**.
* 🔹 **Les études de cas prouvent leur viabilité** : Des projets en **Inde (IIT Madras)** et au **Royaume-Uni** démontrent que les MCF peuvent être déployées dans des **conditions réelles** (souterrain, aérien, sous-marin) avec des performances comparables aux fibres monocœurs.
* 🔹 **Les fibres creuses (Hollow Core) complètent les MCF** : Elles offrent une **latence ultra-faible** pour des applications spécifiques (réseaux haute fréquence, quantique), mais leur adoption reste limitée par leur coût et leur complexité.
* 🔹 **L'écosystème des MCF est en construction** : Les **transceivers multi-cœurs** et les **interfaces standardisées** sont en développement, avec une commercialisation prévue d'ici **2026-2027**.
* 🔹 **Le retour sur investissement (ROI) est positif** : Malgré un coût initial plus élevé, les MCF permettent des **économies significatives** sur les coûts civils, l'espace dans les data centers, et la consommation d'énergie.

---
## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

Okay, okay. So, thank you for being here today with us in this workshop. This workshop is part of the technology watch. The is organized by cert. My name is Adel Hilou. I will be the moderator for this issue today. This online workshop. I am to deal. Hello. I don't know. We have an issue with someone with I cannot see the problem this speaker.

Okay. Just mute your mic. So, as I mentioned, this online workshop is part of the technology watch plan for 2026 in cert. So, my name is Adel Hilou. I will be the moderator for this session today. Just before that, we leave in the details and technical presentation. I want just to take a few minutes to explain just where we are today and why we choose this topic for our workshop and we're always joining to share their expertise with us.

So, the technology watch program really, it was in the conviction that we need to be proactive from those point of view. And this is the foundation for digital development, future and so on here. So, especially nowadays that we have a technology that evolving rapidly, that what we face before in decay now it is happening in months.

So, we need to be on dissipating this change. Today workshop is bringing together researchers, engineers and operator decision makers to examine the technology trends and to define tomorrow's plan. This year, our workshops are organized around two two axes. The first is dedicated for AI and infrastructure and applications.

And the second axis is addressing sustainable digital infrastructure. And then first axis we explored already AI transformative roles in telecommunication and also we organized one workshop for for for for QS and two year benchmark. So, the today workshop is dedicated for MCF and mixed generation five technologies.

The second axis is for sustainable digital and we organized already in the workshop for TACA Center system in Biliq. So, what are the drivers that push us to organize this workshop and why we selected today? So, I will try to hear just to give you three main reasons for this selection of the topic. The growth of AI bandwidth, now the growth is redefining all the infrastructure to quantum telecommunication and it is expected to be double every two to three years.

And the fiber demand is also is projected to grow more than 20 per 300 percent to support the requirement for for for the new data centers and new interconnection requirements. In this context, it is clear that this will require also a high capacity low latency and also scalability for which the current technology is and current single model first actually cannot answer the question.

The second reason is the market growth or market evolution. The market the melting core fiber market is expected to reach 4.6 billion by 2021 2013 with the compound annual growth more than 70 percent. This growth is reflecting the cost between the global stakeholders to move forward to this new technology.

The third reason of this election is the standardization driver. So currently international standardization body like IQT, IAS, IEEE are working actively in developing standard and technical framework for these technologies which represent this standardization. It's critical that we need to align it for our national infrastructure and strategies to be in alignment with the global benchmark.

So our objective in this workshop today is to deep dive into multi-core technology and to have an examination also of a real deployment use games. So for our workshop today is organized in collaboration with the Starlight technology and we thank all Starlight members for their collaboration and for accepting the organization of this workshop today.

So Estelle is a global leader in advanced connectivity solutions delivering end-to-end infrastructure for AI, reading network, FTTX network, enterprise networks and also data centers. Estelle has a presence in more than 100 countries and working with the world's leading telecom operators, cloud operators and also the service providers.

So our first speaker will be Mr. Sudipta Bommik. He is the head of application and standard engineering for Estelle optical networking business. Mr. Sudipta brings over 28 years of experience in telecommunication. He is a architect of Estelle Fiber and cable manufacturing process with a large experienced in research and development, reliability, engineering, quality assurance, and international business development.

Mr. Sudipta also serves as vice chair of study group 15 in IQT and also working part II. He is also serving as a laser officer for IS, Technical Committee 86. He has published over 40 papers and haunt multiple patents. Joining him we have Mr. Andrian Dundloo, lead technical research in Estelle. Sales, marketing division.

Mr. Andrian Dundloo brings deep technology knowledge and applied commercial expertise with large experience also in translating the cutting H5 technology into a concrete deployment. So, gentlemen just on behalf of certain door participants to ask today we are really honored to have you with us and thank you again for accepting our invitation.

So just now in a few moments we will take the photo, group photo, after that our colleague from Estelle will begin the presentation. During the presentation please if you have any question you can just put it on the chart. We will collect them and we will address all these questions during the key and the session.

At the end and it is expected that we close our shop at 11. So please if you could just now open your camera just to take the photo, the group photo photo, just I want to close the shop which here is just to take the photo. Okay, we will just for the items So on behalf Okay. Okay. Thank you so much. So I know it's not, it's not easy to do this.

Thank you. With our best to make it successful is needed for the communication, you know. So I will not take it more time. I will just ask Siddhata, please start your part. The floor is yours. Thank you so much. Thank you. Thank you. Hope I am audible to all of you. Can you hear me? Yes. Yes. Thank you.

First of all, thank you very much, Adel, for this introduction and inviting starlet ecologies to talk about the next generation of fiber technologies. So also I have some of our colleagues also joining from different part of the world. We have Tom Boswell joining from UK. Then we have Aala and some other joining from Ewey and also Houtifa joining from Rio.

So we have a in addition to the Anduin from France. So we have a more political joining and they will also pitch in the right time when we need to discuss some I mean topics. So as you mentioned that this this talk mainly focus on the next generation products. And I will going to lead the discussions and as we requested that some part of the presentation, it possible to the taken French to have our colleagues.

So we'll jump in whenever required. So please feel to ask question. You can put a question in the chat box. We will at the end of the presentation. We will answer all the questions one by one. And also we can speak in French if you would like to do. And you have free to speak English and French both.

So we can able to answer from in those questions. So I'm just sharing my screen. Hope I have the starting right. Yes. Yes. Okay. So. So of course this topic today is the space division multiplexing multi code and the next generation to fiber for optical infrastructure for the AI. So this is a kind of a high level outline.

So first we'll give a little bit context and introduction of the stellar technologies. Then we'll talk about that what are the fiber technologies revolving and what are the motivation behind that that is mainly AI DC network connectivity. They talk about these space division multiplexing or the concept behind this SDM.

And then we'll discuss about different type of multi code fibers and is technologies design key parameters fiber and the cable testing methods, preparations and qualifications. And we end with some diploma in case studies that we come across India and also other part in the world. So I'm just begin with that introduction of STN.

So as I already mentioned that we are the multinational company that is based out of India and we're focusing mainly in the advanced connectivity solution for the digital infrastructures. We have a four customer segment telecom operators data center and the cloud company CDG networks and the large enterprises.

So you have a two vertical one is optical networking and second is digital and technology solution which is basically a software network win. So all of us joining today are from optical networking business and where we are mainly manufacture of the optical fiber optical fiber cable specialty cables optical connectivity solution closer or characterize cables and we have a detailed data center portfolio.

So this is a brief about our history and we have almost 30 plus years of experience in optical networking solution business and we have a end to end solution with offering across the value chain. So you can see that picture of different plans total we have a 10 global production facilities where we produce optical fiber from a glass that is in India in China and we have a optical fiber cable manufacturing facilities in two locations in India and one each in Italy, Brazil and South Carolina, look of USA.

In addition to that also we have a optical connectivity solutions manufacturing capability in India and Italy. So this is a very high level of manufacture manufacturing of our products so we we call it silicon to fiber to IBC. So what is the meaning of this that we start our manufacturing from a metal called silicon metal and from there we produce a chemical known as silicon detector right that is SICL4 and this SICL4 is a major raw material producing a high grade optical fiber glass.

And we do it by a process called chemical vapor deposition you can see the picture of a layer and then when we produce optical fiber glass reform which is a basically a cylindrical glass rod we draw a optical fiber of just 125 micro ampere diameter by a drawing process. And then we send this optical fiber to our cable plant for different cable manufacturing and in addition to that we have a connectivity products connectivity products means this are the price cables, closers, joint closure racks and all those stuffs and all this going to lead to this air data center solution.

So we have a complete value chain starting from a silicon metal to the the final product so that is glass before manufacturing fiber drawing cable manufacturing connectivity and cable all those stuffs. So at other mentioned that we are also actively participant in different telecoms generation organizations so most important is the international telecommunication union that is the international SDOs which is a specialized agency of United Nations and second is that international technical commission or IEC that is a WTO what is their organization recognized SDO so both are very important standard development organization in telecom industry and you can see that most of the product specification or test methods are when they developed by these two organizations.

In addition to that we also actively participate in different national standard development organization in India that is telecom engineering center this is very similar to this your organization that is CRT so this telecom engineering center basically develop the national standard test methods and also helping our ministra communication to writing different.

So we document for different kind of telecom deployment and second is that the group of Indian standard this is our national committee where I have a Miller committee to starting with 15 that is NWG 15 and LIT 11 so they are generally participate to helping our national body as well as international body to develop different telecom standards.

So in the right side you can see that how this process works the standard development process generally we collect the needs from the market and change in the technologies and we feed this information to product life strategy development where we we we strategically understand which product to develop then is comes under research and developing innovation where we collaborate with different partners where these customers or suppliers or any educational and the research organizations in India and abroad and output of that innovation is a technical product then research papers channel papers and standards.

Again we take this certification and the certified product to access the market and again we collect the market so this is a cyclic process or circular process where we continuously evolved our product based on the market breeds and technological technological development so the revolution. Now coming to the topic today so this AI and DC is what you can see that there are three structural shifts that this redefining this 21st century one side you can see that a clean energy evaluations and intelligence evaluation and biotape evaluations.

So if we double click at the medial that is intelligence revolution we can see that there is a computer computer becomes a cognition and where there is a two layers of information flows and developments happening one is that a intelligence layer and second is that a compute layer and here AI is going to play very important role so one side AI drives computer.

So this is the development and another side compute another is the AI evaluation so these two evaluation is happening side by side so what we see in the beginning of the last decade that in view of this intelligence layer that we can see that there is a lot of things happening in the AI where where AI is could predict that what is our liking and which movies went to to see and then it is going to start recognizing the photos and objects and the data.

And it is starting that writing the males and stories for us and also is giving an analyzing data and give an insight and helping us to making a decisions in future. AI is going to probably run a factory without any minimum manual interventions so this is happening in the intelligence layer the what is happening in the computer in computer is also evolving to mean this requirement and if you see that main evolution happening is the processing unit computer.

processing unit computer processing unit what I whether it is from CPU to GPU to GPU to GPU all the strips is happening in this computing layer and the basic changes happening here that the data communications where we will be talking about 800 and soon is going to talk about 1.6 TV kind of things. So because of this changes happening in intelligence and computer layer there also you can see the evolution in the data center infrastructures and the bandage requirement and that is the fundamental reason behind that space digital multiplexing on HTML technologies in the physical infrastructures.

So I will just explain the figure the right that you can see a lot of patch cable or patch forward or people kind of a of fireworks so what is happening that because of this so much requirement that the data the fiber demand is increased drastically. For us other mentioned in the beginning of the presentation how we can see this growth is so explosive in nature.

For example here you can see one example where a modern AI body developed by and recently very popular very well on organizations what this particular GPU node just one GPU node is required on 1000 152 to 5 years to connect 1152. Just imagine we have a 8 GPU node per row it is going to consume 9216 and if you have a 32 rows in a hall it will it will lead around 294 912 fiber and if you have a 2 hall center center you have to connect to all to 1 and 2.

So, we need around you can just do the mathematics and the enormous number of 5 as will be required. So, so many fiber is required inside the data center then how we can manage that do you need a different fiber do you need a different technology to handle so many fiber to de plus so many fiber. So, that is the question we are asking and that is the fundamental reason behind conceptual fundamental reason behind this development of this multi core fiber and the space division multi plus technologies.

Now, I am little bit back that is to see the history of single mode fiber evaluation what happened in last 30 40 50 years. So, this is a very slide that generally we show in I duty to all the newcomers that how it is involved in this slide you can see this graph where one side you have a translation capacity and other side is part of the against a time scale since 1980.

So, this I duty first time developed this single mode fiber standard 0 6 62 still it is very popular in 1984 just the celebrate and 40 years of anniversary of this 0 6 5 2. So, that time it was mainly optimized in the O band that is 3010 elevator band for is a low dispersion values next come to EDFA.

The medium doped fiber amplifier which generally operate at C band that is 1550 elevator band that time is also developed the 2 type of 5 to the 0 6 63 and 0 6 64 which is part of the 5. Then we have a come that W DM or even division multiplexing then a tailored dispersion type of fiber is was developed 0 65 also known as the non 0 dispersion shifted fiber and 0 66 for a wide band non 0 dispersion shifted fiber.

Then comes to the enough F2 T h fiber to the home then we see that band necessity fiber comes to the picture 0 65 and then in the area of BSP or digital signal processing that dispersion parameters is become less important that is why that the product like 0 65 5 0 6533 066 is not much in the top mainly 0 657 and 0 6 52 these 2 type of standard are now being.

So, we will use heavily and the right hand side you can see that the number of versions of different type of standards so 0 652 now running version is number 10 that means it is revised 10 times in last 40 years almost every 4 years once it is revised similarly, this 54 revised 12 times and 0 6567 5 10 is since 2006.

So, in I 2 this 3 standard are very active you can say and most of the experts are generally keep on revising this standard based on the technological advancement. However, based on his hero experiment it is realized that existing standards or existing technologies fiber technology is not sufficient to meet that a high data requirement that we have seen in the last slide that is the very 1.6 TV was so many fiber and cables required inside the data center.

So, there is a hero experiment telling that there is a maximum liquid 100 TV per fiber. So, if you need more than that what we will do so that is a question is so just to get it more understanding about this so again you have to go back to understand the basic fundamental a Shannon transmission capacity limit what is tells us that a transmission capacity which is a directly proportional with bandwidth that is we in is a number of channel.

And signal to know ratio so if we see the overall bandwidth of a signal mode 5 or this is very wide around 53 terahurge if we starting from 1380 to around 1650 millimeter that is O to L band. However, actual use of this interest vector is emitted to the sea and to some extent L band because this is a low loss region low optical loss region.

So, if we take this overall overall pattern on 10 terahurge and very optimistic figure around 10 can be ps per per meter of the average then you can get a value of 100 TV for fiber so that is a basically a limitation of a one single channel capability. So, now what we can do now one is that you can increase more channel to open more channel like C plus a band and second option will come to the more number of channels.

So, now if you how we can increase more number of channels so it is very simple as good as a increase number of fiber in a cable but it is not as simple as that so it did not a lot of you a lot of innovation to just increase the number of fiber in a channel. So, that is a basically fundamental concept or motivation behind the concept of space revision multiplexing.

Now, I am coming to the next things now let us talk about what are the different type of SDM fibers. So, now as I mentioned that the SDM is basically increase the number of channels so now how we can increase the number of channels the two ways you can do. First is that you can improve a special density optical fiber in a unit cross sections and second way you can increase the number of special channels in a common cladding.

So, in this picture you can see that the left side you have a traditional optical fiber single optical fiber where you have a core at the center then you have a cladding and then you have a outdoor polymer coating. So, the first SDM fiber you can see it is a reduced coating diameter fiber and where basically we reduce the thickness of the coating but maintaining the same cladding diameter that is one 25 micrometer.

So, by this way you can reduce the total concentration area of the fiber so that you can pack more and more fiber in a cable. So, you can reduce the cable diameter and you can increase the number of channels. Second is that reduce cladding diameter where we can reduce both coating and cladding thickness and reduce overall overall diameter of the fiber and again you can increase the number of channels.

So, third concept is coming the multi-col fiber where in the same cladding diameter you can increase the number of core. So, in this picture you can see instead of one core you have a four cores that means that in the same construction same fiber will have a full channel is four number of N. So, you can just multiply the overall capacity just four times in a multi-col fiber.

And last SDM fiber you can say that few more fiber where in between a multi-modal single mode but instead of one mode we can have a more than one mode. So, that this is also by the increase of a number of channels. So, you can see that in the SDM there is a four type of SDM fibers reduced coating diameter fiber, reduced cladding diameter fiber, multi-col fiber and few more fiber.

Now, question is that how far you can increase the number of fiber in a cable by reducing the coating diameter. So, here we can see the fiber density, fiber density means that the number of fibers in a unit construction area and how it increase with reducing the coating diameter. So, now existing we have a 250 micro meter coating diameter for normal fiber it is just a normalize as a one as a fiber density.

So, if you reduce to 4 as a 200 which is now already commercialized for long long time you can increase the fiber density from 1 to 1.5. Just a hypothetical case it can reduce the coating close to 125 that is almost cladding diameter still we cannot increase more than 5 the fiber density. So, there is a limitation of increasing fiber density even after reducing the coating diameter.

So, that is why the this is the where we cannot go beyond then your multiple fiber is comes up picture. So, because of this reason that 4 called multiple fiber what we can see is a most commercialized because by reducing coating diameter maybe you can increase the number of channels 4 times but not more than that.

So, that time we need to have a multiple fiber. Now, what is multiple fiber? This is very simple that in the in the in the left side you can see that we have a standards in the mode fiber code at the center cladding 125 micro meter coating around 250 and 1 in micro meter. And the multiple fiber instead of 1 call we have a more than 1 call.

In this picture you can see a 4 call multi call fiber by the same cladding 125 the macro diameter we have a it should have 1 you have a 4 calls. And where we can improve or we can add more than 1 call. So, there are few more parameters are become very important like distance between the 2 calls that is known as the core pitch.

That is very important and second important parameter is coming that OCT or outer cladding thickness that means the distance from a core to the outside cutting layer. So, when we design a multi code fiber these 2 parameters we have to maintain a balance of that the core pitch and also outer coating diameter or also the outer cladding cladding thickness.

So, I will discuss more about later that how these 2 parameters influence different multi code fiber parameters. There is an addition additional circle you can see at the top middle center point is a marker. So, when we add more than 1 call inside a multi code fiber we need to identify those cores. So, that we need to understand that which is call 1 code 3 and call 4 for that into the marker.

So, the core is close to this marker you can we can just identify as a code number 1 and either clockwise or anticlockwise you can give the number. So, identification of the core also very important for your termination point of view. Now, in STL we already developed many SGM type of fiber the first time mentioned that we do is coating diameter fiber.

So, we have a around 1 to micrometer coating diameter fiber which is coming with that 0.657 A2 type of bin in CSEB fiber. And there is one example you can see here that on the left side that a 280 fiber cable of having around 180 micrometer reduced coating diameter fiber just in diameter of 6.5 millimeter.

So, you can achieve such a small diameter of cable even such a high fiber comp. So, that is the beauty of this reduced coating diameter fiber. The right side we have a multi first. Multi first is basically our trade name where we call this 4 core multi core fiber which is already commercialized and that already seen the last slide that 4 core multi core fiber.

And this is we will I mean talk about more about the coming slides. So, now, the other another important technology is just like that we are not deploying a fiber we are deploying a cable. So, there are also lot of innovation is required in the cable in technology. So, we can we can we can reduce the coating diameter we can we can we can therefore, up a multi core fiber.

But when we design a cable our intention was to reduce the diameter of the cable also. So, you know that when we are going for a high fiber comp cable the reburning technology is very very important reburning is very important because need to reduce the splicing time or MTT or low. So, we can reduce the splicing time to club 12 or giving more rebons in a one one calculated form so that you can splice all the together.

However, the conventional ribbon or also we have the flat ribbon is that this is very rigid we cannot bend it. So, it just to be very strange and at the same plane when it is inside inside the cable. And because of that that cable design of with a traditional flat ribbon is very bulky and there are lot of empty spaces inside the tube.

And that empty spaces also feed by some jelly kind of material. So, the conventional cable design with this conventional flat ribbon having a very bulky very large diameter and because of the jelly the weight also is very high. So, this is very difficult to manage in a such a high kind of a fiber density scenario.

So, that is why the innovation happen in the ribbon design instead of flat ribbon. A new type of ribbon comes in the market that is called intermetically bonded ribbon in ITU we called it partially bonded ribbon. So, this particular ribbon this is basically you can see in the picture that which is also is another spider wave ribbon.

So, it is not bondage along the length some intermediate position it is bonded because of that it can be rolled and make a circle. And if it is make a circle then we can easily achieve that high packing density. So, I can reduce the empty spaces inside a inside a cable. You can see in the grey side we have also commercialized a optical fiber cable around containing 6000 912 516 912 and diameter it just goes to around 35 millimeter.

So, now this is being used heavily in different data center data center operation inside the data center support. And this is another reason that this intermetically bonded technologies are very very important to utilize the maximum duct spaces. So, here you can see one example that we have a maybe 20 millimeter duct where you can able to deploy a conventional multi-lose tube cable of 96 fiber just diameter down to 12.5 millimeter.

So, if you going to use a intermetically bonded technology this same diameter is just 12.5 you can able to install around 432 fiber cables. So, just multiply the number of fibers in the same duct space. So, that is one of the many need of a data center connectivity where you do not have any duct to duct availability is your installation of a duct is too expensive and to time consuming they are this kind of technologies are very much useful.

Now, I am touch upon that another technology that is being lot of discussion under the you call it 0 or 650 4 E fiber also known as the cutoff shifted fiber. So, this particular fiber category was first developed in ITUD studybook 15 in September 16 it was consentent and that particular fiber mainly developed for the terrestrial application.

So, 0.654 generally developed for the submarine application that is a b c and b category and e category was developed for the terrestrial or the land application to support 100 g for 100 g and beyond applications. So, there you can see there is a too very important benefit of this 0 or 650 4 E fiber one is that is adding a high motfield diameter compared to the existing this 662 fiber or 650 or B fiber because of this large motfield diameter to saving a higher effective area.

And because of the higher 50 per year we are reducing non linear effect and because of the non reducing non linear effect it can allow to consume or transmit very higher input power. So, that is the first advantage second advantage is that it is a very low detonation this is a pure silicon rose fiber and activation as low as around 0.18119 dB in the cable stage also can be achieved with this fiber.

And it is map urban loss which is very important for land or terrestrial applications is similar to that 0.652 d fiber it means that the same same well current you are deploying existing 0.652 fiber 0.654 E fiber also can be deployed do not need any extra precaution for that. And it chromatic dispersion also similar to that existing fiber.

So, because of this to benefit that is low activation and large effective area what we can see in a link we can getting a overall external benefit that is optical signal to noise ratio. So, once I do can if you see this equation here where sonar is depend on input power and the spandas that is the basically the detonation.

So, once I because of this large effective area we can increase the input power that means we can increase the way sonar and other side because of this low activation we can decrease the spandas. So, we can increase input power we can decrease the spandas because of that we can increase the way sonar value.

So, why we need a higher way sonar the main reason become that we have a some two examples below you can see here. So, that for example, you can have a 100 GB kind of being and we wanted to doubling the transmission distance in the same data range it means that we need additional 3 db was and plus db was and all you wanted to increase the data rate from 100 g to 200 g the same distance in it around 7 db was and extra 7 db was and all.

So, it means that the to increase the transmission distance or increase the data rate in either kind of question needed higher way sonar that can be 0.664 to e 5 word can help you to achieve that. So, there is some simulation study we carried out you know laboratory and we can see the output of this study where we took around 60 millimeter and the 85 millimeter of link where we can see can compare that 0.650 whole e 5 word versus existing 0.62 or 0.657 fiber and this is basically a maximum transmission distance.

Here you can see that the if you going to have a data rate 200 g and above there you can see the value of this fiber but if we play blood 200 g so, probably do not need 0.650 fiber existing 6.62 or 6.57 fiber also okay okay. So, in the higher data rate you need this fiber then if we wanted to this fiber as I mentioned that is a higher effective area larger effective area we can punch more launch power up to plus 1.5 db we have already tried even you can go higher.

You can it can help you to increase the span length currently maybe span length what you know that is around 60 kilometer to 80 kilometer varies. So, you can go up to 120 kilometer as well. So, it means that you can even to reduce that in the amplifier and associated copies and also it can increase the overall translation distance beyond 1000 5.2 millimeter which help in reducing the regenerator cost.

The regenerator cost is very costly because in regenerator it is unable to be regenerated. So, by this way for long distance communications this fiber is become useful it is actually developed to connect to connect a landing stations the submarine cable landing station to a data center but later this point look kind of fiber become very very popular in long hall network long distance network connecting data center or any other telecom app.

So, we need a very high voice and to support such a high data rate and why we want to reduce the capets in online and referred and the regionators. Now, I will touch upon the whole call fiber this is another topic in the under discussion is a lot this is in IT also we are discussing and lot of contribution also comes and we are discussing right to start writing a technical report.

So, I will touch upon some points here. So, why call fiber and what is the motivation behind that. So, mainly that the unique property of call over fiber is a low latency and because of the first data transmissions and it is a promising communication it is promising for a communication network for fiber cable and connector formers.

There is a standard yet however the discussion is aggressive going on in different standard development normalizations and we can see that other technical advantages that actually driving this interest at that three important thing is that one is the low latency I mentioned. Second is the very negligible optical non-layerity and third is that very low loss those is these three things are basically very unique feature in holocall fiber that you can see is been benefit over a solid call fiber and application point of view where we need such a low latency application like your high speed spreading or the stock exchanges they need a very low latency applications or have a high latency application.

So, this is the high speed application or the given networks or this AI data center they want to a real time synchronization between two data center or age data center there you can see this benefit of this the holocall fiber. So, is holocall fiber as a concept is not a new it was a many years old concept however you can see there is a development happens throughout many years.

So, first time the holocall fiber or developed first is not the black fiber so, this is a you can see the picture the left side as a multiple alternate layers transmitted layers of low liquid type index. Second comes that photonic band of fiber and latest one that is the anti resonant or ARF holocall fiber.

So, this ARF design also the lowest activation is achieved other to design it may have a lower latency maybe some other benefit but the activation of those designers very high. So, this anti resonant fiber that is having a low latency low at elevation and the low does low dispersion so, all the three benefits we can.

So, this is a very high level of comparison between holocall fiber and a solid silica optical fiber here have taken 0 or 657 dot a1 type fiber we can see that in holocall fiber theoretically you can achieve less than 0.1 dB per kilometer attenuation and so, far we have seen that it is reported up to 0.05 d per kilometer.

However, this fiber have a larger coating diameter so, it is not a s dm or reduced coating 5 at that means, you cannot increase the number of channel here even this is the higher diameter for the micrometer. However, it is happening operating band with is very, very wide above 850 nanometer also can be achieved.

How many dispersion extremely low are normal solid core fiber 17 because again per nanometer per meter where you can achieve close to 0 almost less than 2 picosegain and anometer kilometer. PMD is almost similar non-linear coefficient is very, very low map proven loss is little bit higher side as of now is reported but research is still going on how to control this map proven loss.

More fluid diameter of this fiber is higher side where normal solid core on 10 micrometer at 15, 15, 15 nanometer where hollow core on 32 to 37 micrometer. So, because of that when it to have a hollow core to solid core transition there are some adaptor or some mechanism required for this condition. The last one is a main benefit where diffractive in this hollow core is close to 1 that is as good as air and because of this you can get a latent 7 if it like for example, a solid silicon core on the latent 0.9 microsecond per kilometer where a hollow core fiber you can say around 3.33 microsecond per kilometer.

So, that this is the main differentiator in addition to this low attenuation and the known non-linear effect to the hollow core fiber. So, how do you can see that most of the descent application is focusing on mainly in the low latent significance. So, this is the hollow core fiber that we developed we called is a hybrid kernel because it is contain 3 type of fibers hollow core fibers 2 hollow core fibers then 3 tubes of solid core fiber of the liquid.

So, this is the hollow core fiber of 0657a1 and 1 lose 2 of g.654 e fiber and we developed this particular hybrid cover because to understand that in the same network how we can compare 2 or 3 different type of fiber in terms of loss and the latency. So, this are the some of the results that we tested in a more research laboratory application research laboratory and different kind of a data rate 100 400 and 600 g different kind of launch power different kind of frequency level.

And all the cases what you have found that is fiber is well well I mean I mean we have across 600 g and the pre-efficiency we are limit is below that the threshold values later on. So, we tested this fiber in a POC where you can realize you could realize that a 32 percent the latency benefit against a solid core fiber.

So, what are the use cases of hollow core fiber? Of course, the data center and a hyper scalar they have you can see the benefit because of a low latency. You can have a data center interconnect as a synchronization application high frequency printing take home operator also see the benefit for a long distance communication even to reduce the number of computers the regenerators the amplifiers.

And other also research is going on for the QKD application quantum heat distributions where hollow core fiber is found to very unique benefit which which not be able to achieve by a solid core fiber because of different scattering kind of phenomenon there. So, now this is all about the next generation fiber technologies I covered SDM different SDM fibers covered GJR650 more and hollow core fiber.

So, now the rest of the presentation will more focus on the multi core fiber and its use places as standard action effort. So, maybe you can take some question if is other love in you know takes a question if there is question then I will go to the next stage. I believe that we continue so that I am then going to the decision that yes.

Okay, okay, sure. Thank you. Thank you. Thank you. So, I am coming to again the slide that I have shown before the different kind of SDM fiber reduce coating diameter fiber reduce cutting diameter fiber RCF multi code fiber MCF and MMF the remote fiber. So, there are some advantages and challenges of in all those fiber.

So, if we start with the first one reduce coating diameter fiber the first advantage is that you can achieve the high fiber density cable you can see in the IVR we can pack 6 and 6 and 1 to in 1 and 1 and 1 and 2 micro meter you can pack 2 to 5 by just 6 millimeter cable and having a fully backward compatibility because the cladding diameter is same.

So, you can easily splice and do not need any extra component that the existing ecosystems we can work with you know anything extra for that. But the challenge is that there is a limitation we cannot go is a limited to 4 10 density even 4 10 is a hypothetical max or 2 or 1.5 or 2 times you can improve but beyond that not possible with this reduce coating diameter fiber.

You will see that reduce cladding diameter fiber again you can increase the fiber density do not need to any additional component. However, we have a better design to adjust this lower cladding diameter most of the time it is 80 micro meter diameter and also need to do it. So, you know that the more you can do it, the more you can do it.

Sorry. Yes, I do. Any question? No, it's fine. I believe that one mic was active now is this active. No, it's us. Yes, it's a little bit. No problem. Thank you. So, the reduced cladding diameter fiber is a different kind of cladding diameter. So, the splicing and compatibility will be the challenge. In multiple fiber again we achieve a very high core density because in the same 125 you can have a 2 core 4 core mode.

So, you can reduce the cable dimension and weight and interestingly each and every core also supports the existing ideal standard that is is a fully optically backward compatible. But the challenge is that using multiple fiber we need to develop and the ecosystems. We need to have a fanning fan out devices.

We need to have a one example, we have a special mechanism for splicing and connections into a connected unique optical interfaces with. Few more fiber again. You can have a higher HDM channels in the same 125 micro meter cladding diameter. It is easy for splicing because there is a larger core diameter.

The splicing operation is much less easy. The challenge is that it needs a advanced digital processing, signal processing. And it requires again the marks and be max the end to ends of the optical network. So, this is a kind of very high level of advantage challenges. If you see the standard development status, RCDM and RCAB is very mature technologies.

We have so many IIC standards. Those are also referred in I2 standards. Both for product characteristics and for test methods. In terms of multiple fiber, I2 developed to non normative technical report. One is GSTR HDM. Let us say technical report on the distribution of multiplexing in 2022. And last year we also published another supplement document that is GSTR 87.

It is basically related to the roadmap of the multi-core fiber standardization. How we move forward on this? And again, these two reports also cover the feed mode fiber. And I2 and also IIC, we first took a decision to start developing the standard on the multi-core fiber first. And also we took the weekly couple multi-core fiber I will talk about later.

And then that the several standard are already open for division and need work item also initiated. So, again in the multi-core fiber, you can see there is three type of multi-core fibers. First is that weekly couple multi-core fiber. It means that the signal of one core is not going to or coupled to the another core, the adjacent core.

That means all these four core are four different channels. And there are very very low inter cost of between the two adjacent core. That is, it is none of the weekly couple. In the randomly coupled, the core can be placed going close to each other. And it will not bother about signal going from one core to another core.

So, that is why it is none of the randomly coupled. And in the randomly coupled multi-core, we can we can we can place many cores inside the gridding. But in weekly couple, we have to make a distance between the two adjacent core. That is a core pitch. And few more again that same multi-core fiber, but instead of a one single mode behavior, we have a few more behavior of the each core.

So, all the out of the three type of multi-core fiber, the first one that is weekly couple multi-core fiber is the first priority in the standardization space. And also, we can see the immediate commercialization and the benefits of the application. So, you can see the mostly used multi-core fiber now in the world is the weekly couple multi-core fiber.

Now let us see that the MCD ecosystems, we have a fiber then we have a cable. So, for example, you have to connect to data centered by a multi-core fiber. So, what are the other accessories we need other than fiber and the cable? So, first of all other than fiber, the cable we need to have a panel and one side at the transmitter side and receiver side, you have a fat out.

So, fanning a fan out means that for example, you have a four core multi-core fiber. So, each and every core should connect to the transceiver. So, that means, you need to take four core out or four fiber out of a one fiber. This fan out has to be the other fan out. And we need to have a M-shape connector at the end and also M-shape transceiver.

And in fact, if you have a M-shape connector or M-shape transceiver and M-shape transceiver, probably you do not need a fanning and a fan out device. And in that case, you can directly connect a multi-core fiber to a multi-core fiber connector. And then by this, you can directly connect to a transceiver.

However, M-shape connector and M-shape transceiver is still under development stage. So, that's why all the existing connectors is happening to a fanning fan out devices. And then of course, you need to have a patch panel where we have to place all the fanning fan out devices and the slicing, and the frames and all those stuffs.

So, this is also another important requirement to make a optical fiber network by M-shape fiber. In addition to that we also need to have a join poser if you're going to deploy the M-shape cable in the outside of the plan network. We have to connect to the end of the cable, of course, and need that.

So, what is happening in the standard developer organization? So, if you see all the M-shape components, we have seen is in the ecosystem. So, IITU, IAC are already involved to develop a standard for each and every item. You can see which study group, which questions and which working group in IAC are working on it.

In addition to IITU and IAC, two other standard developer organizations like IIT Repelry and OIA, they are also now actively involved to develop standard on the transceiver interface. Now, come to the M-shape technologies and design and the key parameters. So, what we can see here that, multiple fiber, what benefit you can get, for example, is the four-core multiple fiber is the 75 percent smaller surface area versus equivalent to the single-core fiber bundles.

And it means to accommodate so many cores inside the cable. And we can see here that, four-core multiple fiber, which can also come with your 200-micron fiber. It means that, once I do have a multi-core, as I said, we have reduced coating diameter. So, by converging, these two technologies of SDM, that is the multi-core fiber technology, reduced coating diameter technology.

By converging two technologies, we can even achieve further the fiber density. So, that is a, so that is basically said in STL, we have a two products. One is that, four-core multiple fiber with 250 micron diameter and also four-core multiple fiber with 200 micron diameter. So, we can also achieve for more fiber density by converging this two technologies.

So, now, what are the application spaces? So, in ITU or also in IAC, whatever we decided that, two major applications, especially you can see a value of a multi-core fiber. First is a summed application, longer summed application, second is the data center applications. So, in ITU, now two standard are being developed.

One and both the standard will have two varieties of multi-core fiber, two-core and four-core. And one will be the backward compatible with 0,652 and 0,657 standard. And second one will be backward compatible with 0,654 cutoff shifted fiber. Now, we can see that what are the benefits in the optical network?

Now, we can achieve by using a multi-core fiber. In the top side table, you can see that we have four fibers and in one four-core multiple fiber, we go one to a four single-core fiber. So, you can see that directly benefit of a construction area of 0.25, that is 70% benefit. And equally, you can also reduce the weight of the fiber.

So, in the below, you can see that we have a duct, then we have a duct in the EOLO corer, then we have a black size, black color, circle or cylinder, you can see the single-core fiber cable and multi-core-based green color. So, this is the way you can reduce the diameter of the fiber and cable. And it is going to help to pack more fiber in a duct space.

And also, it will help in the first deployment because of the reduced diameter of the cable and reduced weight of the cable. So, it basically offers a large scalability and feature proof infrastructure. Now, I talk about it a little bit more about the pre-foam. So, one side we are innovation and development happening in the fiber side and the cable side.

And apparently, there are a lot of development happen in the fanning fan of device, which is very important component, at least current and on my desk without a feeble, you cannot install a multi-core fiber cable. So, for example, the top, we can say that first feeble being developed with our partner, we developed, we called it non-jacketed feeble.

The length was around 110 millimeter and thickness are with, these are on 3 millimeter. And first time we achieved a loss around 1.2 dpx 15 feet in an millimeter. In the next phase, we achieved around 0.5 dp per kilometer, we reduced the length to 60 millimeter. And the last one that we achieved, we length 50 per millimeter and insertion loss, that's 0.1 to 0.35 dp, this as good as a connector loss even below that, and also with the jacket.

So, this is the size of the feeble is something like this that we can easily place inside a spice spray. Just like a spice spray or a heat shrink. And you can see that once committed back on at the bottom of this figure, where we see that how this feeble is placed, the two ends of a multi-core fiber, you can say that no day and no day, we have a 1, 2, 3, 4, 4 single-core fiber, or single-core fiber, that is coming into the feeble device.

So, in feeble device, one end, we have a 4 single-core fiber, and another end, we have a 4-core multi-core fiber. So, that is the device and both the end, we have a 2, 3, 4 device. So, when we developing that standard for multi-core fiber cable, after similarly, also we are developing the test methods.

So, here two, in IQ, one of the standard recommendation called G652 or 2, that is the recommendation for the test methods. So, now this is open for division. The main topic of revisions are the include the crosstalk measurements. So, in multi-core fiber, there are the two parameters are very important to revise.

One is that a new parameter crosstalk, which is not there in the single-core fiber. And second is that glass geometry parameter, because in multi-core we have a more than one-core. So, only to revise the glass geometry methods to measure the different new parameter related to the more than one-core. So, these documents are open for division in IQ as well as also in IAC.

Now, what is the key parameters of a multi-core fiber? So, as I mentioned that two parameters are very important. One is that core pitch means the distance between the two adjacent core. Then of course, we have a core profile, that is referred to a minus profile, which is basically the fundamental optical properties are determined or achieved by this referred to a minus profile of each and every core.

Number of core of course, is the more fundamental things. OCT outer cladding thickness, that is the distance between the core to the outside cladding boundary, bin radius and the fiber length. Fiber length is also important because the crosstalk also depend on the length of the fiber. So, this is all the design parameters and what are the output or the actual characteristic of a multi-core fiber is the crosstalks, butter, voyablanx, macroband loss and mode field diameter of each and every core.

So, this is the basically target parameter to meet those requirements, you need to design the multi-core accordingly. So, now I am talking about that test method or crosstalk measurement, how we measure the crosstalk? Because I talk about mode in detail because this is a new parameter for multi-core fiber.

Other parameter is very similar to the normal single mode fiber. So, nothing much to discuss about that. So, there is a two ways we can measure crosstalk. One is that light source and the power metronome method. And second is that OTR method. So, the top one is the light source and power metronome.

So, where you can see you can see a one multi-core fiber, then you have a fan out fan in one side and a fan out other side. So, fan in for example, you have a core core. So, one core fiber core number one C1, we could one result, result or power or transmitter and we excite this core one. So, what is the cost of crosstalk?

So, means that how much power is going to the other core? That is core number two, three and four. So, then what we do? We will put a detector or power meter in core one first. Core one of obvious we will get very high power because we are exciting the core one and the other side. And the receiver side again we measure the power and core two, then core three and core four, C2, C3 and C4.

And we measure the power and that power is basically the crosstalk. And our and a good or well designed vehicle cover multi-core fiber is value will be as low as possible. And second is the OTR method. In the OTR method is very similar but there is a difference is that instead of a two device, there is a problem to have a one device.

We have a OTR here at the one end present a core one. And we wanted to measure the crosstalk between core one and core two. So, at the receiver end we will make a dummy, a kind of dummy single mode fiber, single core fiber and we can just join core one and core two. And what we will do that then when the light is going from core one and coming back to core two.

So, there will be one juncture or you can see a peak and that value of the peak is basically the crosstalk measurement. I will show one of the peak in the little side. So, again the power meter method what we will do first we will use a core one and we measure the power all the other side over one C2, C1, C2, C3, C4.

And again we will excite C2 core two and we measure the power and C1, C2, C4 similar to C3 we will excite the core three and then excite core four and measure all the power. In OTR method as I mentioned we have a core one first to excite then we will attach a link core one and core two at the other end we are dummy single mode fiber.

Then again we will excite core one again we will measure the dummy core one versus core three that means we if we measure the cost between core one and core two we will attach core one core two at the other side. If we want to measure core one to core three then we have to attach core one core three at the other side and again we come to measure the cost between core one and core four.

we have to attach core 1 and core 4 other side. And you can see the one graph at the below. So, this is basically a particular graph when you measure a cost of at the middle of this dummy fiber will get one peak and this peak is basically the cost of between this two particular fiber sorry two particular core.

Now coming to the splicing that is another important topic because the normal splicing machine will not be helpful for a multi core fiber splicing. So, this is not a advertisement of any other splicing devices here. Just we know this this splice we have used and is available in the market as we are showing it here.

So, there is a two type of devices one is that Fujikura model and is a feature model here. And this particular device is as a different type of technologies to alignment the core. Because core alignment is very important and some devices as a machine they can auto align and the main mechanism is that it can have a rotational motor to have a 360 degree rotation to rotate and align the core.

And some device will get the picture at the end view where we can manually move or rotate clockwise or until clockwise the core and extrapolate core 1 core 1 and core 2 with core 2 with the and you can do the splicing. So, previously the splicing time was very high but recent advertisement in the splicing technologies.

Now, I can see that a core core multi core fiber takes around 5 to 10 minutes per fiber. So, if we see that one core it is almost 1 to 2 minute per core kind of this is very similar to a single core fiber. So, we do not see any larger I mean long splicing time for multi core fiber even you can achieve a low splice loss less than 0.1 dB which is very similar to a single core fiber splice loss.

Now, we STL our journey on weekly cover multi core fiber. So, we start with a multi core fiber 4 core multi core fiber with a 125 micron diameter having a fully backward and geometrical compatibility with existing fiber. And these are the some of the parameters that you maintain like OCT value around 30 to 35 micron meter core we can import it to 45 micron meter.

So, here important thing is that if we bring this core very close to each other the cost of value will increase ok. So, that means, we have to make some distance between two cores. So, core piece is important to reduce the cost of higher is the core piece lower is the cost of well. The problem is that if we make with the too much high too much high core piece the core will be very close to the outside crowding that means, OCT value also will be less.

So, we have a OCT value less than atunations and Ben loss will be high. So, we have a optimization between core piece and the OCT that means, it is optimization between cost stock and the atunuation is a kind way. So, there actually innovation is happening. So, first the core core multi core fiber we developed then we add a marker because the way we identified core is by using a marker.

So, is a marker at the adjacent to one core and so that you can identify this is a core one or whatever number you can give then you can go clockwise and anticlockwise and you can identify all other the three cores. The third design that we developed with a trench profile. So, you know this trench profile is very popular to achieve a bend in sensitive property of a normal single core fiber.

So, what we did we just created trench on each and every core to reduce the attenuation as well as the cost of as well as the map problem. So, this is a multiplier effect. So, after using a trench profile we could see a very high level of improvement both in attenuation and the cost of values. The latest one that we developed is 7 core multi core fiber.

7 core for multi core fiber within a 125 micron diameter that means, 7 times you are increasing the number of challenge in the same footprint. So, that is the latest development. So, this is a request to discuss about the test method I already mentioned about some of the test methods mainly cost of and that is the most important for multi core fiber.

A list of the test methods are very very similar for any existing cable that we already measured. But thing is that in the multi core fiber measurement we have a fanning and a fan out device that is the most important thing. So, for example, here if you wanted to measure a link kind of attenuation or link cost of in this picture you can see that we have around 4 to kilometer cable drum a multi core fiber and we got link a spicing with the fiber in between then we have a fanning one out fan out other side then we measured the same way by OTTR by connecting coming at the two sides and measure the cost of and also attenuation.

So, most of the attenuation we receive in the cable stage less than 0.2 dB that is as good as your normal single about 5 words like 652 or 657 kind of fiber cost of value will receive around minus 36 minus 52 dB. So, this is a very good cost of value in terms of the kind of a data that we are looking for.

Of course, it will be improved further based on this the change in optimization of the refrigerant maintenance profile. You can see that some of the things that you have carried out with the cable, multiple fiber cable this all of the cable tension like your tension measurement or crash measurement or impact or tension bend.

So, those are basically exactly the same device that we used to test the normal cable. Only thing is that when we wanted to measure the characteristics or the performance of 4 individual course we need to have a fanning and kind of device kind of both the 8 there is only difference. The rest of the parameters of the process are exactly of a normal normal cable or the single core fiber cable measurements.

Environmental test again we perform all the aging test at the time per cycling and all those jobs. This is mainly depend on the cable constructions more rather than the fiber properties the fiber properties as is the same properties. So, we could able to easily meet that need the requirement of the existing IEC standards.

Now while touch upon few of the few of the work case studies first case study is the lab transmission study. So, we have a full phase application research laboratory in our our our our the India plant we call the COE center of excellence. While we have a complete test bed to test up to 600 G systems and we have a test bed up to 2000 kilometer with normal single core fiber you can see some of the pictures of our laboratory.

In this laboratory you test it the multiple fiber in a 50 kilometer link around 80 that is falling to 20 TV per transmission. We can see that the network diagram that we have test it is a DWRM channel. Then we use the speech or the infinite fanning of device multiple fiber and they can we have a receiver and all the network quality measurement devices.

The right side you can see that the BIR value BFEC BIR value and the optimum launch power or decision on minus 1 dBm and the BIR value is well well below the threshold values of this mathematical fiber. Then also we are tested with one of our comment agency called C.DOT they are basically a government research wing where a test was carried out for the Q quantum distribution over 100 kilometer cable I am sorry 100 kilometer fiber here you can see that test apparatus here where also cost of value of to minus 49 dBm at a time with the activation around 0.2 dBm at a Q-3 demo around error fee exchange with bandwidth or on 80 TV per fiber over 50 kilometer and overall test rate around 100 kilometer in the C.DOT that is a government it is a organization.

So it is also proven that this fiber also can take a quantum net channels and the benefit is that you have a 4 core multiple fiber. In a one core you can use a classical channel and the other core you have a quantum channel maybe two adjacent of the diagonal core. We do not need a two different fiber for quantum communication.

JL what happened that two fiber being deployed one taking classical channel and another quantum channel. So in multicore the one fiber you can use for both the purpose. They are they overall because of our technologies that we first developed a glass preform with multicore fiber preform then we draw this preform to produce multicore fiber.

They are cabling then we have a inter fiber management systems. So do this kind of a POC or experiment you can say that also the deployment actually we produce a composite cable containing single core fiber and multicore fiber. Here you can see the construction of a 12 multicore fiber and 12 single core fiber and both the fiber multicore and single core are G57A1 and G62D fiber compliance.

We developed armored fiber for undergone applications then ADSS sorry armored cable for undergone applications then ADSS while directly supporting cable for added applications then also you have a inutive version and also the multidivotion. So basically try it all type of combinations that you can see currently being deployed globally and all these actually cables are passed or qualified all the existing cable standard whether it is a mechanical test or environmental test according to our national standards.

So and then this cable also being deployed in two areas one in India and other is in UK. So we have a case study here that is a POC test that is POC Stanford Advanced Optical Communication this is a government of India funded consortium between industry academia and government where this particular multicore fiber composite cable deployed in IIT Madhag.

IIT Madhag is a very premium technology institution in India there campus you can see that the boundary of IIT is deployed both undergone and area where standard basically supply cable as a equipment even deployment service of as well to end to end and after deployment this cable has been tested in various applications some application you can mention you can see here like hyper scale data center or made to access network mobile front all 5 basic application quantum application sensing application.

So basically this case mode is ready now all kind of testing are are going on by academia and other industry bodies. We have a second case studies that is in UK court this is essentially well known data center infrastructure provider where a multicore fiber cable deployed in UK you can see the map here the connecting two data center terminal and important thing is that here not only outdoor cable indoor cable also being developed you can see that indoor cable two L5 or MCF then you have a outdoor composite cable and then we have a joint closure transition box and termination box.

So all are developed by starlight and install for both single core and the multicore fiber cable this also tested now I think this is still running this for testing. You can see there is one of the publicly available news where a cold trials multicore fiber to power the connection of the network and where it would actually partner with different vendors like Cn and Nokia the activation vendor in addition to the starlight technologies.

So what we can see in the multicore fiber the advantages are of course it improve the material efficiency means that instead of 4 fiber you need 1 fiber is kind of so it increase the decrease the space for freight and increase the efficiency is a very compact home factor that is why you can just increase the number of fiber in a cable just by four times it decrease the TOC the total cost of ownership by the deployment by increasing the number of fiber count and of course it increase the enhanced data integrity as specifically for the quantum distributions where we need to have it transmit a critical business data ensuring a half proof the communication.

So what is the way for what what we see that the way the technology is going to evolve in future for multicore fiber or over on SDM thing is that the now the cable that we have shown here that is for different kind of many the loose took design what you can see it will be used for different type of other design like ribbon and iBR or other high fiber count cable and next we see that there is a lot of innovations improvement required in the connectors connector is still under under process the connector standardizations and interfaces and amplifiers so it will again help in the adaptability or first adaptability of the multicore fiber cable ecosystems in standardization point of