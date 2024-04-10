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
#msg = 12.0
binary_msg = input("Enter your binary message you want to encrypt: ")
msg = int(binary_msg, 2)  # Convert binary to integer
print("Message data = ", msg)

# for each 2 nubmers in msg, find the letter

# Encryption c = (msg ^ e) % n
# c = pow(msg, e)
# c = math.fmod(c, n)
# print("Encrypted data = ", c)
c = pow(msg, e, n)  # Use built-in pow() with modulo
print("Encrypted data = ", c)


# Decryption m = (c ^ d) % n
# m = pow(c, d)
# m = math.fmod(m, n)
# print("Original Message Sent = ", m)
m = pow(c, d, n)  # Use built-in pow() with modulo
print("Original Message Sent (decrypted)= ", m)