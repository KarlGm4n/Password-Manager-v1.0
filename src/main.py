from tkinter import *
import customtkinter
import random
import array
import tkinter.messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("300x300")
app.title("MSS")

def login():
    username = ""
    password = ""
    if user_entry.get() == username and user_pass.get() == password:
        tkinter.messagebox.showinfo(title="Login Successful",message="Sisselogimine õnnestus!")
        app.withdraw()  
        main_app = App()  
        main_app.mainloop()
    elif user_entry.get() == username and user_pass.get() != password:
        tkinter.messagebox.showwarning(title='Wrong password',message='Sisestatud parool on vigane.')
    elif user_entry.get() != username and user_pass.get() == password:
        tkinter.messagebox.showwarning(title='Wrong username',message='Sisestatud kasutajanimi on vigane.')
    else:
        tkinter.messagebox.showerror(title="Login Failed",message="Sisestatud andmed on vigased.")
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)
label = customtkinter.CTkLabel(master=frame,text='Modernne Sisselogimise Süsteem')
label.pack(pady=12,padx=10)
user_entry= customtkinter.CTkEntry(master=frame,placeholder_text="Kasutajanimi")
user_entry.pack(pady=12,padx=10)
user_pass= customtkinter.CTkEntry(master=frame,placeholder_text="Parool",show="*")
user_pass.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)
checkbox = customtkinter.CTkCheckBox(master=frame,text='Mäleta mind!')
checkbox.pack(pady=12,padx=10)


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

        self.accountButton = customtkinter.CTkButton(self, text="Add", command=button_event)
        self.accountButton.place(relx=0.5, rely=0.75, anchor='n')


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def slider_event(value):
            self.label1.configure(text=round(value))
            
        def checkbox_event():
            List = []
            for item in varList:
                if item.get() != "":
                    List.append(item.get())
            return List
        
        def generate():
            MAX_LEN = round(self.slider.get())
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
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
                xd_pass = [x for x in xd_pass if x not in LOCASE_CHARACTERS]
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
                temp_pass = temp_pass + random.choice(COMBINED_LIST)
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)
            password = ""
            for x in temp_pass_list:
                password = password + x
            print(password)
            self.previewlabel.configure(text=password)
            
        self.label = customtkinter.CTkLabel(self, text="Password generator", font=("", 20))
        self.label.place(relx=0.5, rely=0.05, anchor='n')
        
        self.label = customtkinter.CTkLabel(self, text="Length:", font=("", 18))
        self.label.place(relx=0.05, rely=0.25, anchor='w')
        
        self.label1 = customtkinter.CTkLabel(self, text="12", font=("", 18))
        self.label1.place(relx=0.4, rely=0.25, anchor='w')

        self.slider = customtkinter.CTkSlider(self, from_=5, to=20, number_of_steps=20, command=slider_event)
        self.slider.place(relx=0.5, rely=0.25, anchor='w')
        
        self.label = customtkinter.CTkLabel(self, text="Complexity:", font=("", 18))
        self.label.place(relx=0.05, rely=0.4, anchor='w')
    
        varList = []
        
        var1 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="a-z", variable=var1, command=checkbox_event,
                                     onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.3, rely=0.4, anchor='w')
        self.checkbox.deselect()
        
        var2 = StringVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text="A-z", variable=var2, command=checkbox_event,
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
        
        self.label = customtkinter.CTkLabel(self, text="Preview:", font=("", 18))
        self.label.place(relx=0.05, rely=0.55, anchor='w')
        
        self.previewlabel = customtkinter.CTkLabel(self, text="xdxd", font=("", 18))
        self.previewlabel.place(relx=0.5, rely=0.52, anchor='n')
        
        self.genbutton = customtkinter.CTkButton(self, text="Generate", command=generate)
        self.genbutton.place(relx=0.5, rely=0.7, anchor='n')


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Managed accounts", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=10)
        

class MyFrame4(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            new_window = customtkinter.CTkToplevel(self)
            new_window.title("Sätted")
            new_window.geometry("300x150")
            
            def LightMode():
                customtkinter.set_appearance_mode("light")

            def DarkMode():
                customtkinter.set_appearance_mode("dark")
                
            light_button = customtkinter.CTkButton(new_window, text="Hele versioon", command=LightMode)
            light_button.pack(pady=10)

            dark_button = customtkinter.CTkButton(new_window, text="Tume versioon", command=DarkMode)
            dark_button.pack(pady=10)

        self.accountButton = customtkinter.CTkButton(self, text="Settings", command=button_event)
        self.accountButton.place(relx=0.5, rely=0.3, anchor='n')


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

        self.my_frame1 = MyFrame1(master=self, width=550, height=290)
        self.my_frame1.grid(row=0, column=0, padx=5, pady=5)
        self.my_frame1.grid_propagate(False)

        self.my_frame2 = MyFrame2(master=self, width=550, height=300)
        self.my_frame2.grid(row=1, column=0, padx=10, pady=5)
        self.my_frame2.grid_propagate(False)

        self.scrollable_frame = ScrollableFrame(master=self, width=550, height=660)
        self.scrollable_frame.grid(row=0, column=2, rowspan=3, padx=20, pady=20)
        
        self.my_frame4 = MyFrame4(master=self, width=160, height=50)
        self.my_frame4.grid(row=2, column=0, padx=10, pady=5)
        self.my_frame4.grid_propagate(False)
        
        def open_toplevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self) 
            else:
                self.toplevel_window.focus()


app.mainloop()
