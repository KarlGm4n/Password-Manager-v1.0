from tkinter import *
import customtkinter
import random
import array


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
        self.accountButton.place(relx=0.5, rely=0.65, anchor='n')


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
