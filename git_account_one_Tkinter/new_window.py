
from git_account_one_Tkinter import button_account_one

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
        product_field.grid(row=1, column=2)

        product_command = self.tk.Label(window_two, text="Produkt")
        product_command.grid(row=1, column=1)

        price_field = self.tk.Entry(window_two)
        price_field.grid(row=2, column=2)

        price_command = self.tk.Label(window_two, text="Cena")
        price_command.grid(row=2, column=1)

        product_button = button_account_one.CreateButtonsTwo(self.tk,window_two)
        product_button.add_product_button()


