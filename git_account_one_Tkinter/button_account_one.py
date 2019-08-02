
class CreateButtons:

    def __init__(self,user_login,user_register,tk,app):

        self.user_login = user_login
        self.user_register = user_register
        self.tk = tk
        self.app = app
        self._login_button()
        self._register_button()

    def _login_button(self):
        login_button = self.tk.Button(self.app, text="Zaloguj się", command=self.user_login.download_date)
        login_button.grid(row=3, column=2)

    def _register_button(self):
        register_button = self.tk.Button(self.app, text="Zarejestruj się", command=self.user_register.add_user)
        register_button.grid(row=4, column=2)
