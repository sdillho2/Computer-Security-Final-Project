#!/usr/bin/env python
# driver.py

import sys
from keyExpansion import gen_key_schedule_128, gen_key_schedule_192, gen_key_schedule_256, get_key_from_user
from byteTables import genTables
from mixCols import mixColumns, invMixColumns
from shiftRows import shiftRows, invShiftRows

def encrypt(text, key_schedule, subBytesTable):
    def encrypt(plaintext, key_schedule, subBytesTable, num_rounds):
    state = text_to_state(plaintext)
    
    # Initial round key addition
    state = add_round_key(state, key_schedule[:4])
    
    # Rounds
    for round_num in range(1, num_rounds):
        state = sub_bytes(state, subBytesTable)
        state = shiftRows(state)
        state = mixColumns(state)
        state = add_round_key(state, key_schedule[round_num * 4:(round_num + 1) * 4])
    
    # Final round (no mixColumns)
    state = sub_bytes(state, subBytesTable)
    state = shiftRows(state)
    state = add_round_key(state, key_schedule[num_rounds * 4:(num_rounds + 1) * 4])
    
    # Convert state to text
    return state_to_text(state)


def decrypt(text, key_schedule, invSubBytesTable):
    # Add your implementation here
    # This should use invMixColumns, invShiftRows, and other necessary steps to decrypt the text
    pass

def main():
    # User interface to select encryption or decryption
    action = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    keysize = int(input("Enter AES key size (128, 192, 256): ").strip())
    
    # Load key and S-boxes
    key_bv = get_key_from_user()
    subBytesTable, invSubBytesTable = genTables()
    
    # Generate the key schedule based on the keysize
    if keysize == 128:
        key_schedule = gen_key_schedule_128(key_bv)
    elif keysize == 192:
        key_schedule = gen_key_schedule_192(key_bv)
    elif keysize == 256:
        key_schedule = gen_key_schedule_256(key_bv)
    else:
        sys.exit("Invalid key size. Only 128, 192, or 256 are allowed.")

    # Get the text to process
    text = input("Enter the text: ").strip()

    # Perform the requested operation
    if action == 'e':
        encrypted_text = encrypt(text, key_schedule, subBytesTable)
        print(f"Encrypted text: {encrypted_text}")
    elif action == 'd':
        decrypted_text = decrypt(text, key_schedule, invSubBytesTable)
        print(f"Decrypted text: {decrypted_text}")
    else:
        sys.exit("Invalid action. Only 'e' for encryption and 'd' for decryption are allowed.")

if __name__ == '__main__':
    main()
