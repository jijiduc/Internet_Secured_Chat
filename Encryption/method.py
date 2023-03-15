"""""
Contient les méthodes de cryptage et de décryptage
"""""
def shift(text, shift):
    data = 0
    for i in text :
        data += i + shift
    return data

def unshift(text):
    number = 0
    letter = ''
    for i in range(128):
        for i in text:
            lol = ""

    return text