import tkinter as tk

# Function to encrypt a message using Rail Fence Cipher
def encryptRailFence(text, key):
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

def encrypt_button_clicked():
    message = entry_message.get()
    key = int(entry_key.get())
    encrypted_message = encryptRailFence(message, key)
    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, encrypted_message)
    text_result.config(state=tk.DISABLED)

def decrypt_button_clicked():
    cipher = entry_message.get()
    key = int(entry_key.get())
    decrypted_message = decryptRailFence(cipher, key)
    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, decrypted_message)
    text_result.config(state=tk.DISABLED)

# Create GUI
root = tk.Tk()
root.title("Rail Fence Cipher Tool")

# Create input fields
label_message = tk.Label(root, text="Enter Message:")
label_message.pack()
entry_message = tk.Entry(root)
entry_message.pack()

label_key = tk.Label(root, text="Enter Key:")
label_key.pack()
entry_key = tk.Entry(root)
entry_key.pack()

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack()

# Create result display
label_result = tk.Label(root, text="Result:")
label_result.pack()
text_result = tk.Text(root, height=5, width=50)
text_result.pack()

root.mainloop()