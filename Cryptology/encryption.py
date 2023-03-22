"""""
Contains some encrypting method
"""""


def caesar(text, number):  # encrypting method : caesar cypher
    data = 0
    for i in text.encode():
        data += i + number
    return data
