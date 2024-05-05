from tkinter import *
from tkinter import ttk
import rsa_all

# e = 65537
# d = 1595442596643526546463176624547329073
# n = 2802855420351877757611258613427567727

root = Tk()
root.configure(background="black")
root.title("RSA Encryption and Decryption")

# formatting

def cipher():
	root.destroy()
	window = Tk()
	window.configure(background='black')
	window.title("RSA Cipher")

	left_frame = Frame(window, width=200, height=600, relief=SUNKEN, bg='black')
	left_frame.pack(side=LEFT)

	main = Frame(window, width=800, height=400, relief=SUNKEN, bg='black')
	main.pack()

	def remove():
		for widget in main.winfo_children():
			widget.destroy()

	def lab():
		text_label = Label(main, text="Enter text below: ", font=('arial', 16, "bold"), bg="black", fg="white")
		text_label.grid(row=0, column=0, padx=20, pady=20)

		scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
		text_box = Text(main, height=8, width=40, pady=10, yscrollcommand=scroll_text.set, bg='white', fg='black')
		text_box.grid(row=1, column=0, pady=1, padx=1)
		scroll_text.config(command=text_box.yview)
		scroll_text.grid(row=1, column=1, sticky='NS')


		scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
		new_text = Text(main, height=8, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='white', fg='black')
		new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
		scroll_text2.config(command=new_text.yview)
		scroll_text2.grid(row=1, column=4, sticky='NS')
		return text_box, new_text

# cipher

	def RSA_cipher(): 
		remove()

		key_label = Label(main, text="Enter e: ", font=('arial', 14), pady=15, bg='black', fg="white")
		key_label.grid(row=2, column=0)
		key_label = Label(main, text="Enter d: ", font=('arial', 14), pady=15, bg='black', fg="white")
		key_label.grid(row=2, column=1)
		key_label = Label(main, text="Enter n: ", font=('arial', 14), pady=15, bg='black', fg="white")
		key_label.grid(row=2, column=2)
		key_e = Entry(main, width=20, bg='white', fg='black')
		key_e.grid(row=3, column=0, padx=10, pady=10)
		key_d = Entry(main, width=20, bg='white', fg='black')
		key_d.grid(row=3, column=1, padx=10, pady=10)
		key_n = Entry(main, width=20, bg='white', fg='black')
		key_n.grid(row=3, column=2, padx=10, pady=10)

		text_box, new_text = lab()
		label = Label(main, text="RSA Encryption" , font=('arial', 16, "bold"),bg="black", fg="white")
		label.grid(row=0, column=1)
		
		#Add insert file/image selection
		file_type = ttk.Combobox(main)
		file_type['values'] = ("text", "image", "file")
		file_type.current(0)
		file_type.grid(row=5, column=0)
  
		def get_key():
			e = key_e.get().strip()
			if e:
				e = int(e)
                
			d = key_d.get().strip()
			if d:
				d = int(d)
			n = key_n.get().strip()
			if n:
				n = int(n)
			return (e, d, n)

		def encrypt():
			cipher_type = file_type.get()
			new_text.delete('1.0', END)
			txt = text_box.get("1.0", END).strip()
			key = get_key()
			if cipher_type == "text":
				enc_text = rsa_all.encrypt_text(txt, key)
				new_text.insert(1.0, enc_text)
			elif cipher_type == "image":
				filename = txt
				outfilename = rsa_all.encrypt_image(filename, key)
				new_text.insert(1.0, outfilename)
			else:
				filename = txt
				outfilename = rsa_all.encrypt_file(filename, key)
				new_text.insert(1.0, outfilename)
			
		enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt, bg='white', fg='black')
		enc.grid(row=0, column=2, padx=20, pady=30)

		def decrypt():
			cipher_type = file_type.get()
			txt = text_box.get("1.0", END).strip()
			new_text.delete('1.0', END)
			key = get_key()
			if cipher_type == "text":	
				dec_text = rsa_all.decrypt_text(txt, key)
				new_text.insert(1.0, dec_text)
			elif cipher_type == "image":
				filename = txt
				outfilename = rsa_all.decrypt_image(filename, key)
				new_text.insert(1.0, outfilename)
			else:
				filename = txt
				outfilename = rsa_all.decrypt_file(filename, key)
				new_text.insert(1.0, outfilename)

		dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt, bg='white', fg='black')
		dec.grid(row=0, column=3, padx=10, pady=10)
	
	btn_exit = Button(left_frame, text="Quit", padx=20, bd=10, width=10,height=2, command=window.destroy,
				  bg='white', fg="black", font=('arial', 20, 'bold'))
	btn_exit.grid(row=15, column=0)

	RSA_cipher()

cipher()

root.mainloop()