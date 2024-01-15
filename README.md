# Détection d'émotions dasn la voix
Ce projet a été réalisé dans le cadre du cours d'Interaction Homme-Machines Evoluées (IHME), dispensé à l'INSA Rouen Normandie, par DOUET Marie, GRINDEL Brice, MARTIN Lucas et SOUVANNAVONG Elise. 

Il se base notamment sur les synthèses bibliographiques suivantes :
- Reconnaissance d’émotions dans la voix, IMBERT Alexis et MARTIN Lucas, 21 novembre 2023
- Détection et synthèse (visuelle et sonore) d’émotions, LUYPAERT Pierre et SOUVANNAVONG Elise, 21 novembre 2023

## Manuel d'installation

1. Cloner le projet
2. Télécharger l'archive de ressources
3. Inscrire le token Discord du bot dans `src/bot/config.json`
4. Mettre le fichier JDA de l'archive ressource dans `jda/`
5. Mettre le contenu du dossier `data_samples` de l'archive ressource dans `assets/`
6. Dans un premier terminal, exécutez les commandes suivantes depuis la racine du projet :
```bash
javac src/bot/*.java -sourcepath src -classpath jda/JDA-5.0.0-beta.15-withDependencies.jar -d class
java -classpath class:jda/JDA-5.0.0-beta.15-withDependencies.jar bot.Main
```
7. Dans un second, exécutez ces commandes :
```bash
cd src/web-server
npm i
cd interface-web
npm i
npm run build
cd ..
npm start
```

8. Enfin, dans un troisième et dernier terminal, faîtes depuis la racine du projet :
```bash
python3 src/main.py
```

9. Connectez vous à un channel vocal de votre serveur Discord, sur lequel est invité le bot. Tapez `/join` dans un cannal de texte et commencez à parler.

10. Profitez de la reconnaissance à l'adresse indiquée par le bot ou sur `localhost:3002`

## Manuel utilisateur

```bash

```

## Rapport
### Introduction
<!-- Expliquer comment le problème est attaqué (boîte noire, temps réel, extraits de voix court, ...)-->

### Spécifications
<!-- Repréciser les specs (<1s de délai, 70% de précision, 60% seuil critique) -->

### Conception
<!-- Mettre un schéma de la pipeline avec les in/out -->

### Implémentation
<!-- Expliquer l'implémentation, ce qui a été retenu, pq, comment ça marche, comment les différents parties communiquent entre elles, interfaces, sources des données, ... -->

## Vidéo de démonstration

Une vidéo de démonstration est disponible [ici]()