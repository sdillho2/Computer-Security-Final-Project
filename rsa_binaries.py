import gmpy2
from gmpy2 import powmod

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

# ADD PRIVATE KEY TO USE
d = int(input("Enter your private key (d): "))

# Message to be encrypted
# ADD IN USER INPUT TO GET THE MESSAGE TO ENCRYPT
binary_msg = input("Enter your binary message you want to encrypt: ")
msg = int(binary_msg, 2)  # Convert binary to integer
print("Message data = ", msg)

c = powmod(msg, e, n)  # Use built-in pow() with modulo
print("Encrypted data = ", c)


m = powmod(c, d, n)  # Use built-in pow() with modulo
print("Original Message Sent (decrypted)= ", m)