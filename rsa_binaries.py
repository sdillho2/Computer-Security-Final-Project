def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus  # Reduce the base modulo modulus
    while exponent > 0:
        # exponent is odd, multiply result with base modulo modulus
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Exponentiate base by squaring and reduce modulo modulus
        base = (base * base) % modulus
        # Divide exponent by 2
        exponent //= 2
    return result

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

c = mod_pow(msg, e, n)  # Use built-in pow() with modulo
print("Encrypted data = ", c)


m = mod_pow(c, d, n)  # Use built-in pow() with modulo
print("Original Message Sent (decrypted)= ", m)