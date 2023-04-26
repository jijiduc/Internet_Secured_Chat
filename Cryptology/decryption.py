"""""
Contains some decrypting methods
"""""
import string
import Cryptology.ressources
import Network.functions


def cesar_decode(int_array, key):
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] - key
    return int_array


def vigenere_decode(int_array, key):
    for i, val in enumerate(int_array):
        key_value = key[i % len(key)]
        int_array[i] = int_array[i] - key_value
    return int_array


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

    # print("Input list is:", int_array)
    # print("Frequency of elements is:")
    # print(frequencyDict)
    # print(ord('e'))

    def get_value(k): # donne la valeur d'un dictionnaire à partir d'une clef
        for clef, valeur in Cryptology.ressources.letterFrequency.items():
            if k == clef:
                return valeur

        return "There is no such Key"

    # Key finding process
    difference = 0
    difference_maximum = 1
    good_pick = 0
    the_key = 0
    for key, value in frequencyDict.items():
        difference = abs(get_value('e') - value)
        if difference < difference_maximum:
            difference_maximum = difference
            good_pick = key

    # print(good_pick)
    the_key = good_pick - 101
    # print("clef final : ")
    # print(the_key)

    # Decrypting the text with the found key
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] - the_key
    return int_array

# def kasiski(int_array): # permet de trouver la longeur de la clef d'un cryptage de vigenere


def detect_repetition(int_array):
    repetitions = []
    ensemble_de_sous_chaines = []
    for n in range(0, 100):
        for i in range(0, len(int_array)-1):
            sous_chaine = int_array[i: i + n]
            print(Network.functions.int_array_to_string(sous_chaine))
            for j in range(i, len(int_array)-1):
                sous_chaine_de_test = int_array[j: j + n]
                if sous_chaine_de_test == sous_chaine:
                    ensemble_de_sous_chaines += sous_chaine_de_test

            if len(ensemble_de_sous_chaines) > len(repetitions):
                repetitions = ensemble_de_sous_chaines
                ensemble_de_sous_chaines = []


    return repetitions


