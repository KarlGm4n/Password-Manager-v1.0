from tkinter import *
import customtkinter
from cryptography.fernet import Fernet

global service_entry

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


class MyFrame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            print("Button pressed!")

        self.label = customtkinter.CTkLabel(self, text="New account", font=("", 20))
        self.label.place(relx=0.5, rely=0.05, anchor='n')

        self.siteEntry = customtkinter.CTkEntry(self, placeholder_text="Site", width=200)
        self.siteEntry.place(relx=0.5, rely=0.2, anchor='n')

        self.usernameEntry = customtkinter.CTkEntry(self, placeholder_text="Username", width=200)
        self.usernameEntry.place(relx=0.5, rely=0.35, anchor='n')

        self.passwordEntry = customtkinter.CTkEntry(self, placeholder_text="Password", width=200, show="*")
        self.passwordEntry.place(relx=0.5, rely=0.5, anchor='n')

        self.accountButton = customtkinter.CTkButton(self, text="Add", command=add_password)
        self.accountButton.place(relx=0.5, rely=0.65, anchor='n')
        
        self.get_Button = customtkinter.CTkButton(self, text="Saa andmed", command=get_password)
        self.get_Button.place(relx=0.7, rely=0.75, anchor='n')


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def slider_event(value):
            print(value)
            
        def checkbox_event():
            for valik in valikud:
                if checkboxes[valik].get():
                    print(valik)
            
        self.label = customtkinter.CTkLabel(self, text="Password generator", font=("", 20))
        self.label.place(relx=0.5, rely=0.05, anchor='n')
        
        self.label = customtkinter.CTkLabel(self, text="Length", font=("", 18))
        self.label.place(relx=0.05, rely=0.25, anchor='w')

        self.slider = customtkinter.CTkSlider(self, from_=1, to=12, number_of_steps=12, command=slider_event)
        self.slider.place(relx=0.5, rely=0.25, anchor='w')
        
        self.label = customtkinter.CTkLabel(self, text="Complexity", font=("", 18))
        self.label.place(relx=0.05, rely=0.4, anchor='w')
        
        valikud = ['Valik1','Valik2','Valik3','Valik4']
        
        checkboxes = {}
        checkboxes["Valik1"] = customtkinter.CTkCheckBox(self, text="a-z", command=checkbox_event,
                                     onvalue="on", offvalue="off")
        checkboxes["Valik1"].place(relx=0.3, rely=0.4, anchor='w')
        checkboxes["Valik1"].deselect()
        
        checkboxes["Valik2"] = customtkinter.CTkCheckBox(self, text="A-z", command=checkbox_event,
                                     onvalue="on", offvalue="off")
        checkboxes["Valik2"].place(relx=0.45, rely=0.4, anchor='w')
        checkboxes["Valik2"].deselect()
        
        checkboxes["Valik3"] = customtkinter.CTkCheckBox(self, text="0-9", command=checkbox_event,
                                     onvalue="on", offvalue="off")
        checkboxes["Valik3"].place(relx=0.6, rely=0.4, anchor='w')
        checkboxes["Valik3"].deselect()
        
        checkboxes["Valik4"] = customtkinter.CTkCheckBox(self, text="%()=*", command=checkbox_event,
                                     onvalue="on", offvalue="off")
        checkboxes["Valik4"].place(relx=0.75, rely=0.4, anchor='w')
        checkboxes["Valik4"].deselect()


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Managed accounts", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=10)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Password Manager v1.0")
        customtkinter.set_appearance_mode("dark")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        width = 1200 # Laius 
        height = 700 # Kõrgus

        screen_width = self.winfo_screenwidth()  # Ekraani laius
        screen_height = self.winfo_screenheight() # Ekraani kõrgus

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (1200, 700, x, y)) # Tsentreerib akna

        self.my_frame1 = MyFrame1(master=self, width=550, height=310)
        self.my_frame1.grid(row=0, column=0, padx=20, pady=20)
        self.my_frame1.grid_propagate(False)

        self.my_frame2 = MyFrame2(master=self, width=550, height=310)
        self.my_frame2.grid(row=2, column=0, padx=20, pady=20)
        self.my_frame2.grid_propagate(False)

        self.scrollable_frame = ScrollableFrame(master=self, width=550, height=660)
        self.scrollable_frame.grid(row=0, column=2, rowspan=3, padx=20, pady=20)


app = App()
app.mainloop()
