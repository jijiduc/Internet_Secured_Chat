"""""
Contient les fonctions d'encodages et décodages du protocole du server
"""""
def encode() : # pour l'instant on envoie du texte par défaut
    message = "petit pain d'épices" #input('Your message :\n')
    header = b'ISCt'
    size = len(message.encode()).to_bytes(2,"big")
    data = bytearray()
    data.extend(header)
    data.extend(size)
    for i in message :
        data.extend(bytes(4-len(bytes(i.encode()))) + bytes(i.encode()))
    return data

