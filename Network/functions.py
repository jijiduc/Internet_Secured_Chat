"""""
Contient les fonctions d'encodage et décodage du protocole du server
"""""


def encode(message, type):  # fonction encodage de message
    data = b'ISC'
    data += type.encode()
    data += len(message).to_bytes(2, "big")
    for i in message:
        data += (bytes(4 - len(bytes(i.encode()))) + bytes(i.encode()))
    return data


def decode(message):  # fonction de décodage d'un message
    data = ""
    décodable = message[6:len(message)]
    info = [décodable[i:i + 4] for i in range(0, len(décodable), 4)]
    for i in info:
        byte = b''
        for j in i:
            if j != 0 or byte != b'':
                byte += j.to_bytes(1, 'big')
        data += byte.decode()
    return data
