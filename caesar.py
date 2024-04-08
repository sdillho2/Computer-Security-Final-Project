def encrypt(M,K):
    C = ""

    # iterate over the given text
    for i in range(len(M)):
        ch = M[i]
        
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
            #encrypt lowcase
            #97 is lowercase a
            a = 97
            C += chr((ord(ch) + K-a) % 26 + a)
    
    return C


#TO DO: make it for user input
M = "HELLO WORLD"
K = 3
print("Plain Text is : " + M)
print("Shift pattern is : " + str(K))
print("Cipher Text is : " + encrypt(M,K))