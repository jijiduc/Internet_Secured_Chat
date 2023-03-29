"""""
Contains some encrypting method
"""""


def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number

    return int_array

