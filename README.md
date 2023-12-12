# emotion_detection
The goal is to detect emotion in a vocal flux from Discord and to display the detected emotion. 

## Dataset pris pour le benchmark 

Savee : https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee --> big 6 plus neutre

RAVDESS Emotional speech audio : https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio --> big 6 plus neutre 

EmoReact : demandé

IEMOCAP : https://www.kaggle.com/datasets/samuelsamsudinng/iemocap-emotion-speech-database

EmoDB : on ne prend pas car ce sont pas les bonnes émotions

Emovo : https://dagshub.com/kingabzpro/EMOVO --> big 6 plus neutre

## features qu'on extract 
F0 mean,  F0 range, Tempo, Voice Quality et loudness. La voice quality se base sur la qualité de l'articulation et si il y a du bruit dans la voix (comme des tremblements) 

prendre en compte le genre ? comment on fait ? idée : faire deux modèle
si on choisit un dataset avec des émotions qu'on a pas choisit on fait quoi comment ? other ? on les supprime ? 
