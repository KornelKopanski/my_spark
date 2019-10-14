
from tkinter import *
from tkinter import ttk
from datetime import *
from save_to_dictionary import *
from calculation_data import Calc
import json

all_shopping = {}

class Products(Frame):

    def __init__(self,master=None):

        super(Products,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_listbox()
        self.create_button()
        self.create_combobox()
        self.create_entry()
        self.create_spinbox()
        self.create_scrollbar()
        self.create_show()

    def create_label(self):

        self.label_products_window = Label(self,text="Zakupy lokatorów")
        self.label_products_window.grid(row=1,column=0,pady=5,padx=60,sticky=S)

        self.label_category = Label(self,text="Kategoria",width=10)
        self.label_category.grid(row=2,column=1)

        self.product_label = Label(self,text="Produkt")
        self.product_label.grid(row=3,column=1)

        self.price_label = Label(self,text="Cena(szt/kg)")
        self.price_label.grid(row=4,column=1)

        self.quantity_label = Label(self,text="Ilość(szt.)")
        self.quantity_label.grid(row=5,column=1)

        self.weight_label = Label(self,text="Waga(kg)")
        self.weight_label.grid(row=6,column=1)

        self.date_purchase_label = Label(self,text="Data")
        self.date_purchase_label.grid(row=7,column=1)

        date_today = str(date.today())
        self.date_info = Label(self, width=24,text=date_today,bg="white")
        self.date_info.grid(row=7, column=2)

    def create_spinbox(self):

        value = IntVar()

        self.quantity_spinbox = Spinbox(self,from_ = 0,to=10000, textvariable = value,width=26)
        self.quantity_spinbox.grid(row=5,column=2)

        value_two = IntVar()

        self.weight_spinbox = Spinbox(self,from_ = 0,to = 10000, textvariable = value_two, width=26)
        self.weight_spinbox.grid(row=6,column=2)

    def create_entry(self):

        self.product_entry = Entry(self,width=28)
        self.product_entry.grid(row=3,column=2)

        self.price_entry = Entry(self,width=28)
        self.price_entry.grid(row=4,column=2)


    def create_combobox(self):

        self.category_combobox = ttk.Combobox(self,values=["Spożywcze","Przemysłowe"],width=25)
        self.category_combobox.current(0)
        self.category_combobox.grid(row=2,column=2)

    def create_scrollbar(self):

        self.scrollbar_product_window = Scrollbar(self)
        self.scrollbar_product_window.place(in_ = self.main_products_window, relx = 1., rely = 0, relheight = 1.)
        self.scrollbar_product_window.config(command = self.main_products_window.yview)

    def create_listbox(self):

        self.main_products_window = Listbox(self,width=70,height=25)
        self.main_products_window.grid(row=2,column=0,pady=1,padx=10,sticky=N,rowspan=70)

    def create_get_data(self):

        name_product = self.product_entry.get()
        quantity_product = self.quantity_spinbox.get()
        weight_product = self.weight_spinbox.get()
        price_product = self.price_entry.get()
        date_product = str(date.today())
        category_get = self.category_combobox.get()

        save(all_shopping,category_get,name_product,quantity_product,weight_product,price_product,date_product)

        with open("AccountOAll.json", "w")  as my_file:
            json.dump(all_shopping, my_file,indent=2)

        calc = Calc()
        calc.done()
        calc.init_calc_price()

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                all_shopping[key] = value

        self.main_products_window.delete(0, END)
        for user in all_shopping:
            self.main_products_window.insert(END, f"Zakupy lokatora {user}:")
            for category_product in all_shopping[user]:
                self.main_products_window.insert(END, f"                                      {category_product}:")
                for product in all_shopping[user][category_product]:
                    self.main_products_window.insert(END, f"                                                              {product}")
                    for data in all_shopping[user][category_product][product]:
                        for item in data:
                            if item == "sum_shopping":
                                self.main_products_window.insert(END,
                                                                 f"                                                                        "
                                                                 f"      Ilość sztuk: {str(data[item])}")
                            for info in data:
                                if info == "sum_price":
                                    self.main_products_window.insert(END,
                                                                     f"                                                                        "
                                                                     f"      Łączna cena(zł): {str(data[info])}")

    def create_show(self):

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                all_shopping[key] = value

        self.main_products_window.delete(0, END)
        for user in all_shopping:
            self.main_products_window.insert(END, f"Zakupy lokatora {user}:")
            for category_product in all_shopping[user]:
                self.main_products_window.insert(END, f"                                      {category_product}:")
                for product in all_shopping[user][category_product]:
                    self.main_products_window.insert(END,
                                                     f"                                                            {product}")
                    for data in all_shopping[user][category_product][product]:
                        for item in data:
                            if item == "sum_shopping":
                                self.main_products_window.insert(END,
                                                                 f"                                                                        "
                                                                 f"      Ilość sztuk: {str(data[item])}")
                            for info in data:
                                if info == "sum_price":
                                    self.main_products_window.insert(END,
                                                                     f"                                                                        "
                                                                     f"      Łączna cena(zł): {str(data[info])}")

    def product_info_window(self):  # dodatkowe okno
        Toplevel = Tk()

        Toplevel.geometry("350x300")
        Toplevel.title("Informacje o produkcie")

        app = Frame(Toplevel)
        app.pack()

        info_window = Listbox(app, width=57, height=19)
        info_window.pack()

        Toplevel.mainloop()

    def create_button(self):

        self.calculation_batton = Button(self, text="Oblicz", width=30)
        self.calculation_batton.grid(row=72, column=0)

        self.add_product_button = Button(self,text="Dodaj produkt",width=32,command=self.create_get_data)
        self.add_product_button.grid(row=8,column=1,columnspan=2,sticky=E)

        self.remove_product_button = Button(self,text="Usuń produkt",width=32)
        self.remove_product_button.grid(row=9,column=1,columnspan=2,sticky=E)

        self.info_product_button = Button(self,text="Szczegóły produktu",width=32,command=self.product_info_window)
        self.info_product_button.grid(row=10,column=1,columnspan=2,sticky=E)







