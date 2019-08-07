
from tkinter.ttk import *

class CategorySlider:

    def __init__(self,category=None):

        self.category = category


    def choice_category_slider(self,window_two):

        category_slider = Combobox(window_two)
        category_slider['values'] = ("Spożywcze", "Przemysłowe")
        category_slider.current(0)  # ustawienie co ma być wartością domyślną
        category_slider.grid(column=3, row=2)
