"""""
Contains some encrypting methods
"""""
import random
from Network.functions import powerAndModRSA

def caesar(int_array, number):  # using caesar cypher concept
    for i in range(0, len(int_array)):
        int_array[i] = int_array[i] + number
    return int_array


def vigenere(int_array, key):   # Vigenere encoding
    for i, val in enumerate(int_array):
        key_value = key[i % len(key)]
        int_array[i] = int_array[i] + key_value
    return int_array


def generatePrimes(rangeMin, rangeMax):
    depart = random.randint(rangeMin, rangeMax)
    for depart in range(depart, rangeMax):
        for x in range(2, depart):
            if (depart % x == 0):
                break
        else:
            return depart

def LOOOOOONGEUCLIDE(r, r2):
    u = 1
    v = 0
    u2 = 0
    v2 = 1
    while r2 != 0:
        q = r / r2
        rs = r
        us = u
        vs = v
        r = r2
        u = u2
        v = v2
        r2 = rs - q * r2
        u2 = us - q * u2
        v2 = vs - q * v2
    return (r)


def newRSAKey(): #RSA encoding
    p = generatePrimes(1,20000)
    q = generatePrimes(1,20000)
    n = p * q
    k = (p - 1) * (q - 1)
    e = generatePrimes(1, k)
    d = LOOOOOONGEUCLIDE(e,k)
    out = [e, d]
    print(f"VOILA LES NOUVELLES CLES D'ENCRYPTION CHEF:\n"
          f"PUBLIQUE: ({n}, {e})\n"
          f"PRIVEE: ({n}, {d})")

    return(out)


def RSAEncrypt(int_array, key, modulo):
    for i in range(0, len(int_array)):
        int_array[i] = powerAndModRSA(int_array[i], key, modulo)
    return int_array