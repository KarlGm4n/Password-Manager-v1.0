import customtkinter as ctk
import tkinter.messagebox as tkmb
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.geometry("300x300")
app.title("MSS")
root = tk.Tk()
def login():
    username = ""
    password = ""
    #new_window = ctk.CTkToplevel(app)
    #new_window.title("New window")
    #new_window.geometry("350x150")
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="Sisselogimine õnnestus!")
        root.destroy()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',message='Sisestatud parool on vigane.')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',message='Sisestatud kasutajanimi on vigane.')
    else:
        tkmb.showerror(title="Login Failed",message="Sisestatud andmed on vigased.")
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)
label = ctk.CTkLabel(master=frame,text='Modernne Sisselogimise Süsteem')
label.pack(pady=12,padx=10)
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Kasutajanimi")
user_entry.pack(pady=12,padx=10)
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Parool",show="*")
user_pass.pack(pady=12,padx=10)
button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)
checkbox = ctk.CTkCheckBox(master=frame,text='Mäleta mind!')
checkbox.pack(pady=12,padx=10)
app.mainloop()