"""""
Contains some encrypting method
"""""


def caesar(text, number):  # encrypting method : caesar cypher
    data = 0
    for i in text:
        data += i + number
    return data
