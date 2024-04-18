#!/usr/bin/env python
## keyExpansion.py

import sys
from BitVector import *
from byteTables import genTables

# We'll be replacing the BitVector calls with native Python integers
# For compatibility with the BitVector code, we use '0b' prefix to define binary numbers

# Define the AES modulus for use in the gf_multiply_modular function below
AES_modulus = BitVector(bitstring='100011011')

def main():
    key_words = []
    keysize, key_bv = get_key_from_user()
    if keysize == 128:
        key_words = gen_key_schedule_128(key_bv)
    elif keysize == 192:
        key_words = gen_key_schedule_192(key_bv)
    elif keysize == 256:
        key_words = gen_key_schedule_256(key_bv)
    else:
        sys.exit("wrong keysize --- aborting")

    key_schedule = []
    print("\nEach 32-bit word of the key schedule is shown as a sequence of 4 one-byte integers:")
    for word_index, word in enumerate(key_words):
        keyword_in_ints = []
        for i in range(4):
            keyword_in_ints.append(word[i*8:i*8+8].intValue())
        if word_index % 4 == 0: print("\n")
        print("word %d: %s" % (word_index, str(keyword_in_ints)))
        key_schedule.append(keyword_in_ints)

    num_rounds = {128: 10, 192: 12, 256: 14}.get(keysize, None)
    round_keys = [None for _ in range(num_rounds+1)]
    for i in range(num_rounds+1):
        round_keys[i] = (key_words[i*4] + key_words[i*4+1] + key_words[i*4+2] + key_words[i*4+3]).get_bitvector_in_hex()
    print("\n\nRound keys in hex (first key for input block):\n")
    for round_key in round_keys:
        print(round_key)

def gee(keyword, round_constant, byte_sub_table):
    """ This function performs the g() transformation used in AES key expansion. """
    # Perform a one-byte left circular rotation on the argument 4-byte word
    rotated_word = keyword.deep_copy()
    rotated_word << 8
    newword = BitVector(size=0)
    for i in range(4):
        # Perform a byte substitution for each byte of the word
        # using the previously generated S-box
        byte = rotated_word[8*i:8*i+8].intValue()
        byte_sub = BitVector(intVal=byte_sub_table[byte], size=8)
        newword += byte_sub
    # XOR the leftmost byte of the transformed word with the round constant
    newword[:8] ^= round_constant
    # Update the round constant for the next round using gf_multiply_modular
    round_constant = round_constant.gf_multiply_modular(BitVector(intVal=0x02), AES_modulus, 8)
    return newword, round_constant

def gen_key_schedule_128(key_bv):
    subBytesTable, _ = genTables()
    key_words = [None for i in range(44)]
    round_constant = BitVector(intVal=0x01, size=8)
    for i in range(4):
        key_words[i] = key_bv[i*32: i*32+32]
    for i in range(4, 44):
        if i % 4 == 0:
            kwd, round_constant = gee(key_words[i-1], round_constant, subBytesTable)
            key_words[i] = key_words[i-4] ^ kwd
        else:
            key_words[i] = key_words[i-4] ^ key_words[i-1]
    return key_words

def gen_key_schedule_192(key_bv):
    subBytesTable, _ = genTables()
    key_words = [None for i in range(52)]
    round_constant = BitVector(intVal=0x01, size=8)
    for i in range(6):
        key_words[i] = key_bv[i*32: i*32+32]
    for i in range(6, 52):
        if i % 6 == 0:
            kwd, round_constant = gee(key_words[i-1], round_constant, subBytesTable)
            key_words[i] = key_words[i-6] ^ kwd
        else:
            key_words[i] = key_words[i-6] ^ key_words[i-1]
    return key_words

def gen_key_schedule_256(key_bv):
    subBytesTable, _ = genTables()
    key_words = [None for i in range(60)]
    round_constant = BitVector(intVal=0x01, size=8)
    for i in range(8):
        key_words[i] = key_bv[i*32: i*32+32]
    for i in range(8, 60):
        if i % 8 == 0:
            kwd, round_constant = gee(key_words[i-1], round_constant, subBytesTable)
            key_words[i] = key_words[i-8] ^ kwd
        elif (i % 8) == 4:
            # Apply byte substitution to the whole word
            transformed_word = BitVector(size=0)
            for j in range(4):
                byte_val = key_words[i-1][j*8:j*8+8].intValue()
                sub_byte = subBytesTable[byte_val]
                transformed_word += BitVector(intVal=sub_byte, size=8)
            key_words[i] = key_words[i-8] ^ transformed_word
        else:
            key_words[i] = key_words[i-8] ^ key_words[i-1]
    return key_words



def get_key_from_user():
    if sys.version_info[0] == 3:
        keysize = int(input("\nAES Key size: "))
        key = input("\nEnter key (any number of chars): ")
    else:
        keysize = int(raw_input("\nAES Key size: "))
        key = raw_input("\nEnter key (any number of chars): ")
    key = key.strip()
    key += '0' * (keysize//8 - len(key)) if len(key) < keysize//8 else key[:keysize//8]
    key_bv = BitVector(textstring=key)
    assert keysize in [128, 192, 256], "keysize is wrong (must be one of 128, 192, or 256) --- aborting"
    return keysize, key_bv

if __name__ == '__main__':
    main()
