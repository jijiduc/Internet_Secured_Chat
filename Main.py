"""""
C'est le fichier main, qui appelle toutes les fonctions et fait tourner le programme
"""""
import Encryption.method
from UI.window import *
from Encryption.method import *

text = "Bonjour, ceci est un test de la méthode de shifting"
shiftedText = Encryption.method.shift(text, 4)
print(text)
print(shiftedText)
