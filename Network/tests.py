import Network.functions

if __name__ == "__main__":
    stack = bytes(b'ISCt\x00\x06\x00\x00\x00c\x00\x00\x00o\x00\x00\x00u\x00\x00\x00c\x00\x00\x00o\x00\x00\x00u')

    print(Network.functions.decode_to_int(stack))