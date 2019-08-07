
from git_account_one_Tkinter import button_account_one,elelments,category_slider

class Windows:

    def __init__(self,tk,root):

        self.tk = tk
        self.root = root



    def create_window(self):

        window_two = self.tk.Frame(self.root)
        window_two.pack()

        empty_field1 = self.tk.Label(window_two)
        empty_field1.grid(row=0, column=1)

        product_field = self.tk.Entry(window_two)
        product_field.grid(row=4, column=3,sticky = self.tk.W)

        product_command = self.tk.Label(window_two, text="Produkt")
        product_command.grid(row=4, column=2,sticky = self.tk.E)

        price_field = self.tk.Entry(window_two)
        price_field.grid(row=5, column=3,sticky = self.tk.W)

        price_command = self.tk.Label(window_two, text="Cena")
        price_command.grid(row=5, column=2,sticky = self.tk.E)

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
        ca_slider.subcategory_slider(ca_slider.you_choice_category)








