"""""
Contains the server's encoding/decoding functions
"""""


def encode(message, category):  # encode a str text to the server's protocol
    data = b'ISC'
    data += category.encode()
    data += len(message).to_bytes(2, 'big')
    for i in message:
        data += (bytes(4 - len(bytes(i.encode()))) + bytes(i.encode()))
    return data


def decode_to_int(message):  # transform server's message into an array of int
    data = message[6:len(message)]
    int_array = []
    four_byte = [data[i:i + 4] for i in range(0, len(data), 4)]
    for i in four_byte:
        int_array.append(int.from_bytes(i, 'big'))
    return int_array


def int_array_to_string(int_array):  # transform an array of int into a string
    string_data = ""
    for i in int_array:
        string_data += chr(i)
    return string_data


def string_to_int_array(string_data):  # transform a string text into an array of int
    int_array = []
    indices = 0
    for i in string_data:
        int_array[indices] = int(i.encode())
        indices += 1
    return int_array
