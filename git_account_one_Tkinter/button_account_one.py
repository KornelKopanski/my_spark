

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



class CreateButtonsTwo:

    def __init__(self,tk,app):

        self.tk = tk
        self.app = app
        self.product = None
        self.price = None
        self.quantity = None
        self.data = None
        self.brand = None
        self.weight = None

        self.product_field = self.tk.Entry(self.app)
        self.product_field.grid(row=3, column=3, sticky=self.tk.W)

        self.price_field = self.tk.Entry(self.app)
        self.price_field.grid(row=4, column=3, sticky=self.tk.W)

        # ilość produktów
        self.quantity_field = self.tk.Entry(self.app)
        self.quantity_field.grid(row=5, column=3, sticky=self.tk.W)

        # Data zakupu
        self.date_field = self.tk.Entry(self.app)
        self.date_field.grid(row=6, column=3, sticky=self.tk.W)

        # Marka produktu
        self.brand_field = self.tk.Entry(self.app)
        self.brand_field.grid(row=7, column=3, sticky=self.tk.W)

        # Waga
        self.weight_field = self.tk.Entry(self.app)
        self.weight_field.grid(row=8, column=3, sticky=self.tk.W)

    def add_product_button(self):

        add_product_button = self.tk.Button(self.app, text="Dodaj produkt", command = self.download)
        add_product_button.grid(row=9, column=3,sticky = self.tk.W,columnspan = 2)


    def download(self):

        self.product = self.product_field.get()
        self.price = self.price_field.get()
        self.quantity = self.quantity_field.get()
        self.data = self.date_field.get()
        self.brand = self.brand_field.get()
        self.weight = self.weight_field.get()





