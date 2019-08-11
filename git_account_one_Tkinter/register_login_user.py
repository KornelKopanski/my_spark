
from git_account_one_Tkinter import new_window


class Login:

    def __init__(self,login_field,password_field,user_base,messagebox,root,app,tk):

        self.login_field = login_field
        self.password_field = password_field
        self.user_base = user_base
        self.messagebox = messagebox
        self.root = root
        self.app = app
        self.tk = tk
        self.login = None
        self.password = None
        self.user_register = None




    def _check_login(self):

        if self.login in self.user_base:
            return True
        else:
            self.messagebox.showinfo("Informacja", "Podany login nie istnieje!\n"
                                                   "Popraw login lub zarejestruj się!")

    def _check_password(self):

        if self.password == self.user_base[self.login][self.login]:
            return True
        else:
            self.messagebox.showinfo("Informacja", "Podane hasło jest nieprawidłowe!")

    def _sign_in(self):

        user = Login._check_login(self)
        password_user = Login._check_password(self)

        if user and password_user:
            return True
        else:
            return False

    def _sign_and_new_window(self):

        sign = Login._sign_in(self)

        if sign:
            # zamknięcie okna rejestracji
            self.app.destroy()

            # utworzenie okna dodawania produktów
            self.root.geometry("800x600")
            app_two = new_window.Windows(self.tk,self.root)
            app_two.create_window()



    def download_date(self):

        login = self.login_field.get()
        self.login = login

        password = self.password_field.get()
        self.password = password

        Login._sign_and_new_window(self)

class Register(Login):

    def download_date(self):

        login = self.login_field.get()
        self.login = login

        password = self.password_field.get()
        self.password = password

    def _add_user_login(self):

        Register.download_date(self)

        if self.login in self.user_base:
            self.messagebox.showinfo("Informacja", "Podany login już istnieje, zmień login!")
            return False
        else:
            return True

    def _add_user_password(self):

        if len(self.password) >= 6:
            return True
        else:
            self.messagebox.showinfo("Informacja", "Hasło jest za krótkie!\n"
                                                       "Musi zaiwerać conajmniej 6 znaków!")
            return False

    def add_user(self):

        if Register._add_user_login(self) and Register._add_user_password(self):
            # dodanie loginu
            self.user_base[self.login] = {}
            self.user_register = self.user_base[self.login]
            # dodanie hasła
            self.user_register[self.login] = self.password
            self.messagebox.showinfo("Informacja", "Proces rejestracji przebiegł pomyślnie!")





































