import math


def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

# ADD INPUT TO GET PUBLIC KEY E,N AND PRIVATE KEY D
e = int(input("Enter your public key for e: "))
n = int(input("Enter your public key for n: "))

# Private key (d stands for decrypt)
# choosing d such that it satisfies
# d*e = 1 + k * totient
# ADD PRIVATE KEY TO USE
d = int(input("Enter your private key (d): "))
#d = (1 + (k*phi))/e

# Message to be encrypted
# ADD IN USER INPUT TO GET THE MESSAGE TO ENCRYPT
text = input("Enter your text message you want to encrypt: ")

# Convert text to numerical representation using ASCII
numerical_msg = [ord(char) for char in text]

print("Message data = ", numerical_msg)

# Encryption c = (msg ^ e) % n
encrypted_msg = [pow(char, e, n) for char in numerical_msg]
print("Encrypted data = ", encrypted_msg)

# Decryption m = (c ^ d) % n
decrypted_msg = [pow(char, d, n) for char in encrypted_msg]
print("Original Message Sent = ", ''.join([chr(int(char)) for char in decrypted_msg]))
