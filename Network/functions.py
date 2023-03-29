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

# i.to_bytes(2, 'big').decode('utf-8')
def string_to_int_array(text):  # transform a string text, from each char into an array of int
    int_array = [0 for _ in range(len(text))]
    indices = 0
    for i in text:
        int_array[indices] = ord(i)
        indices += 1
# int.from_bytes(i.encode('utf-8'), 'big')
    return int_array
