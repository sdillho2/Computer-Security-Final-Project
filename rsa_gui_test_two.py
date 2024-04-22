import tkinter as tk
from tkinter import filedialog, messagebox
from gmpy2 import powmod

PADDING_CORRECTION = 1

def encrypt(message, key):
	e, _, n = key
    # Your encrypt function code goes here
	if isinstance(message, bytes) or isinstance(message, bytearray):
		message = list(message)
	elif isinstance(message, str):
		message = list(map(ord, message))
	else:
		message = list(message)
	e, _d, n = key
	cipher = []
	for iblock in range(0, len(message), 16 - PADDING_CORRECTION):
		m = int.from_bytes(message[iblock:iblock+16 - PADDING_CORRECTION], "big")
		c = int(powmod(m, e, n))
		cipher.extend(c.to_bytes(16, "big"))
	return cipher

def decrypt(cipher, key):
    _, d, n = key
    if isinstance(cipher, bytes) or isinstance(cipher, bytearray):
        cipher = list(cipher)
    elif isinstance(cipher, str):
        cipher = list(map(ord, cipher))
    else:
        cipher = list(cipher)
        
    _e, d, n = key
    message = []
    for iblock in range(0, len(cipher), 16):
        c = int.from_bytes(cipher[iblock:iblock+16], "big")
        m = int(powmod(c, d, n))
        message.extend(m.to_bytes(16 - PADDING_CORRECTION, "big"))
    return message

def encrypt_text(text, key, blocksize=16):
    text = text.strip()
    text = bytes(text, encoding='utf-8')
    if blocksize:
        blocksize = blocksize - PADDING_CORRECTION
        pad_length = blocksize - (len(text) % blocksize)
        text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    return bytes(cipher).hex()

def decrypt_text(cipher, key, blocksize=16):
    cipher = bytes.fromhex(cipher)
    text = decrypt(cipher, key)
    if blocksize:
        text = text[:-text[-1]]
    text = bytes(text).decode("utf-8") 
    return text

def encrypt_image(filename, key, blocksize=16):
    with open(filename, "rb") as img_file:
        img = bytes(img_file.read())
    if blocksize:
        blocksize = blocksize - PADDING_CORRECTION
        pad_length = blocksize - (len(img) % blocksize)
        img += bytes([pad_length]) * pad_length
    cipher = encrypt(img, key)
    with open('./encryptedImage.jpeg', 'wb') as out:
        out.write(bytes(cipher))
    return "./encryptedImage.jpeg"
	
def decrypt_image(filename, key, blocksize=16):
    with open(filename, "rb") as cipher_file:
        cipher = bytes(cipher_file.read())
    img = decrypt(cipher, key)
    if blocksize:
        img = img[:-img[-1]]
    with open('./decryptedImage.jpeg', 'wb') as out:
        out.write(bytes(img))
    return './decryptedImage.jpeg'

def encrypt_file(filename, key, blocksize=16):
    with open(filename, "r", newline="\n") as text_file:
        text = bytes(text_file.read(), encoding='utf8')
    if blocksize:
        blocksize = blocksize - PADDING_CORRECTION
        pad_length = blocksize - (len(text) % blocksize)
        text += bytes([pad_length]) * pad_length
    cipher = encrypt(text, key)
    cipher = bytes(cipher)
    with open('./encryptedFile.c', 'wb') as out:
        out.write(cipher)
    return "./encryptedFile.c"

def decrypt_file(filename, key, blocksize=16):
    with open(filename, "rb") as cipher_file:
        cipher = bytes(cipher_file.read())
    text = decrypt(cipher, key)
    if blocksize:
        text = text[:-text[-1]]
    text = bytes(text).decode("utf-8") 
    with open('./decryptedFile.c', 'w', newline="\n") as out:
        out.write(text)
    return "./decryptedFile.c"

def browse_file():
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def toggle_text_entry():
    if mode_var.get() == "Text":
        text_entry.grid(row=3, column=1, padx=5, pady=5)
    else:
        text_entry.grid_remove()

def encrypt_gui():
    mode = mode_var.get()
    if mode == "File":
        filename = entry.get()
        key = key_entry.get()
        try:
            key = eval(key)  # Convert string input to tuple
            encrypted_filename = encrypt_file(filename, key)
            messagebox.showinfo("Encryption Successful", f"File encrypted successfully. Encrypted file: {encrypted_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    elif mode == "Text":
        text = text_entry.get("1.0", tk.END).strip()
        key = key_entry.get()
        try:
            key = eval(key)  # Convert string input to tuple
            encrypted_text = encrypt_text(text, key)
            messagebox.showinfo("Encryption Successful", f"Text encrypted successfully. Encrypted text: {encrypted_text}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def decrypt_gui():
    mode = mode_var.get()
    if mode == "File":
        filename = entry.get()
        key = key_entry.get()
        try:
            key = eval(key)  # Convert string input to tuple
            decrypted_filename = decrypt_file(filename, key)
            messagebox.showinfo("Decryption Successful", f"File decrypted successfully. Decrypted file: {decrypted_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    elif mode == "Text":
        cipher = text_entry.get("1.0", tk.END).strip()
        key = key_entry.get()
        try:
            key = eval(key)  # Convert string input to tuple
            decrypted_text = decrypt_text(cipher, key)
            messagebox.showinfo("Decryption Successful", f"Text decrypted successfully. Decrypted text: {decrypted_text}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("RSA Encryption and Decryption")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

mode_var = tk.StringVar()
mode_var.set("File")

mode_label = tk.Label(frame, text="Select Mode:")
mode_label.grid(row=0, column=0, sticky="w")

file_radio = tk.Radiobutton(frame, text="File", variable=mode_var, value="File", command=toggle_text_entry)
file_radio.grid(row=0, column=1, padx=5, pady=5)

text_radio = tk.Radiobutton(frame, text="Text", variable=mode_var, value="Text", command=toggle_text_entry)
text_radio.grid(row=0, column=2, padx=5, pady=5)

label = tk.Label(frame, text="Select File/Enter Text:")
label.grid(row=1, column=0, sticky="w")

entry = tk.Entry(frame, width=40)
entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=1, column=2, padx=5, pady=5)

key_label = tk.Label(frame, text="Enter RSA Key (as tuple e, d, n):")
key_label.grid(row=2, column=0, sticky="w")

key_entry = tk.Entry(frame, width=40)
key_entry.grid(row=2, column=1, padx=5, pady=5)

text_entry = tk.Text(frame, width=40, height=5)
text_entry.grid(row=3, column=1, padx=5, pady=5)
text_entry.grid_remove()  # Hide the text entry box initially

encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt_gui)
encrypt_button.grid(row=4, column=1, padx=5, pady=5)

decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt_gui)
decrypt_button.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()