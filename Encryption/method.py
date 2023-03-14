"""""
Contient les méthodes de cryptages
"""""

def shift(text, shift):
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) if 'a' <= char <= 'z' else char
        for char in text.lower())