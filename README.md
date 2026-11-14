🌐 EchoVoyageStreet x TravelBuddy — Ton monde, résonnant de souvenirs
- usual actions
- publier des photos d'un vyage
- unusual actions : 
EchoVoyage x TravelBuddy est une plateforme immersive qui transforme chaque ville en expérience vivante, chaque voyage en quête sensorielle, et chaque retour chez soi en redécouverte intime. C’est une invitation à explorer le monde à travers les sons, les paysages, les émotions et les récits — et à faire de ta propre ville un miroir vibrant de tes aventures passées.
🧠 Vision du projet

    Revenir chez soi, c’est redécouvrir sa ville à travers les sons, les odeurs, les émotions du voyage. Chaque rue devient une mélodie. Chaque boutique, un musée de souvenirs sensoriels. Mais avant de partir, tu dois créer. Une application, un poème, un jeu, une chanson — quelque chose qui te servira de boussole intérieure.

🔁 Cycle d’expérience

    Tu crées : avant le départ, tu fabriques une œuvre, un outil, une capsule personnelle

    Tu voyages : tu enregistres des sons, des ambiances, des émotions

    Tu explores : tu vis des quêtes, tu découvres des paysages et des lieux secrets

    Tu reviens : ta ville devient un miroir de ce que tu as vécu ailleurs

    Tu revisites : les lieux familiers résonnent de souvenirs lointains

    Tu repars : enrichi, prêt pour une nouvelle aventure

📱 Fonctionnalités clés
Fonction	Description
🧳 Carnet de voyage sonore	Chaque destination génère une capsule sensorielle (sons, photos, émotions)
🎧 Rue musicale	L’app joue des sons liés à tes voyages pendant tes balades locales
🏪 Souvenir vivant	Les magasins deviennent des points de mémoire sensorielle
💎 Ruby GPS émotionnel	Te guide dans ta ville selon ton mood, l’heure, et tes souvenirs
🚀 Prêt au départ	Avant de partir, tu crées quelque chose de nouveau
🧱 Limite de carte	Zones floues où la réalité se dissout et l’imaginaire prend le relais
🧱 Limite de Map — Le bord du connu

    “C’est là où la ville s’arrête… ou commence à rêver.”

La limite de carte devient :

    Un déclencheur sensoriel : sons, odeurs, souvenirs se mélangent

    Une zone floue : les repères se dissolvent, l’imaginaire prend le relais

    Un défi personnel : pour bouger, tu dois créer quelque chose

    Un événement JavaScript : déclenche des effets visuels et sonores à l’approche

🎛 Exemple d’événement JavaScript
javascript
document.addEventListener('mapLimitReached', () => {
  playInstrumentSound(userProfile.instrument);
  showMemoryOverlay();
  triggerLimitMoodText();
});

    playInstrumentSound() : joue le son associé à l’instrument du voyageur (ex. synthé rétro, tambour tribal)

    showMemoryOverlay() : affiche une couche visuelle avec photos et souvenirs

    triggerLimitMoodText() : affiche un texte introspectif depuis limit_mood.md

🎼 Instrument du voyageur

Chaque profil contient un instrument de voyage :
yaml
instrument: "violon rêveur"

Cet instrument :

    Influence les sons joués à l’approche des limites

    Modifie l’ambiance musicale des playlists

    Peut être utilisé comme déclencheur narratif dans les quêtes

📁 Structure du dépôt

EchoVoyage/
│
├── profiles/                    # Profils personnalisés (.yaml/.json)
├── cities/                      # Dossiers par ville avec photos, playlists, quêtes
├── envyage/                     # Milieux naturels et ambiances sonores
├── quests/                      # Quêtes interactives et récits immersifs
├── playlists/                   # Génération dynamique via API musicale
├── gallery/                     # Galerie de cartes postales sonores
├── map/                         # Carte du monde interactive
├── memories/                    # Carnet de voyage collaboratif
├── map_limits/                  # Zones de bascule et déclencheurs
│   ├── villeurbanne_limit.json
│   ├── limit_sounds/
│   ├── limit_mood.md
│   ├── limit_trigger.py
│   └── creations_before_departure/
└── README.md

🧱 Limite de Map — Le bord du connu

    “C’est là où la ville s’arrête… ou commence à rêver.”

La limite de carte n’est pas qu’un bord géographique. C’est aussi :

    Ce qui te limite : fatigue, peur, manque de temps, d’argent, d’élan

    Ce qui t’appelle : curiosité, mémoire, désir de créer, besoin de partir

    Ce que tu dois franchir : pas physiquement, mais intérieurement

🎮 Fonction narrative

La limite devient :

    Un point de bascule entre réalité et mémoire

    Un déclencheur sensoriel : sons, odeurs, souvenirs se mélangent

    Une zone floue : les repères se dissolvent, l’imaginaire prend le relais

    Un défi personnel : pour bouger, tu dois créer quelque chose

✨ Avant de partir, tu dois créer

    Le voyage ne commence pas par un billet, mais par une impulsion créative.

Avant de franchir la limite, tu dois :

    🎨 Créer une œuvre : un poème, une chanson, une image, un jeu

    🛠️ Fabriquer un outil : une mini-app, un carnet, un talisman numérique

    🎭 Inventer un rôle : ton alter ego voyageur, ton mood, ton instrument

    📜 Écrire une intention : pourquoi tu pars, ce que tu cherches, ce que tu veux laisser derrière

Cette création devient ta clé de passage. Elle est enregistrée dans ton profil, elle influence ton aventure, et elle résonne à ton retour.

🌿  Explorer — Milieux naturels et immersion sensorielle

Chaque boutique contient des souvenirs d'une destination (environnement + voyage) avec :

    🏞️ Milieux naturels : forêts, plages, montagnes, parcs urbains, avec photos et sons ambiants

    🎧 Ambiances sonores : bruits de la ville, chants d’oiseaux, vagues, musiques locales

    🧘 Mood sensoriel : selon l’heure du jour ou ton état (matin calme, nuit vibrante, retour nostalgique)

💎 Ruby de la ville — Ton GPS émotionnel

Quand tu reviens dans ta ville, tu débloques ton Ruby, une sorte de talisman numérique qui :

    📍 Connaît les lieux qui te parlent (cafés, ruelles, bancs secrets, musées préférés)

    🌙 S’adapte à l’heure : suggestions nocturnes ou diurnes selon ton rythme

    🎶 Te joue une musique qui te reconnecte à ton “toi local”

    🧠 Se souvient de tes trajets, tes humeurs, tes découvertes

    Le Ruby est comme une mémoire vivante de ta ville. Il évolue avec toi.

🔁 Cycle du voyage
