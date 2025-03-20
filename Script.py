import socket
import math

# Adresse et port du serveur
server_address = ('challenge01.root-me.org', 52002)

# Création de la socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    client_socket.connect(server_address)
    print("Connecté au serveur")

    # Réception de la réponse
    response = client_socket.recv(1024)
    print("Réponse du serveur:", response.decode())

    valeur_extraite = int(response.decode().split()[27])
    valeur_extraite2 = int(response.decode().split()[31])

    print(valeur_extraite)
    print(valeur_extraite2)

    squareRoot = math.sqrt(valeur_extraite)

    finalResult = squareRoot * valeur_extraite2

    print(finalResult)

    resultArrondi = round(finalResult, 2)

    print(resultArrondi)

    #resultArrondiStr = str(resultArrondi).encode()

    reponse = f"{resultArrondi}\n"

    client_socket.sendall(str(reponse).encode())

    finalResponse = client_socket.recv(1024).decode()
    print("Réponse du serveur:", finalResponse)

    

finally:
    # Fermeture de la connexion
    client_socket.close()
