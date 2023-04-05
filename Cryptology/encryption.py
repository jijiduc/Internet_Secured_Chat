"""""
Contains some encrypting methods
"""""


def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number
    return int_array


def vigenere(int_array, key):   # Vigenere encoding
    for i, val in enumerate(int_array):
        key_value = key[i % len(key)]
        int_array[i] = int_array[i] + key_value
    return int_array
