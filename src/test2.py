from tkinter import *
import customtkinter
from gui import *


class MyFrame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            print("Button pressed!")

        self.label = customtkinter.CTkLabel(self, text="New account", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=20)

        self.siteEntry = customtkinter.CTkEntry(self, placeholder_text="Site", width=200)
        self.siteEntry.grid(row=1, column=0, padx=20, pady=0)

        self.usernameEntry = customtkinter.CTkEntry(self, placeholder_text="Username", width=200)
        self.usernameEntry.grid(row=2, column=0, padx=20, pady=20)

        self.passwordEntry = customtkinter.CTkEntry(self, placeholder_text="Password", width=200)
        self.passwordEntry.grid(row=3, column=0, padx=20, pady=0)

        self.accountButton = customtkinter.CTkButton(self, text="Add", command=button_event)
        self.accountButton.grid(row=4, column=0, padx=20, pady=20)


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def slider_event(value):
            print(value)

        self.label = customtkinter.CTkLabel(self, text="Password generator", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=20)

        self.slider = customtkinter.CTkSlider(self, from_=1, to=12, number_of_steps=13, command=slider_event)
        self.slider.grid(row=1, column=0, padx=20, pady=0)


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Managed accounts", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=20)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Password Manager v1.0")
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