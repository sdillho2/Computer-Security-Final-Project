# Computer Security Final Project 
# Triple DES

# Define Triple DES encryption and decryption functions

def adjust_key_parity(key):
    """
    Adjust the parity bits of the key to ensure odd parity.
    """
    adjusted_key = bytearray()
    for byte in key:
        parity = 0
        for i in range(7):
            if byte & (1 << i):
                parity = (parity + 1) % 2
        adjusted_byte = byte & 0xFE | parity
        adjusted_key.append(adjusted_byte)
    return bytes(adjusted_key)

def des_block_encrypt(block, key):
    """
    Encrypt a single DES block using a given key.
    """
    # Placeholder for DES block encryption logic
    encrypted_block = block  # Replace with actual DES encryption logic
    return encrypted_block

def triple_des_encrypt(plaintext, key):
    """
    Encrypt plaintext using Triple DES algorithm with the given key.
    """
    # Adjust key parity
    key = adjust_key_parity(key)
    
    # Divide the key into three subkeys
    key1 = key[:8]
    key2 = key[8:16]
    key3 = key[16:]
    
    # Pad plaintext if necessary
    padding_length = 8 - len(plaintext) % 8
    plaintext += bytes([padding_length] * padding_length)
    
    # Encrypt plaintext block by block
    ciphertext = b''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        encrypted_block = des_block_encrypt(block, key1)
        encrypted_block = des_block_encrypt(encrypted_block, key2)
        encrypted_block = des_block_encrypt(encrypted_block, key3)
        ciphertext += encrypted_block
    
    return ciphertext

def triple_des_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Triple DES algorithm with the given key.
    """
    # Adjust key parity
    key = adjust_key_parity(key)
    
    # Divide the key into three subkeys
    key1 = key[:8]
    key2 = key[8:16]
    key3 = key[16:]
    
    # Decrypt ciphertext block by block
    plaintext = b''
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        decrypted_block = des_block_decrypt(block, key3)
        decrypted_block = des_block_decrypt(decrypted_block, key2)
        decrypted_block = des_block_decrypt(decrypted_block, key1)
        plaintext += decrypted_block
    
    # Remove padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    
    return plaintext

# Placeholder function for DES block decryption
def des_block_decrypt(block, key):
    """
    Decrypt a single DES block using a given key.
    """
    # Placeholder for DES block decryption logic
    decrypted_block = block  # Replace with actual DES decryption logic
    return decrypted_block

# Allow users to enter or import the key
def get_key_from_user():
    key = input("Enter the key (24 bytes): ").encode()
    return key

# Allow users to encipher any types of messages
def get_message_from_user():
    message = input("Enter the message: ").encode()
    return message

# Allow users to choose between encryption and decryption
def main():
    while True:
        option = input("Choose an option (1: Encrypt, 2: Decrypt, 3: Exit): ")
        
        if option == '1':
            key = get_key_from_user()
            plaintext = get_message_from_user()
            ciphertext = triple_des_encrypt(plaintext, key)
            print("Ciphertext:", ciphertext.hex())
        elif option == '2':
            key = get_key_from_user()
            ciphertext = bytes.fromhex(input("Enter the ciphertext (in hexadecimal): "))
            plaintext = triple_des_decrypt(ciphertext, key)
            print("Decrypted plaintext:", plaintext.decode())
        elif option == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()