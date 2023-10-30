from tkinter import *
import customtkinter
import random
import array
import tkinter.messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
w = app.winfo_reqwidth()
h = app.winfo_reqheight()
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (300, 300, x, y))
#app.geometry("300x300")
app.title("MSS")

def login():
    username = ""
    password = ""
    if user_entry.get() == username and user_pass.get() == password:
        tkinter.messagebox.showinfo(title="Edukas!", message=r"Sisselogimine õnnestus! Kontode haldur ja paroolide genereerija asuvad C:\Users\Kasutaja\Desktop\Password Manager v1.0")
        app.withdraw()  
    elif user_entry.get() == username and user_pass.get() != password:
        tkinter.messagebox.showwarning(title='Probleem!',message='Sisestatud parool on vigane.')
    elif user_entry.get() != username and user_pass.get() == password:
        tkinter.messagebox.showwarning(title='Probleem!',message='Sisestatud kasutajanimi on vigane.')
    else:
        tkinter.messagebox.showerror(title="Ebaõnnestus!",message="Sisestatud andmed on vigased.")
        
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)
label = customtkinter.CTkLabel(master=frame,text='Modernne Sisselogimise Süsteem')
label.pack(pady=12,padx=10)
user_entry= customtkinter.CTkEntry(master=frame,placeholder_text="Kasutajanimi")
user_entry.pack(pady=12,padx=10)
user_pass= customtkinter.CTkEntry(master=frame,placeholder_text="Parool",show="*")
user_pass.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame,text='Logi sisse',command=login)
button.pack(pady=12,padx=10)
checkbox = customtkinter.CTkCheckBox(master=frame,text='Mäleta mind!')
checkbox.pack(pady=12,padx=10)

app.mainloop()
