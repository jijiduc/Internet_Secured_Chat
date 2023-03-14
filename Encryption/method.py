"""""
Contient les méthodes de cryptage et de décryptage
"""""

def shift(text, shift):
    crypted = ""
    for i in text :
        crypted += chr(ord(i) + shift)
    return crypted

def unshift(text):
    number = 0
    letter = ''
    for i in range(128):
        for i in text:
            lol = ""

    return text