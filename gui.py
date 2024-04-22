import tkinter as tk
from tkinter import ttk, messagebox
from vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
from railfence import encryptRailFence, decryptRailFence
from caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from tripleDES import triple_des_encrypt, triple_des_decrypt

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption App")

        self.cipher_options = ['Vigenere', 'Rail Fence', 'Caesar', 'Triple DES']

        self.create_widgets()

    def create_widgets(self):
        # Cipher selection
        self.cipher_label = ttk.Label(self.root, text="Select Cipher:")
        self.cipher_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.cipher_combo = ttk.Combobox(self.root, values=self.cipher_options, state="readonly")
        self.cipher_combo.grid(row=0, column=1, padx=5, pady=5)
        self.cipher_combo.current(0)

        # Text entry
        self.text_label = ttk.Label(self.root, text="Enter Text:")
        self.text_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.text_entry = ttk.Entry(self.root, width=50)
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)

        # Key entry
        self.key_label = ttk.Label(self.root, text="Enter Key:")
        self.key_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.key_entry = ttk.Entry(self.root)
        self.key_entry.grid(row=2, column=1, padx=5, pady=5)

        # Encrypt Button
        self.encrypt_button = ttk.Button(self.root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Decrypt Button
        self.decrypt_button = ttk.Button(self.root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Result Display
        self.result_label = ttk.Label(self.root, text="Result:")
        self.result_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)

        self.result_text = tk.Text(self.root, height=5, width=50)
        self.result_text.grid(row=5, column=1, padx=5, pady=5)

    def encrypt(self):
        cipher = self.cipher_combo.get()
        text = self.text_entry.get()
        key = self.key_entry.get()

        if cipher == "Vigenere":
            result = vigenere_encrypt(text, key)
        elif cipher == "Rail Fence":
            result = encryptRailFence(text, int(key))
        elif cipher == "Caesar":
            result = caesar_encrypt(text, int(key))
        # elif cipher == "Triple DES":
        #     result = triple_des_encrypt(text.encode(), key.encode()).hex()
        elif cipher == "Triple DES":
            result = triple_des_encrypt(text.encode(), key.encode()).hex()
        elif cipher == "Triple DES":
            result = triple_des_decrypt(bytes.fromhex(text), key.encode()).decode()

        else:
            result = "Invalid cipher selected"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def decrypt(self):
        cipher = self.cipher_combo.get()
        text = self.text_entry.get()
        key = self.key_entry.get()

        if cipher == "Vigenere":
            result = vigenere_decrypt(text, key)
        elif cipher == "Rail Fence":
            result = decryptRailFence(text, int(key))
        elif cipher == "Caesar":
            result = caesar_decrypt(text, int(key))
        elif cipher == "Triple DES":
            result = triple_des_decrypt(bytes.fromhex(text), key.encode()).decode()
        else:
            result = "Invalid cipher selected"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
