import customtkinter as ctk
import tkinter

from string import  ascii_lowercase, ascii_uppercase, digits, punctuation

from PIL import Image

import password

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Password Generator")
        self.resizable(False, False)
        self.iconphoto(False, tkinter.PhotoImage(file='img/preview.png'))

        self.logo = ctk.CTkImage(dark_image=Image.open("img/preview.png"), size=(200, 132))
        self.logo_label = ctk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = ctk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.button_generate = ctk.CTkButton(master=self.password_frame, text="Generate", width=100, command=self.set_password)

        self.button_generate.grid(row=0, column=1)

        self.settings_frame = ctk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length = ctk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        self.password_length.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")
        

        self.password_length_entry = ctk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = ctk.CTkCheckBox(master=self.settings_frame, text="0-9", variable= self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)


        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = ctk.CTkCheckBox(master=self.settings_frame, text="a-z", variable= self.cb_lower_var, onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = ctk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable= self.cb_upper_var, onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = ctk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable= self.cb_symbol_var, onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master=self.settings_frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        # default settings
        self.password_length.set(8)
        self.password_length_entry.insert(0, 8)
        self.appearance_mode_option_menu.set("System")
        self.cb_digits_var.set(digits)
        self.cb_digits.select(1)



    def change_appearance_mode_event(self, new_appearance_mode):
        # смена темы
        ctk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        # слайдер
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        # чекбоксы
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbol_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_entry.get()), characters=self.get_characters()))




if __name__ == '__main__':
    app = App()
    app.mainloop()

