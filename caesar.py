def encrypt(M,K):
    C = ""

    #convert to uppecase 
    M = M.upper()

    # iterate over the given text
    for ch in M:

        #check if the character is a letter
        if ch.isalpha():

            #encrypt uppercase
            #65 is uppercase A
            A = 65
            C += chr((ord(ch) + K-A) % 26 + A)

        else:
            C += ch
    
    return C

def decrypt(C,K):
    D = ""

    #convert to uppercase
    C = C.upper()

    # iterate over the given text
    for ch in C:
        
        # check if the character is a letter
        if ch.isalpha():
            #decrypt uppercase
            #65 is uppercase A
            A = 65
            D += chr((ord(ch) - K-A) % 26 + A)

        else:
             D += " "
    
    return D


#TO DO: make it for user input
#M = "Hello World"
#CM= input("Enter the message to be encrypted: ").strip()
#K = 3
#K = int(input("Enter the key to encrypt: "))
#print("Plain Text is : " + M)
#print("Key is : " + str(K))
#print("Cipher Text is : " + encrypt(M,K))

#C = "Khoor ZRUOG"
#C = input("Enter the message to be decrypted: ").strip()
#K = 3
#K = int(input("Enter the key to decrypt: "))
#print("Cipher Text is : " + C)
#print("Key is : " + str(K))
#print("Plain Text is : " + decrypt(C,K))