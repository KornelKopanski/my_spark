

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

    def _check_login(self):

        if self.login in self.user_base:
            return True
        else:
            self.messagebox.showinfo("Informacja", "Podany login nie istnieje!")

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


    def _sign_and_window(self):

        sign = Login._sign_in(self)

        if sign:
            self.app.destroy()
            app_two = self.tk.Frame(self.root)
            app_two.pack()

    def download(self):

        login = self.login_field.get()
        self.login = login

        password = self.password_field.get()
        self.password = password

        Login._sign_and_window(self)















