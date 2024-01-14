import requests
import socket
import os
from pydub import AudioSegment
from model import load_data, load_model, dump_model, predict_emotion

### SOCKET PART
SOCKET_HOST = '127.0.0.1'  # Adresse IP locale
SOCKET_PORT = 65432         # Port d'écoute

### MODEL PART
MODEL_FOLDER = "emoticall.cnn"
RAVDESS_FOLDER = "assets/data_samples/RAVDESS"
EXCLUDED_FILES = ["README.md","03-01-06-01-01-02-20.wav", "03-01-08-01-02-02-01.wav", "03-01-03-01-02-01-20.wav"]

emotions = {
    '01': "neutral", 
    '02': "calm", 
    '03': "happy", 
    '04': "sad", 
    '05': "angry", 
    '06': "fearful", 
    '07': "disgust", 
    '08': "surprised"
}

def send_results(prediction):
    URL = "http://127.0.0.1:3002/emotion"
    emotion = {"emotion": prediction}

    r = requests.post(url=URL, data=emotion)

    print(r.status_code, r.text)

def convert_stereo_to_mono(input_file):
    # Charger le fichier audio stéréo
    sound = AudioSegment.from_file(input_file)

    # Convertir en mono (moyenne des canaux gauche et droit)
    mono_sound = sound.set_channels(1)

    # Enregistrer le fichier audio mono
    mono_sound.export(input_file, format="wav")

### MODEL ###

print("Looking for model ...")
if not os.path.exists(MODEL_FOLDER):
    print("No model found, training one")

    x,y = load_data(RAVDESS_FOLDER, emotions=emotions, excluded_files=EXCLUDED_FILES)
    dump_model("emoticall.cnn",x,y)

    print("Model dumped !")

print("Model found")
cnn_model = load_model(MODEL_FOLDER)
print("Model loaded")


### SOCKET ###
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.bind((SOCKET_HOST,SOCKET_PORT)) 

s.listen()

print(f"Serveur en attente de connexions sur {SOCKET_HOST}:{SOCKET_PORT}")

while True:
    # Attendre une connexion
    client_socket, client_address = s.accept()
    print(f"Connexion acceptée de {client_address}")

    # Boucle de réception de données
    while True:
        # Recevoir des données du client
        data = client_socket.recv(1024)

        # Vérifier si la connexion est fermée
        if not data:
            print(f"Connexion fermée par {client_address}")
            break

        # Traiter les données reçues (exemple: affichage)
        print(f"Reçu de {client_address}: {data.decode('utf-8')}")
        file = data.decode('utf-8').replace("\n","")
        convert_stereo_to_mono(file)
        emotion = predict_emotion(cnn_model,file)[0]
        print(emotion)
        send_results(emotion)

    # Fermer le socket du client
    client_socket.close()