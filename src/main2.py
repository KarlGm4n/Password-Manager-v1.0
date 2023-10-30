from tkinter import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import customtkinter
import random
import array
import pyperclip            # Vajalikud moodulid
import base64
import json
import os.path


def get_kdf():
    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),        # Andmete krüpteering
        length=32,
        salt='salt'.encode(),
        iterations=390000,
    )

def save(data, password):
    password = password.encode()
    kdf = get_kdf()
    key = base64.urlsafe_b64encode(kdf.derive(password))        # Andmete salvestus
    fernet = Fernet(key)

    data = json.dumps(data)
    print(data)

    krtud = fernet.encrypt(data.encode())

    f = open("andmed.txt", "w")
    f.write(str(krtud))
    f.close()


def load(password):
    kdf = get_kdf()
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))        # Andmete kättesaamine

    f = open("andmed.txt", "r")
    krtud = f.readline()
    krtud = krtud.strip()
    krtud = krtud[2:-1]
    f.close()
    fernet = Fernet(key)
    krmata = fernet.decrypt(krtud.encode()).decode()
    krmata = json.loads(krmata)
    return krmata

data = []
password = input("Sisesta parool: ")        # Sisenemiseks parooli nõudmine
if os.path.isfile("andmed.txt"):
    try:
        data = load(password)
        print(data)
    except:
        print("Vale parool!")
        exit()

class MyFrame1(customtkinter.CTkFrame):            # Paroolide lisamise aken
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            list = []
            list.append(self.siteEntry.get())
            list.append(self.usernameEntry.get())        # Nupu funktsioon
            list.append(self.passwordEntry.get())
            app.receive(list)
            clear_entries()

        def clear_entries():
            self.siteEntry.delete(0, 'end')
            self.usernameEntry.delete(0, 'end')
            self.passwordEntry.delete(0, 'end')

        self.label = customtkinter.CTkLabel(self, text="Uue konto lisamine", font=("", 20))
        self.label.place(relx=0.5, rely=0.05, anchor='n')

        self.siteEntry = customtkinter.CTkEntry(self, placeholder_text="Keskkond", width=200)        # Pealkirjad
        self.siteEntry.place(relx=0.5, rely=0.2, anchor='n')

        self.usernameEntry = customtkinter.CTkEntry(self, placeholder_text="Kasutajatunnus", width=200)
        self.usernameEntry.place(relx=0.5, rely=0.35, anchor='n')

        self.passwordEntry = customtkinter.CTkEntry(self, placeholder_text="Salasõna", width=200, show="*")
        self.passwordEntry.place(relx=0.5, rely=0.5, anchor='n')

        self.accountButton = customtkinter.CTkButton(self, text="Lisa andmed", command=button_event)
        self.accountButton.place(relx=0.5, rely=0.65, anchor='n')


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        # Genereerija aken

        def slider_event(value):
            self.label1.configure(text=round(value))        # Liuguri töövõime

        def checkbox_event():
            List = []
            for item in varList:
                if item.get() != "":
                    List.append(item.get())        # Linnukestega kastide töövõime
            return List

        def generate():
            MAX_LEN = round(self.slider.get())
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']        # Generaator
            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
            COMBINED_LIST = []
            temp_pass = ""
            times = 0
            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            xd_pass = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
            if checkbox_event()[0] == "on":
                COMBINED_LIST.extend(LOCASE_CHARACTERS)
                temp_pass += rand_lower
            else:
                xd_pass = [x for x in xd_pass if x not in LOCASE_CHARACTERS]            # Nõuete lisamine/eemaldamine generatsioonist
                times += 1

            if checkbox_event()[1] == "on":
                COMBINED_LIST.extend(UPCASE_CHARACTERS)
                temp_pass += rand_upper
            else:
                xd_pass = [x for x in xd_pass if x not in UPCASE_CHARACTERS]
                times += 1

            if checkbox_event()[2] == "on":
                COMBINED_LIST.extend(DIGITS)
                temp_pass += rand_digit
            else:
                xd_pass = [x for x in xd_pass if x not in DIGITS]
                times += 1

            if checkbox_event()[3] == "on":
                COMBINED_LIST.extend(SYMBOLS)
                temp_pass += rand_symbol
            else:
                xd_pass = [x for x in xd_pass if x not in SYMBOLS]
                times += 1

            for x in range(times):
                temp_pass += random.choice(xd_pass)
                times -= 1
            for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)        # Eelvaate loomine
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)
            password = ""
            for x in temp_pass_list:
                password = password + x
            print(password)
            self.previewlabel.configure(text=password)
            pyperclip.copy(password)        # Kopeerib genereeritud parooli lõikelauale
            spam = pyperclip.paste()

        self.label = customtkinter.CTkLabel(self, text="Parooli generaator", font=("", 20))        # Pealkirjad
        self.label.place(relx=0.5, rely=0.05, anchor='n')

        self.label = customtkinter.CTkLabel(self, text="Pikkus:", font=("", 18))
        self.label.place(relx=0.05, rely=0.25, anchor='w')

        self.label1 = customtkinter.CTkLabel(self, text="12", font=("", 18))
        self.label1.place(relx=0.4, rely=0.25, anchor='w')

        self.slider = customtkinter.CTkSlider(self, from_=5, to=20, number_of_steps=20, command=slider_event)
        self.slider.place(relx=0.5, rely=0.25, anchor='w')

        self.label = customtkinter.CTkLabel(self, text="Keerukus:", font=("", 18))
        self.label.place(relx=0.05, rely=0.4, anchor='w')

        varList = []

        var1 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="a-z", variable=var1, command=checkbox_event,
                                     onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.3, rely=0.4, anchor='w')
        self.checkbox.deselect()

        var2 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="A-z", variable=var2, command=checkbox_event,        # Valikute kontroll
                                     onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.45, rely=0.4, anchor='w')
        self.checkbox.deselect()

        var3 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="0-9", variable=var3, command=checkbox_event,
                                     onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.6, rely=0.4, anchor='w')
        self.checkbox.deselect()

        var4 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="%()=*", variable=var4, command=checkbox_event,
                                     onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.75, rely=0.4, anchor='w')
        self.checkbox.deselect()

        varList.append(var1)
        varList.append(var2)
        varList.append(var3)
        varList.append(var4)

        self.label = customtkinter.CTkLabel(self, text="Eelvaade:", font=("", 18))
        self.label.place(relx=0.05, rely=0.55, anchor='w')

        self.previewlabel = customtkinter.CTkLabel(self, text="xdxd", font=("", 18))        # Veel pealkirju <3
        self.previewlabel.place(relx=0.5, rely=0.52, anchor='n')

        self.genbutton = customtkinter.CTkButton(self, text="Genereeri!", command=generate)
        self.genbutton.place(relx=0.5, rely=0.7, anchor='n')


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):        # Haldaja aken
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()        # Haldaja töövõime
        self.label_list = []
        self.button1_list = []
        self.button2_list = []

    def add_item(self, list):
        label = customtkinter.CTkLabel(self, text=(f"Site: {list[0]}"), compound="left", padx=5, anchor="w")        # Kontode lisamine
        button1 = customtkinter.CTkButton(self, text="Isikutunnistus", width=100, height=24)
        button2 = customtkinter.CTkButton(self, text="Eemalda", width=100, height=24)
        if self.command is not None:
            button1.configure(command=lambda button_type="Isikutunnistus": self.command(list, button_type))
            button2.configure(command=lambda button_type="Eemalda": self.command(list, button_type))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button1.grid(row=len(self.label_list), column=1, pady=(0, 10), padx=5)
        button2.grid(row=len(self.label_list), column=2, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button1_list.append(button1)
        self.button2_list.append(button2)

    def remove_item(self, list):
        for label, button1, button2 in zip(self.label_list, self.button1_list, self.button2_list):        # Kontode eemaldamine
            if list[0] in label.cget("text"):
                label.destroy()
                button1.destroy()
                button2.destroy()
                self.label_list.remove(label)
                self.button1_list.remove(button1)
                self.button2_list.remove(button2)
                return


class MyFrame4(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        # Sätete aken

        def button_event():
            new_window = customtkinter.CTkToplevel(self)        # Sätete avamine
            new_window.title("Sätted")
            new_window.geometry("300x150")

            def LightMode():
                customtkinter.set_appearance_mode("light")        # Hele variant

            def DarkMode():
                customtkinter.set_appearance_mode("dark")        # Tume variant

            light_button = customtkinter.CTkButton(new_window, text="Hele versioon", command=LightMode)        # Hele variant
            light_button.pack(pady=10)

            dark_button = customtkinter.CTkButton(new_window, text="Tume versioon", command=DarkMode)        # Tume variant
            dark_button.pack(pady=10)

        self.accountButton = customtkinter.CTkButton(self, text="Seaded", command=button_event)        # Nupu asukoht ja kujundus
        self.accountButton.place(relx=0.5, rely=0.3, anchor='n')


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        # Kõikehõlmav aken

        self.title("Password Manager v1.0")
        customtkinter.set_appearance_mode("dark")        # Tunnused
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        width = 1200        # Laius
        height = 700        # Kõrgus

        screen_width = self.winfo_screenwidth()        # Ekraani laius
        screen_height = self.winfo_screenheight()        # Ekraani kõrgus

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (1200, 700, x, y))        # Tsentreerib akna

        self.my_frame1 = MyFrame1(master=self, width=550, height=310)        # Lisamise akna kujundusparameetrid
        self.my_frame1.grid(row=0, column=0, padx=20, pady=20)
        self.my_frame1.grid_propagate(False)

        self.my_frame2 = MyFrame2(master=self, width=550, height=310)        # Genereerimise akna kujundusparameetrid
        self.my_frame2.grid(row=1, column=0, padx=20, pady=20)
        self.my_frame2.grid_propagate(False)

        self.scrollable_frame = ScrollableFrame(master=self, width=550, height=660, command=self.label_button_frame_event)        # Haldaja akna kujundusparameetrid
        self.scrollable_frame.grid(row=0, column=2, rowspan=3, padx=20, pady=20)

        self.my_frame4 = MyFrame4(master=self, width=160, height=50)        # Sätete akna kujundusparameetrid
        self.my_frame4.grid(row=2, column=0, padx=10, pady=5)
        self.my_frame4.grid_propagate(False)

        
        for list in data:
            self.scrollable_frame.add_item(list)         # Loeb iga listi andmetest ja lisab funktsioonile scrollable_frame

    
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():        # PEAKS keelama mitme seadete akna avamise
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

    def receive(self, list):
        self.scrollable_frame.add_item(list)        # Hallatavate kontode kättesaamine
        data.append(list)

    def label_button_frame_event(self, list, button_type):
        if button_type == "Isikutunnistus":
            print(f"Account credentials: username {list[1]} and password {list[2]}")        # Haldusaluste kõrval olevad nupud
        if button_type == "Eemalda":
            self.scrollable_frame.remove_item(list)
            data.remove(list)


app = App()
app.mainloop()        # Kõige töövõime
save(data, password)
