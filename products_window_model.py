
from tkinter import *
from tkinter import ttk
from datetime import *


class Products(Frame):

    def __init__(self,master):

        super(Products,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_listbox()
        self.create_button()
        self.create_combobox()
        self.create_entry()
        self.create_spinbox()

    def create_label(self):

        self.label_products_window = Label(self,text="Zakupy lokatorów")
        self.label_products_window.grid(row=1,column=0,pady=5,padx=60,sticky=S)

        self.label_category = Label(self,text="Kategoria",width=10)
        self.label_category.grid(row=2,column=1)

        self.product_label = Label(self,text="Produkt")
        self.product_label.grid(row=3,column=1)

        self.price_label = Label(self,text="Cena")
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

    def create_button(self):

        self.calculation_batton = Button(self, text="Oblicz", width=30)
        self.calculation_batton.grid(row=72, column=0)

        self.add_product_button = Button(self,text="Dodaj produkt",width=32)
        self.add_product_button.grid(row=8,column=1,columnspan=2,sticky=E)

        self.remove_product_button = Button(self,text="Usuń produkt",width=32)
        self.remove_product_button.grid(row=9,column=1,columnspan=2,sticky=E)

    def create_combobox(self):

        self.category_combobox = ttk.Combobox(self,values=["Spożywcze","Przemysłowe"],width=25)
        self.category_combobox.current(0)
        self.category_combobox.grid(row=2,column=2)

    def create_listbox(self):

        self.main_products_window = Listbox(self,width=70,height=25)
        self.main_products_window.grid(row=2,column=0,pady=1,padx=10,sticky=N,rowspan=70)

