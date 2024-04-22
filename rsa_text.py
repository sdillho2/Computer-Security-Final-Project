from gmpy2 import powmod

def encrypt(message, key):
    e, _d, n = key
    cipher = b""
    for iblock in range(0, len(message), 8):
        m = int.from_bytes(message[iblock:iblock+8], "big")
        c = powmod(m, e, n)
        # Convert the mpz object to a Python integer and then to bytes
        byte_length = (c.bit_length() + 7) // 8
        cipher += int(c).to_bytes(byte_length, "big")
    return cipher


def decrypt(cipher, key):
    _e, d, n = key
    message = bytearray()  # Use bytearray to efficiently append bytes
    for iblock in range(0, len(cipher), 16):
        c = int.from_bytes(cipher[iblock:iblock+16], "big")
        m = powmod(c, d, n)
        # Convert the mpz object to a Python integer and then to bytes
        byte_length = (m.bit_length() + 7) // 8
        message.extend(int(m).to_bytes(byte_length, "big"))
    return message




def encrypt_text(text, key):
    text = text.strip()
    text = bytes(text, encoding='utf-8')
    block_size = (len(text) // 8 + 1) * 8  # Adjust block size based on message length
    pad_length = block_size - len(text)
    text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    # Convert the byte string cipher to hexadecimal
    encrypted_text = cipher.hex()
    return encrypted_text
    
def decrypt_text(cipher, key):
    cipher = bytes.fromhex(cipher)
    text = decrypt(cipher, key)
    pad_length = text[-1]
    text = text[:-pad_length]
    return text.decode("utf-8") 

def main():
    option = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if option.lower() == 'e':
        text = input("Enter the text to encrypt: ")
        key = (int(input("Enter the public key 'e': ")), 0, int(input("Enter the modulus 'n': ")))
        encrypted_text = encrypt_text(text, key)
        print("Encrypted text:", encrypted_text)
    elif option.lower() == 'd':
        cipher = input("Enter the cipher to decrypt: ")
        key = (0, int(input("Enter the private key 'd': ")), int(input("Enter the modulus 'n': ")))
        decrypted_text = decrypt_text(cipher, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid option. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
