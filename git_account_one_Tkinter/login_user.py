

class Login:

    def __init__(self,login_field,password_field,user_base,messagebox,root,app,tk):

        self.login = login_field
        self.password = password_field
        self.user_base = user_base
        self.messagebox = messagebox
        self.root = root
        self.app = app
        self.tk = tk

    def _check_login(self):

        if self.login in self.user_base:
            self.messagebox.showinfo("Informacja", "ok!")
            return True
        else:
            self.messagebox.showinfo("Informacja", "Podany login nie istnieje!")

    def _check_password(self):

        if self.password == self.user_base[self.login][self.login]:
            return True
        else:
            self.messagebox.showinfo("Informacja", "Podane hasło jest nieprawidłowe!")

    def _sign_in(self):

        Login._check_login(self)
        Login._check_password(self)

        login = Login._check_login(self)
        password = Login._check_password(self)

        if login and password:
            return True
        else:
            return False

    def signed_successfully(self):

        Login._sign_in(self)

        sign = Login._sign_in(self)

        if sign:
            self.app.destroy()
            app_two = self.tk.Frame(self.root)
            app_two.pack()


class Download:

    def __init__(self,login_field):

        self.login_field = login_field
        self.logi = None

    def log(self):
        login = self.login_field.get()
        self.logi = login
        print(self.logi)














