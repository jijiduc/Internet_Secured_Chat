"""""
Contains the server's encoding/decoding functions
"""""
import numpy


def encode(message, category):  # encode a str text to the server's protocol
    data = b'ISC'
    data += category.encode()
    data += len(message).to_bytes(2, 'big')
    for i in message:
        data += (bytes(4 - len(bytes(i.encode()))) + bytes(i.encode()))
    return data


def decode_to_int(message):  # transform server's message into an array of int
    data = message[6:len(message)]
    int_array = numpy.full((1, len(data)), numpy.inf)
    indices = 0
    four_byte = [data[i:i + 4] for i in range(0, len(data), 4)]
    for i in four_byte:
        int_array[indices] = int.from_bytes(i, 'big')
        indices += 1
    return int_array


def int_array_to_string(int_array):  # transform an array of int into a string
    string_data = ""
    for i in int_array:
        string_data += str(i)
    return string_data
