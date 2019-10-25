
from tkinter import *

_user_login = []

class _Panel_Login_Frame(Frame):

    def __init__(self,master):

        super(_Panel_Login_Frame,self).__init__(master)
        self.grid(pady=20, padx=40)
        self.all_tenats = None

    def create_label(self):

        self.name_label = Label(self, text="Nazwa")
        self.name_label.grid(row=0,column=0)

        self.password_label =Label(self,text="Hasło")
        self.password_label.grid(row=1,column=0)

    def create_entry(self):

        self.name_entry = Entry(self)
        self.name_entry.grid(row=0,column=1)

        self.password_entry = Entry(self,show="*")
        self.password_entry.grid(row=1,column=1)

    def create_button(self):
        self.login_button = Button(self, text="Zaloguj się!")
        self.login_button.grid(column=1, row=2)

        self.register_button = Button(self, text="Zarejestruj sie!")
        self.register_button.grid(column=1, row=3)

    def done(self):

        self.create_label()
        self.create_entry()
        self.create_button()

class Window_Panel:


    def login_window(self):

        root = Tk()
        root.title("Panel użytkownika")
        root.geometry("280x150+600+400")

        elements = _Panel_Login_Frame(root)
        elements.done()


        root.mainloop()

