"""""
Contains some decrypting methods
"""""
import math

import Network.functions
import Cryptology.ressources
from math import gcd


def cesar_decode(int_array, key):
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] - key
    return int_array


def vigenere_decode(int_array, key):
    for i, val in enumerate(int_array):
        key_value = key[i % len(key)]
        int_array[i] = int_array[i] - key_value
    return int_array

def get_value(k): # donne la valeur d'un dictionnaire à partir d'une clef
        for clef, valeur in Cryptology.ressources.letterFrequency.items():
            if k == clef:
                return valeur

        return "There is no such Key"
def cryptanalysis_cesar(int_array):  # cryptanalysis method against shift

    # calculation of each element frequency
    frequencyDict = dict()
    visited = set()
    listLength = len(int_array)
    for i in range(listLength):
        if int_array[i] in visited:
            pass
        else:
            count = 0
            element = int_array[i]
            visited.add(int_array[i])
            for j in range(listLength - i):
                if int_array[j + i] == element:
                    count += 1
            frequencyDict[element] = round(count / len(int_array), 4)

    difference = 0
    difference_maximum = 1
    good_pick = 0
    the_key = 0
    for key, value in frequencyDict.items():
        difference = abs(get_value('e') - value)
        if difference < difference_maximum:
            difference_maximum = difference
            good_pick = key
    the_key = good_pick - 101
    # Decrypting the text with the found key
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] - the_key
    return int_array
def shift_for_char(int_array): # fonction d'analyse fréquentielle retournant le
    frequencyDict = dict()
    visited = set()
    listLength = len(int_array)
    for i in range(listLength):
        if int_array[i] in visited:
            pass
        else:
            count = 0
            element = int_array[i]
            visited.add(int_array[i])
            for j in range(listLength - i):
                if int_array[j + i] == element:
                    count += 1
            frequencyDict[element] = round(count / len(int_array), 4)

    difference = 0
    difference_maximum = 1
    good_pick = 0
    the_key = 0
    for key, value in frequencyDict.items():
        difference = abs(get_value('e') - value)
        if difference < difference_maximum:
            difference_maximum = difference
            good_pick = key
    the_key = good_pick - 101
    return the_key


def cryptanalysis_vigenere(int_array):
    #  1. trouver la longeur de la clef :
    list_d = []
    for n in range(2, 8):  # On receuille tous les fragments de longueur 2 à 8
        for i in range(0, len(int_array)-n):
            fragment_i = int_array[i: i + n]    # selon le fragment de base i jusqu'à n
            for j in range(i+1, len(int_array)-n):  # pour tous les fragment_j de même taille que le fragment_i
                fragment_j = int_array[j: j + n]
                if fragment_j == fragment_i:
                    list_d.append(j-i)
        print("Fragments de longueur " + str(n) + " collectés...")
    print("Liste des fragments trouvés terminées")
    l = 2
    while l != 0:
        temp = []
        for i in range(0, len(list_d) - 2, 2):
            if math.gcd(list_d[i], list_d[i+1]) != 1:
                temp.append(math.gcd(list_d[i], list_d[i+1]))
        l -= 1
        list_d = temp

    frequencyDict = dict()
    visited = set()
    listLength = len(list_d)
    for i in range(listLength):
        if list_d[i] in visited:
            pass
        else:
            count = 0
            element = list_d[i]
            visited.add(list_d[i])
            for j in range(listLength - i):
                if list_d[j + i] == element:
                    count += 1
            frequencyDict[element] = round(count / len(list_d), 4)

    #  Recherche de la longeur la plus présente après 2 rounds de PGDC
    difference_maximum = 0
    key_length = 0
    for key, value in frequencyDict.items():
        if value > difference_maximum :
            difference_maximum = value
            key_length = key
    print("La longeur de la clef : " + str(key_length))

    #  2. retrouver la clef à partir de sa longueur
    collecting_index = 0
    list_crypt_char = []
    word = []
    for t in range(0, key_length):
        # collecte de toutes lettres émanant du même char de la clef
        while collecting_index < len(int_array):
            list_crypt_char.append(int_array[collecting_index])
            collecting_index += key_length
        # shift cryptanalysis de cette liste de lettres
        word.append(shift_for_char(list_crypt_char))
        list_crypt_char = []
        collecting_index = t + 1
    print("Mot de cryptage : " + Network.functions.int_array_to_string(word))

    # 3. Décryptage de Vigenere avec la clef
    return vigenere_decode(int_array, word)
