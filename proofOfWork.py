# coding=utf-8
#!/bin/python3
#!/usr/bin/python3

import hashlib
import random


def _get_new_hash():
    intToHash = random.randint(0, 2**128-1)
    hashHexa = hashlib.md5(str(intToHash).encode()).hexdigest()
    hashInt = int(hashHexa, 16)
    hashBin = bin(hashInt)
    return hashBin[3:]
    

def proof_of_work(nbOfZeros):

    stringOfZeros = "0" * int(nbOfZeros)
    stringHash = _get_new_hash()

    while not stringHash.startswith(stringOfZeros):
        stringHash = _get_new_hash()
    
    return stringHash


#print(_get_new_hash())
print(len(proof_of_work(20)))