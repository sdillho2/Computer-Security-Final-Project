def encrypt(plain_text, key):

    # Convert both the plaintext and key to uppercase
    plain_text = plain_text.upper()
    key = key.upper()
    
    encrypted_text = ""
    key_index = 0

     # iterate over the given text
    for ch in plain_text:

        if ch.isalpha():
            #encrypt uppercase
            #65 is uppercase A
            A = 65
            
            # Shift the character by the corresponding key character
            shift = ord(key[key_index]) - A
            encrypted_text += chr(((ord(ch) - A + shift) % 26) + A)

            # Move to the next character in the key
            key_index = (key_index + 1) % len(key)

        else:
            # If it's not an alphabet character, just append it as it is
            encrypted_text += ch
     

    return encrypted_text

def decrypt(cipher_text, key):
     # Convert both the encrypted text and key to uppercase
    cipher_text = cipher_text.upper()
    key = key.upper()

    plain_text = ""
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            A = 65 
            # Shift the character back by the corresponding key character
            shift = ord(key[key_index]) - A
            plain_text += chr(((ord(ch) - A - shift) % 26) + A)

            # Move to the next character in the key
            key_index = (key_index + 1) % len(key)
        else:
            # If it's not a letter , just append it as it is
            plain_text += ch

    return plain_text

#plain_text = "Hello World"
#key = "KEY"
#cipher_text = encrypt(plain_text, key)
#print("Encrypted text:", cipher_text)

#cipher_text = "RIJVS UYVJN"
#key = "KEY"
#plain_text = decrypt(cipher_text, key)
#print("Decrypted text:", plain_text)



