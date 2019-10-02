
from tkinter import *
from tkinter import ttk


class Products(Frame):

    def __init__(self,master):

        super(Products,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_listbox()
        self.create_button()
        self.create_combobox()
        self.create_entry()

    def create_label(self):

        self.label_products_window = Label(self,text="Zakupy lokatorów")
        self.label_products_window.grid(row=1,column=0,pady=5,padx=60,sticky=S)

        self.label_category = Label(self,text="Kategoria",width=10)
        self.label_category.grid(row=0,column=1,sticky=SE,rowspan=2)

        self.product_label = Label(self,text="Produkt")
        self.product_label.grid(row=2,column=1)

        self.price_label = Label(self,text="Cena")
        self.price_label.grid(row=3,column=1)

    def create_entry(self):

        self.product_entry = Entry(self,width=28)
        self.product_entry.grid(row=2,column=2)

        self.price_entry = Entry(self,width=28)
        self.price_entry.grid(row=3,column=2)

    def create_combobox(self):

        self.category_combobox = ttk.Combobox(self,values=["Spożywcze","Przemysłowe"],width=25)
        self.category_combobox.current(0)
        self.category_combobox.grid(row=0,column=2,sticky=SE,padx=10,rowspan=2)


    def create_listbox(self):

        self.main_products_window = Listbox(self,width=70,height=25)
        self.main_products_window.grid(row=2,column=0,pady=1,padx=10,sticky=N,rowspan=70)

    def create_button(self):

        self.calculation_batton = Button(self,text="Oblicz",width=30)
        self.calculation_batton.grid(row=72,column=0)