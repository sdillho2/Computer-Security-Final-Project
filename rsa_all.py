from gmpy2 import powmod

def encrypt(message, key):
    if isinstance(message, bytes) or isinstance(message, bytearray):
        message = list(message)
    elif isinstance(message, str):
        message = list(map(ord, message))
    else:
        message = list(message)
        
    e, _d, n = key
    cipher = []
    for iblock in range(0, len(message), 16 - 1):
        m = int.from_bytes(message[iblock:iblock+16 - 1], "big")
        c = int(powmod(m, e, n))
        cipher.extend(c.to_bytes(16, "big"))
    return cipher

def decrypt(cipher, key):
    if isinstance(cipher, bytes) or isinstance(cipher, bytearray):
        cipher = list(cipher)
    elif isinstance(cipher, str):
        cipher = list(map(ord, cipher))
    else:
        cipher = list(cipher)
        
    _e, d, n = key
    message = []
    for iblock in range(0, len(cipher), 16):
        c = int.from_bytes(cipher[iblock:iblock+16], "big")
        m = int(powmod(c, d, n))
        message.extend(m.to_bytes(16 - 1, "big"))
    return message

def encrypt_text(text, key, blocksize=16):
    text = text.strip()
    text = bytes(text, encoding='utf-8')
    if blocksize:
        blocksize = blocksize - 1
        pad_length = blocksize - (len(text) % blocksize)
        text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    return bytes(cipher).hex()

def decrypt_text(cipher, key, blocksize=16):
    cipher = bytes.fromhex(cipher)
    text = decrypt(cipher, key)
    if blocksize:
        text = text[:-text[-1]]
    text = bytes(text).decode("utf-8") 
    return text
    
def encrypt_image(filename, key, blocksize=16):
    with open(filename, "rb") as img_file:
        img = bytes(img_file.read())
    if blocksize:
        blocksize = blocksize - 1
        pad_length = blocksize - (len(img) % blocksize)
        img += bytes([pad_length]) * pad_length
    cipher = encrypt(img, key)
    with open('./encrypted_image.jpeg', 'wb') as out:
        out.write(bytes(cipher))
    return "./encrypted_image.jpeg"

def decrypt_image(filename, key, blocksize=16):
    with open(filename, "rb") as cipher_file:
        cipher = bytes(cipher_file.read())
    img = decrypt(cipher, key)
    if blocksize:
        img = img[:-img[-1]]
    with open('./decrypted_image.jpeg', 'wb') as out:
        out.write(bytes(img))
    return './decrypted_image.jpeg'

def encrypt_file(filename, key, blocksize=16):
    with open(filename, "r", newline="\n") as text_file:
        text = bytes(text_file.read(), encoding='utf8')
    if blocksize:
        blocksize = blocksize - 1
        pad_length = blocksize - (len(text) % blocksize)
        text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    cipher = bytes(cipher)
    with open('./encrypted_file', 'wb') as out:
        out.write(cipher)
    return "./encrypted_file"

def decrypt_file(filename, key, blocksize=16):
    with open(filename, "rb") as cipher_file:
        cipher = bytes(cipher_file.read())
    text = decrypt(cipher, key)
    if blocksize:
        text = text[:-text[-1]]
    text = bytes(text).decode("utf-8") 
    with open('./decrypted_file', 'w', newline="\n") as out:
        out.write(text)
    return "./decrypted_file"