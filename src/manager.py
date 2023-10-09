import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {}

def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        messagebox.showinfo("Õnnestus", "Andmed edukalt lisatud!")
    else:
        messagebox.showwarning("Viga", "Palun täitke kõik väljad.")

def get_password():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        messagebox.showinfo("Andmed", f"Kasutajanimi: {passwords[service]['username']}\nParool: {decrypted_password}")
    else:
        messagebox.showwarning("Viga", "Andmeid ei leitud.")
   
key = generate_key()

instructions = '''Et lisada andmed, täitke kõik väljad ning vajutage "Lisa andmed".
Andmete nägemiseks sisestage keskonna nimi ning vajutage "Saa andmed".'''
signature = "Developed by KEJ Programmeerimine"

window = tk.Tk()
window.title("Kontode Haldaja")
window.configure(bg="gray30")

window.resizable(False, False)

center_frame = tk.Frame(window, bg="gray60")
center_frame.grid(row=0, column=0, padx=10, pady=10)

instruction_label = tk.Label(center_frame, text=instructions, bg="gray60")
instruction_label.grid(row=0, column=1, padx=10, pady=5)

service_label = tk.Label(center_frame, text="Keskkond:", bg="gray60")
service_label.grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(center_frame)
service_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(center_frame, text="Kasutajanimi:", bg="gray60")
username_label.grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(center_frame)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(center_frame, text="Parool:", bg="gray60")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(center_frame, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(center_frame, text="Lisa andmed", bg="gray80", command=add_password, height=1, width=10)
add_button.grid(row=5, column=4, padx=10, pady=5)

get_button = tk.Button(center_frame, text="Saa andmed", bg="gray80", command=get_password, height=1, width=10)
get_button.grid(row=6, column=4, padx=10, pady=5)

signature_label = tk.Label(center_frame, text=signature, bg="gray60")
signature_label.grid(row=7, column=1, padx=5, pady=5)

window.mainloop()