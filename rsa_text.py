from gmpy2 import powmod

def encrypt(message, key):
    e, _d, n = key
    cipher = []
    for iblock in range(0, len(message), 8):
        m = int.from_bytes(message[iblock:iblock+8], "big")
        c = int(powmod(m, e, n))
        cipher.extend(c.to_bytes(16, "big"))
    return cipher

def decrypt(cipher, key):
    _e, d, n = key
    message = []
    for iblock in range(0, len(cipher), 16):
        c = int.from_bytes(cipher[iblock:iblock+16], "big")
        m = int(powmod(c, d, n))
        message.extend(m.to_bytes(8, "big"))
    return message

def encrypt_text(text, key):
    text = text.strip()
    text = bytes(text, encoding='utf-8')
    block_size = (len(text) // 8 + 1) * 8  # Adjust block size based on message length
    pad_length = block_size - len(text)
    text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    return bytes(cipher).hex()

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
