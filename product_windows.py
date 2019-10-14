
from tkinter import *
from tkinter import ttk

class InfoWindow:

    def __init__(self,main_products_window,all_shopping):

        self.main_products_window = main_products_window
        self.all_shopping = all_shopping

    def product_info_window(self):  # dodatkowe okno

        info_product = self.main_products_window.get("active")

        tenant = []

        for user in self.all_shopping:
            tenant.append(user)

        Toplevel = Tk()

        Toplevel.geometry("379x470")
        Toplevel.title("Szczegóły o produkcie")

        app = Frame(Toplevel)
        app.grid(pady=5,padx=5)

        app_listbox = Frame(app)
        app_listbox.grid(row=2,column=0,pady=3,padx=3)

        user_combobox = ttk.Combobox(app, values=tenant, width=30)
        user_combobox.current(0)
        user_combobox.grid(row=0, column=0,pady=3,padx=3)

        category_combobox = ttk.Combobox(app, values=["Spożywcze","Przemysłowe"], width=30)
        category_combobox.current(0)
        category_combobox.grid(row=1, column=0,pady=3,padx=3)

        products_button = Button(app, text="Pokaż produkty", width=30)
        products_button.grid(row=3, column=0,pady=3,padx=3)

        product_info_button = Button(app, text="Szczegóły produktu", width=30)
        product_info_button.grid(row=4, column=0,pady=3,padx=3)

        all_products_info_button = Button(app, text="Szczegóły wszystkich produktów", width=30)
        all_products_info_button.grid(row=5, column=0,pady=3,padx=3)

        sb_info_window = Scrollbar(app_listbox)

        info_window = Listbox(app_listbox, width=57, height=19,yscrollcommand = sb_info_window.set)
        info_window.pack(side = LEFT, fill = BOTH)


        sb_info_window.config(command=info_window.yview)
        sb_info_window.pack(side=RIGHT, fill=Y)

        Toplevel.mainloop()
