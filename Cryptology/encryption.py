"""""
Contains some encrypting method
"""""


def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number

    return int_array


def vigenere_cipher(key, message):
    """
    Encrypts the given message using Vigenere cipher with the given key represented as a list of integers.

    Parameters:
    key (list of int): The key to use for encryption.
    message (list of int): The message to encrypt.

    Returns:
    list of int: The encrypted message.
    """
    encrypted_message = []
    key_len = len(key)
    for i, char in enumerate(message):
        key_index = i % key_len
        key_value = key[key_index]
        encrypted_char = (char + key_value) % 256
        encrypted_message.append(encrypted_char)
    return encrypted_message
