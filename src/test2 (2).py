from tkinter import *
import customtkinter

class MyFrame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            print("Content added!")

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
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        def slider_event(value):
            print(value)
            
        def checkbox_event():
            print("checkbox toggled, current value:", check_var.get())

        self.label = customtkinter.CTkLabel(self, text="Password generator", font=("", 20))
        self.label.place(relx=0.5, rely=0.05, anchor='n')
        
        self.label = customtkinter.CTkLabel(self, text="Length", font=("", 18))
        self.label.place(relx=0.05, rely=0.25, anchor='w')

        self.slider = customtkinter.CTkSlider(self, from_=1, to=12, number_of_steps=12, command=slider_event)
        self.slider.place(relx=0.5, rely=0.25, anchor='w')
        
        self.label = customtkinter.CTkLabel(self, text="Complexity", font=("", 18))
        self.label.place(relx=0.05, rely=0.4, anchor='w')
        
        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            #self.add_item(item)

        #def add_item(self, item):
            checkbox = customtkinter.CTkCheckBox(self, text=item)
            if self.command is not None:
                checkbox.configure(command=self.command)
            checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
            self.checkbox_list.append(checkbox)

        def remove_item(self, item):
            for checkbox in self.checkbox_list:
                if item == checkbox.cget("text"):
                    checkbox.destroy()
                    self.checkbox_list.remove(checkbox)
                    return
        
        check_var = customtkinter.StringVar(value="on")
        self.checkbox = customtkinter.CTkCheckBox(self, text="a-z", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.3, rely=0.4, anchor='w')
        
        self.checkbox = customtkinter.CTkCheckBox(self, text="A-z", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.45, rely=0.4, anchor='w')
        
        self.checkbox = customtkinter.CTkCheckBox(self, text="0-9", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.6, rely=0.4, anchor='w')
        
        self.checkbox = customtkinter.CTkCheckBox(self, text="%()=*", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
        self.checkbox.place(relx=0.75, rely=0.4, anchor='w')


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Managed accounts", font=("", 20))
        self.label.grid(row=0, column=0, padx=200, pady=10)

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = customtkinter.CTkLabel(self, text="Login")
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("500x400")
        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)
        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()

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

        self.my_frame2 = MyFrame2(master=self, item_list=[f"item {i}" for i in range(50)], width=550, height=310)
        #self.my_frame2.add_item("new item")
        self.my_frame2.grid(row=2, column=0, padx=20, pady=20)
        self.my_frame2.grid_propagate(False)

        self.scrollable_frame = ScrollableFrame(master=self, width=550, height=660)
        self.scrollable_frame.grid(row=0, column=2, rowspan=3, padx=20, pady=20)

app = App()
app.mainloop()