"""""
Contains some decrypting methods
"""""
import string
import ressources


def cesar_decode(int_array, key):
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] - key

    return int_array








def cracking_cesar(text):  # decrypting method : caesar cypher
    text = text.lower()

    # calculation of each letter frequency
    freq = {}
    for letter in string.ascii_lowercase:
        freq[letter] = text.count(letter) / len(text)

    #  Key finding process
    min_diff = float('inf')
    best_key = 0
    for key in range(26):
        diff = 0
        for letter in ressources.letterFrequency:
            shifted_letter = chr((ord(letter) - 65 + key) % 26 + 65)
            diff += abs(freq.get(shifted_letter, 0) - ressources.letterFrequency[letter])
        if diff < min_diff:
            min_diff = diff
            best_key = key

    # Decrypting the text with the found key
    result = ""
    for letter in text:
        if letter in string.ascii_uppercase:
            shifted_letter = chr((ord(letter) - 65 - best_key) % 26 + 65)
            result += shifted_letter
        else:
            result += letter

    return result
