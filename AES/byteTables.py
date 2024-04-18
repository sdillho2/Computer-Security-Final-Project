#!/usr/bin/env python
## byteTables.py
## Felixander Kery (April 16, 2024)
## This is a Python implementation of the byte substitution transformations for AES using BitVector.
from BitVector import *

# Define the modulus for GF(2^8) as used in AES
AES_modulus = BitVector(bitstring='100011011')

# Initialize substitution tables
subBytesTable = []  # SBox for encryption
invSubBytesTable = []  # SBox for decryption

def genTables():
    c = BitVector(bitstring='01100011')
    d = BitVector(bitstring='00000101')
    for i in range(256):
        # For the encryption SBox
        if i != 0:
            a = BitVector(intVal=i, size=8).gf_MI(AES_modulus, 8)
        else:
            a = BitVector(intVal=0, size=8)
        
        # Bit scrambling for the encryption SBox entries:
        a1, a2, a3, a4 = [a.deep_copy() for _ in range(4)]
        a ^= (a1 >> 4) ^ (a2 >> 5) ^ (a3 >> 6) ^ (a4 >> 7) ^ c
        subBytesTable.append(int(a))
        
        # For the decryption SBox
        b = BitVector(intVal=i, size=8)
        
        # Bit scrambling for the decryption SBox entries:
        b1, b2, b3 = [b.deep_copy() for _ in range(3)]
        b = (b1 >> 2) ^ (b2 >> 5) ^ (b3 >> 7) ^ d
        
        test = b.gf_MI(AES_modulus, 8)
        if isinstance(test, BitVector):
            b = test
        else:
            b = 0
        invSubBytesTable.append(int(b))
    return [int(bv) for bv in subBytesTable], [int(bv) for bv in invSubBytesTable]
        
def print_tables(subBytesTable, invSubBytesTable):
    print("SBox for Encryption:")
    print(subBytesTable)
    print("\nSBox for Decryption:")
    print(invSubBytesTable)

if __name__ == '__main__':
    sbox, inv_sbox = genTables()
    print_tables(sbox, inv_sbox)