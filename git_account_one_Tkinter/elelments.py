
class Elements:

    def __init__(self,tk,root,window):

        self.window = window
        self.tk = tk
        self.root = root

    def _contaneir_products(self,etiquette):


        scroll = self.tk.Scrollbar(etiquette)

        contaneir = self.tk.Listbox(etiquette, width=60, height=20, yscrollcommand=scroll.set)
        scroll.pack(side=self.tk.RIGHT, fill=self.tk.Y)
        contaneir.pack(side=self.tk.LEFT, fill=self.tk.BOTH)
        scroll.config(command=contaneir.yview)

    def window_for_products(self):

        etiquette = self.tk.Label(self.window)
        etiquette.grid(row=5, column=1)

        Elements._contaneir_products(self,etiquette)

    def window_for_settlement(self):

        etiquette = self.tk.Label(self.window)
        etiquette.grid(row=5, column=2)

        Elements._contaneir_products(self, etiquette)

