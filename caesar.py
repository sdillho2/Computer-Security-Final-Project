def encrypt(M,K):
    C = ""

    # iterate over the given text
    for ch in M:
        
        # check if the character is a space
        if ch == " ":
            C += " "

        # check if a character is uppercase 
        elif (ch.isupper()):
            #encrypt uppercase
            #65 is uppercase A
            A = 65
            C += chr((ord(ch) + K-A) % 26 + A)

        # the character is lowercase
        else:
            #encrypt lowercase
            #97 is lowercase a
            a = 97
            C += chr((ord(ch) + K-a) % 26 + a)
    
    return C

def decrypt(C,K):
    D = ""

    # iterate over the given text
    for ch in C:
        
        # check if the character is a space
        if ch == " ":
            D += " "

        # check if a character is uppercase 
        elif (ch.isupper()):
            #decrypt uppercase
            #65 is uppercase A
            A = 65
            D += chr((ord(ch) - K-A) % 26 + A)

        # the character is lowercase
        else:
            #decrypt lowercase
            #97 is lowercase a
            a = 97
            D += chr((ord(ch) - K-a) % 26 + a)
    
    return D


#TO DO: make it for user input
M = "HELLO WORLD"
#CM= input("Enter the message to be encrypted: ").strip()
K = 3
#K = int(input("Enter the key to encrypt: "))
print("Plain Text is : " + M)
print("Key is : " + str(K))
print("Cipher Text is : " + encrypt(M,K))

C = "KHOOR ZRUOG"
#C = input("Enter the message to be decrypted: ").strip()
K = 3
#K = int(input("Enter the key to decrypt: "))
print("Cipher Text is : " + C)
print("Key is : " + str(K))
print("Plain Text is : " + decrypt(C,K))