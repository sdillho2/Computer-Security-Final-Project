import rsa

# Generate RSA key pair
(public_key, private_key) = rsa.newkeys(122)

# Extract e, d, and n from the keys
e = public_key.e
d = private_key.d
n = public_key.n

print("e:", e)
print("d:", d)
print("n:", n)