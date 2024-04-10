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

def main():
    # Your main code logic goes here
    g

if __name__ == "__main__":
    main()