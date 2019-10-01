from tkinter import *

# ramka w postaci klasy
class Login(Frame):

    def __init__(self,master):

        super(Login,self).__init__(master)
        self.grid(pady=20,padx=40)
        self.create_label()
        self.create_button()
        self.create_entry()

    def create_label(self):

        self.name_label = Label(self, text="Nazwa")
        self.name_label.grid(row=0,column=0)

        self.password_label =Label(self,text="Hasło")
        self.password_label.grid(row=1,column=0)

    def create_entry(self):

        self.name_entry = Entry(self)
        self.name_entry.grid(row=0,column=1)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=1,column=1)

    def create_button(self):

        self.login_button = Button(self, text="Zaloguj!")
        self.login_button.grid(column=1)



