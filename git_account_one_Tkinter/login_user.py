

class Login:

    def __init__(self,login_field,password_field,user_base,messagebox):

        self.login = login_field.get()
        self.password = password_field.get()
        self.user_base = user_base
        self.messagebox = messagebox

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

    def sign_in(self):

        login = Login._check_login(self)
        password = Login._check_password(self)

        if login and password:
            return True
        else:
            return False













