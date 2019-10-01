from tkinter import *
from tkinter.messagebox import *

# ramka w postaci klasy
class Login(Frame):

    def __init__(self,master,all_tenants):

        super(Login,self).__init__(master)
        self.grid(pady=20,padx=40)
        self.create_label()
        self.create_button()
        self.create_entry()
        self.login = None
        self.password = None
        self.all_tenants = all_tenants

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

    def confront_login_and_password(self):

        self.login = self.name_entry.get()
        self.password = self.password_entry.get()

        if self.login in self.all_tenants:
            if self.password == self.all_tenants[self.login]:
                showinfo("Informacja","Zalogowano poprawnie!")
            else:
                showinfo("Uwaga!", "Nie poprawne hasło!")
        else:
            showinfo("Uwaga!", "Nie poprawny login!")

    def create_button(self):

        self.login_button = Button(self, text="Zaloguj!", command=self.confront_login_and_password)
        self.login_button.grid(column=1)



