"""""
Contains some encrypting methods
"""""


def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number

    return int_array


def vigenere(int_array, key):
    for i, val in enumerate(int_array):
        # print("index de la liste : " + str(i))
        # print(" index de la clef : " + str(i % len(key)))
        key_value = key[i % len(key)]
        # print("valeur de la clef : " + str(key_value))
        int_array[i] = int_array[i] + key_value
    return int_array
