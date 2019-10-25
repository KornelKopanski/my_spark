

from datetime import *
from save_to_dictionary import *
from calculation_data import Calc
from  product_windows import *
import json

all_shopping = {}
number_x = []

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
        self.create_show()

    def create_label(self):

        self.label_products_window = Label(self,text="Zakupy lokatorów")
        self.label_products_window.grid(row=1,column=0,pady=5,padx=60,sticky=S)

        self.label_user = Label(self,text=f"Zalogowano jako: {user_login[0]}")
        self.label_user.grid(row=1,column=1,columnspan=2)

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

    def create_listbox(self):

        self.listbox_frame = Frame(self)
        self.listbox_frame.grid(row=2,column=0,pady=1,padx=10,sticky=N,rowspan=70)

        scrollbar_product_window = Scrollbar(self.listbox_frame)

        self.main_products_window = Listbox(self.listbox_frame,width=70,height=25,yscrollcommand = scrollbar_product_window.set)
        self.main_products_window.pack(side = LEFT, fill = BOTH)

        scrollbar_product_window.pack(side=RIGHT, fill=Y)
        scrollbar_product_window.config(command=self.main_products_window.yview)

    def create_get_data(self):

        name_product = self.product_entry.get()
        quantity_product = self.quantity_spinbox.get()
        weight_product = self.weight_spinbox.get()
        price_product = self.price_entry.get()
        date_product = str(date.today())
        category_get = self.category_combobox.get()

        if name_product:
            if price_product:
                if quantity_product != "0" or weight_product != "0":

                    save(all_shopping,category_get,name_product,quantity_product,weight_product,price_product,date_product)

                    with open("AccountOAll.json", "w")  as my_file:
                        json.dump(all_shopping, my_file,indent=2)

                    calc = Calc()
                    calc.done()
                    calc.init_calc_price()
                    sum_shopping = SumAll()

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
                    sum_shopping.done()
                else:
                    showinfo("Uwaga!", "Proszę wprowadzić ilość lub wagę!")
            else:
                showinfo("Uwaga!", "Proszę wprowadzić cenę!")
        else:
            showinfo("Uwaga!","Proszę wprowadzić produkt!")

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

    def _log_out(self):

        self.master.destroy()
        number_x.append(1)

    def create_button(self):

        sum_all = SumAll()
        self.calculation_button = Button(self, text="Rozlicz lokatorów", width=32,command=sum_all.done_window)
        self.calculation_button.grid(row=11, column=1,columnspan=2,sticky=E)

        self.add_product_button = Button(self,text="Dodaj produkt",width=32,command=self.create_get_data)
        self.add_product_button.grid(row=8,column=1,columnspan=2,sticky=E)

        self.remove_product_button = Button(self,text="Usuń produkt",width=32)
        self.remove_product_button.grid(row=9,column=1,columnspan=2,sticky=E)

        product_info = InfoWindow(self.main_products_window,all_shopping)
        self.info_product_button = Button(self,text="Szczegóły produktu",width=32,command=product_info.product_info_window)
        self.info_product_button.grid(row=10,column=1,columnspan=2,sticky=E)


        self.log_out = Button(self,text=f"Wyloguj się ({user_login[0]})",width=32,command=self._log_out)
        self.log_out.grid(row=12, column=1,columnspan=2,sticky=E)

        self.exit_window = Button(self, text="Zamknij", width=32)
        self.exit_window.grid(row=13, column=1, columnspan=2, sticky=E)







