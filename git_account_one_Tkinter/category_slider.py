
from tkinter.ttk import *

class CategorySlider:

    def __init__(self,tk,window_two):

        self.window_two = window_two
        self.tk = tk
        self.you_choice_category = None

    def _command_category_slider(self):

        category_command = self.tk.Label(self.window_two, text="Kategoria")
        category_command.grid(column=2,row=2)

    def choice_category_slider(self):

        self._command_category_slider()

        category_slider = Combobox(self.window_two)
        category_slider['values'] = ("Spożywcze", "Przemysłowe")
        category_slider.current(0)  # ustawienie co ma być wartością domyślną
        category_slider.grid(column=3, row=2)
        self.you_choice_category = category_slider.get()














