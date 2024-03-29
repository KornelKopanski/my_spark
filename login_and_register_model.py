from tkinter import *
from tkinter.messagebox import *
import json

category = {"Spożywcze":{},
            "Przemysłowe":{}}

user_login = []

class Login(Frame):

    def __init__(self,master,all_tenants,all_tenants_shoping,index_window=0):

        super(Login,self).__init__(master)
        self.grid(pady=20,padx=40)
        self.create_label()
        self.create_button()
        self.create_entry()
        self.login = None
        self.password = None
        self.master = master
        self.all_tenants = all_tenants
        self.index_window = index_window
        self.all_tenants_shoping = all_tenants_shoping

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
        user_login.clear()
        user_login.append(self.login)

        if self.login in self.all_tenants:
            if self.password == self.all_tenants[self.login]:
                self.index_window += 1
                self.master.destroy()

                with open("AccountOAll.json", "r")  as my_file:
                    lista = json.load(my_file)
                    for i in lista:
                        key = i
                        value = lista[i]
                        self.all_tenants_shoping[key] = value

                if self.login not in self.all_tenants_shoping:

                    self.all_tenants_shoping[self.login] = category

                    with open("AccountOAll.json", "w")  as my_file:
                        json.dump(self.all_tenants_shoping, my_file,indent=2)

            else:
                showinfo("Uwaga!", "Nie poprawne hasło!")
        else:
            showinfo("Uwaga!", "Nie poprawny login!\nPopraw login lub zarejestruj się!")

    def register_user(self):

        self.login = self.name_entry.get()
        self.password = self.password_entry.get()

        if self.login in self.all_tenants:
            showinfo("Uwaga!", "Podany login istnieje, zmień login!")
        else:
            if self.password:
                self.all_tenants[self.login] = self.password
                showinfo("Informacja", "Rejestracja przbiegła pomyślnie!\nNależy się zalogować!")
            else:
                showinfo("Uwaga!", "Proszę wprowadzić hasło!")

    def create_button(self):

        self.login_button = Button(self, text="Zaloguj się!", command=self.confront_login_and_password)
        self.login_button.grid(column=1,row=2)

        self.register_button = Button(self, text="Zarejestruj sie!", command=self.register_user)
        self.register_button.grid(column=1,row=3)




