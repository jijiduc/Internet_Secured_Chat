"""""
Contains some encrypting method
"""""


def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number

    return int_array


def vigenere(int_array, word):  # using vigener cypher
    return int_array