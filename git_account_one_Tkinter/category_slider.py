
from tkinter.ttk import *

class CategorySlider:

    def __init__(self,tk,window_two):

        self.window_two = window_two
        self.tk = tk
        self.you_choice_category = None

    def _command_category_slider(self):

        category_command = self.tk.Label(self.window_two, text="Kategoria")
        category_command.grid(column=2,row=2)

    def _command_subcategory_slider(self):

        category_command = self.tk.Label(self.window_two, text="Rodzaj")
        category_command.grid(column=2,row=3)

    def choice_category_slider(self):

        CategorySlider._command_category_slider(self)

        category_slider = Combobox(self.window_two)
        category_slider['values'] = ("Spożywcze", "Przemysłowe")
        category_slider.current(0)  # ustawienie co ma być wartością domyślną
        category_slider.grid(column=3, row=2)
        self.you_choice_category = category_slider.get()


    def subcategory_slider(self,you_choice_category):

        CategorySlider._command_subcategory_slider(self)

        subcategory_slider = Combobox(self.window_two)

        if you_choice_category == "Spożywcze":

            subcategory_slider['values'] = ("Nabiał", "Pieczywo")

        elif you_choice_category == "Przemysłowe":
            subcategory_slider['values'] = ("Kosmetyki", "Płyny")


        subcategory_slider.current(0)  # ustawienie co ma być wartością domyślną
        subcategory_slider.grid(column=3, row=3)










