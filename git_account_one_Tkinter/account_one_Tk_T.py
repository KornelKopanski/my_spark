


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import tkinter as tk


root = Tk()

root.title("AccountOne")

root.geometry("600x260")

app = Label(root)
app.pack()

empty_fieled = Label(app)
empty_fieled.grid(row=0,column=1)

login_command = Label(app,text="Imię")
login_command.grid(row=1,column=1)


password_command = Label(app,text="Hasło")
password_command.grid(row=2,column=1)

login_field = Entry(app)
login_field.grid(row = 1,column=2)


password_field = Entry(app,show="*")
password_field.grid(row=2,column=2)

register_tenants = {"jan": {"jan": "12345678"}, "adam": {"adam": "12345678"}, "ola": {"ola": "123456789"}}


all_purchases = {}

food_or_industrial = {"spożywcze": {},
                          "przemysłowe": {}}

def _choice_categorys(choice_category, product, price,main_catalog,user):
    if choice_category == "Spożywcze":
        # spozywcze
        if product in main_catalog[user]["spożywcze"]:
            main_catalog[user]["spożywcze"][product].append(price)
        else:
            main_catalog[user]["spożywcze"].setdefault(product, [price])
    elif choice_category == "Przemysłowe":
        # przemysłowe
        if product in main_catalog[user]["przemysłowe"]:
            main_catalog[user]["przemysłowe"][product].append(price)
        else:
            main_catalog[user]["przemysłowe"].setdefault(product, [price])

def x(kontener):


    kontener.delete(0,END)
    for user in all_purchases:
        kontener.insert(END,(f"Lokator '{user}':"))
        for category in all_purchases[user]:
            kontener.insert(END,"    ",("          -{}".format(category)))
            for product in all_purchases[user][category]:
                kontener.insert(END, ("                     - {}".format(product)))
                for price in all_purchases[user][category][product]:
                    kontener.insert(END,("                                - {} zł".format(price)))


def add_products(name):
    new_window = Label(root)
    new_window2 = Label(new_window)

    scroll = tk.Scrollbar(new_window2)

    kontener = Listbox(new_window2,width = 40, height = 20, yscrollcommand = scroll.set)
    scroll.pack(side = tk.RIGHT, fill = tk.Y)
    kontener.pack(side=tk.LEFT, fill=tk.BOTH)
    scroll.config(command = kontener.yview)



    new_window3 = Label(new_window)

    scroll2 = tk.Scrollbar(new_window3)

    kontener2 = Listbox(new_window3, width=40, height=20, yscrollcommand=scroll2.set)
    scroll2.pack(side=tk.RIGHT, fill=tk.Y)
    kontener2.pack(side=tk.LEFT, fill=tk.BOTH)
    scroll2.config(command=kontener2.yview)





    empty_field1 = Label(new_window)
    empty_field1.grid(row=0, column=1)

    product_field = Entry(new_window)
    product_field.grid(row = 1,column=2)


    product_command = Label(new_window, text="Produkt")
    product_command.grid(row=1, column=1)

    price_field = Entry(new_window)
    price_field.grid(row=2,column=2)

    price_command = Label(new_window,text="Cena")
    price_command.grid(row=2,column=1)

    category_slider = Combobox(new_window)
    category_slider['values'] = ("Spożywcze", "Przemysłowe")
    category_slider.current(0)  # ustawienie co ma być wartością domyślną
    category_slider.grid(column=0, row=0)

    user = name

    def you_choice_product():
        category = category_slider.get()
        produkt = product_field.get()
        price = price_field.get()

        if price.isalpha():
            messagebox.showinfo("Informacja","Nie poprawny typ danych, wpisz cyfrę!")
        else:
            _choice_categorys(category,produkt,float(price),all_purchases,user)
            x(kontener)

    add_product_button = Button(new_window,text="Dodaj produkt", command=you_choice_product)
    add_product_button.grid(row=3,column=2)


    new_window.pack()
    new_window2.grid(row=5, column=2)
    new_window3.grid(row=6,column=2)



def login_tenant():

    name = login_field.get()
    password = password_field.get()

    if name not in register_tenants:
        messagebox.showinfo('Informacja', f"Lokator {name} nie istnieje w katalogu, wpisz poprawny nick!")

    elif password != register_tenants[name][name]:
        messagebox.showinfo('Informacja', "Twoje hasło jest niepoprawne!")
    else:
        all_purchases[name] = food_or_industrial
        app.destroy()
        add_products(name)





login_button = Button(app,text="Zaloguj się",command = login_tenant)
login_button.grid(row=3,column=2)

register_button = Button(app,text="Rejestracja")
register_button.grid(row=4,column=2)



root.mainloop()



