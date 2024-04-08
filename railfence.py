# Function to encrypt a message using Rail Fence Cipher
def encryptRailFence(text, key):
    # Create the matrix to cipher
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        rail[row][col] = text[i]
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Construct the cipher using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ''.join(result)
     
# Function to decrypt a message using Rail Fence Cipher
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
             
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)

# Driver code
if __name__ == "__main__":
    while True:
        choice = input("Select 'encrypt' or 'decrypt': ").lower()
        if choice == 'encrypt':
            # Input message and key from the user for encryption
            message = input("Enter the message to encrypt: ")
            encryption_key = int(input("Enter the encryption key: "))
            
            # Encrypt the message using Rail Fence Cipher
            encrypted_message = encryptRailFence(message, encryption_key)
            print("Encrypted message:", encrypted_message)
            break
        elif choice == 'decrypt':
            # Input cipher and key from the user for decryption
            cipher = input("Enter the cipher to decrypt: ")
            decryption_key = int(input("Enter the decryption key: "))
            
            # Decrypt the cipher using Rail Fence Cipher
            decrypted_message = decryptRailFence(cipher, decryption_key)
            print("Decrypted message:", decrypted_message)
            break
        else:
            print("Invalid choice! Please select 'encrypt' or 'decrypt'.")