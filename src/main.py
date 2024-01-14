import requests
import socket
import model

SOCKET_HOST = '127.0.0.1'  # Adresse IP locale
SOCKET_PORT = 65432         # Port d'écoute

def apply_model(path_to_file: str):
    pass

def send_results(prediction):
    URL = "http://127.0.0.1:3002/emotion"
    emotion = {"emotion": prediction}

    r = requests.post(url=URL, data=emotion)

    print(r.status_code, r.text)


""" voice_extract = get_voice_extract()
prediction = apply_model(voice_extract) """
#get_voice_extract()
#send_results(prediction)

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
        apply_model(data)

    # Fermer le socket du client
    client_socket.close()
