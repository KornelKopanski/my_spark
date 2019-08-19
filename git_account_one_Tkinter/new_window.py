
from git_account_one_Tkinter import button_account_one,elelments,category_slider,add_product,account_one_tkinter

shopping = {}


class Windows:

    def __init__(self,tk,root):

        self.tk = tk
        self.root = root
        self.category = None


    def create_window(self):

        window_two = self.tk.Frame(self.root)
        window_two.pack()

        empty_field1 = self.tk.Label(window_two)
        empty_field1.grid(row=0, column=1)

        product_command = self.tk.Label(window_two, text="Produkt")
        product_command.grid(row=3, column=2,sticky = self.tk.E)

        price_command = self.tk.Label(window_two, text="Cena")
        price_command.grid(row=4, column=2,sticky = self.tk.E)

        product_button = button_account_one.CreateButtonsTwo(self.tk,window_two)
        product_button.add_product_button()

        # Etykieta na produkkty
        elements_etiquette = elelments.Elements(self.tk,self.root,window_two)
        elements_etiquette.window_for_products()

        # # Etykieta rozliczenie
        # settlement_etiquette = elelments.Elements(self.tk,self.root,window_two)
        # settlement_etiquette.window_for_settlement()

        # Pole wyboru kategorii
        ca_slider = category_slider.CategorySlider(self.tk,window_two)
        ca_slider.choice_category_slider()
        self.category = ca_slider.you_choice_category

        add = add_product.AddProduct(account_one_tkinter.user,shopping,self.category)
        add.add_product(product_button.product,self.category,product_button.price)


        quantity_command = self.tk.Label(window_two, text="Ilość")
        quantity_command.grid(row=5, column=2, sticky=self.tk.E)

        date_command = self.tk.Label(window_two, text="Data")
        date_command.grid(row=6, column=2, sticky=self.tk.E)

        brand_command = self.tk.Label(window_two, text="Marka")
        brand_command.grid(row=7, column=2, sticky=self.tk.E)

        weight_command = self.tk.Label(window_two, text="Waga")
        weight_command.grid(row=8, column=2, sticky=self.tk.E)






















