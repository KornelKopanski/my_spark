
from tkinter import *
from tkinter import ttk
from login_and_register_model import user_login

class InfoWindow:

    def __init__(self,main_products_window,all_shopping):

        self.main_products_window = main_products_window
        self.all_shopping = all_shopping
        self.index = None

    def product_info_window(self):  # dodatkowe okno


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

        self.check_index(tenant)
        self.user_combobox = ttk.Combobox(app, values=tenant, width=30)
        self.user_combobox.current(self.index)
        self.user_combobox.grid(row=0, column=0,pady=3,padx=3)


        self.category_combobox = ttk.Combobox(app, values=["Spożywcze","Przemysłowe","Wszystkie"], width=30)
        self.category_combobox.current(2)
        self.category_combobox.grid(row=1, column=0,pady=3,padx=3)

        products_button = Button(app, text="Pokaż produkty", width=30,command=self.show_products)
        products_button.grid(row=3, column=0,pady=3,padx=3)

        product_info_button = Button(app, text="Szczegóły produktu", width=30,command = self.product_details)
        product_info_button.grid(row=4, column=0,pady=3,padx=3)

        all_products_info_button = Button(app, text="Szczegóły wszystkich produktów", width=30)
        all_products_info_button.grid(row=5, column=0,pady=3,padx=3)

        sb_info_window = Scrollbar(app_listbox)

        self.info_window = Listbox(app_listbox, width=57, height=19,yscrollcommand = sb_info_window.set)
        self.info_window.pack(side = LEFT, fill = BOTH)


        sb_info_window.config(command=self.info_window.yview)
        sb_info_window.pack(side=RIGHT, fill=Y)

        self.show_products()

        Toplevel.mainloop()

    def show_products(self):

        login = self.user_combobox.get()

        category_get = self.category_combobox.get()

        self.info_window.delete(0, END)
        for user in self.all_shopping:
            if user == login:
                for category in self.all_shopping[user]:
                    if category == category_get:
                        self.info_window.insert(END, f"{category}:")
                        for product in self.all_shopping[user][category]:
                            self.info_window.insert(END,f"                     {product}")
                if category_get == "Wszystkie":
                    for categor in self.all_shopping[user]:
                        self.info_window.insert(END,f"{categor}:")
                        for item in self.all_shopping[user][categor]:
                            self.info_window.insert(END, f"                     {item}")

    def check_index(self,tenant):

        number = -1

        for i in tenant:
            number += 1
            if i == user_login[0]:
                self.index = number

    def product_details(self):

        produc = self.info_window.get("active")
        tenant = self.user_combobox.get()
        category_get = self.category_combobox.get()


        product = produc.strip()

        self.info_window.delete(0, END)
        for user in self.all_shopping:
            if user == tenant:
                for category in self.all_shopping[user]:
                    if category == category_get:
                        self.info_window.insert(END,category)
                        for item in self.all_shopping[user][category]:
                            if item == product:
                                self.info_window.insert(END,f"                  {item}")
                                for data in self.all_shopping[user][category][item]:
                                    for info in data:
                                        if info == "date_product":
                                            self.info_window.insert(END,f"")
                                            self.info_window.insert(END,f"                          Data zakupu: {data[info]}")
                                            self.info_window.insert(END, f"")
                                            for i in data:
                                                if i == "quantity_product":
                                                    if i != "0":
                                                        self.info_window.insert(END,f"                                              Ilość(szt.): {data[i]}")
                                            for i in data:
                                                if i == "weight_product":
                                                    if i != "0":
                                                        self.info_window.insert(END, f"                                             Waga(kg): {data[i]}")
                                            for i in data:
                                                if i == "price_product":
                                                    self.info_window.insert(END, f"                                             Cena za (szt/kg): {data[i]}zł")











