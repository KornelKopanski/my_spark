


# Program zbiera dane o zakupach zrobionych przez współlokatorów,
# po czym dzieli je, na wszytkich mieszkańców.
# I sprawdza która osoba musi oddać pieniądze innym współlokatorom,
# a która sama powinna otrzymać zwrot pieniedzy.

from git_account_one import add_elements,user_sum,register_and_login,recording_and_reading
import json

# Tworzę słownik w którym będą gromadzone zakupy wszystkich współlokatorów.
all_purchases = {}
# Tworzę słownik w którym będą gromadzone dane rejestracyjne lokatorów.
register_tenants = {}

# Tworzę zmienną zawierającą sumę zakupów, wszystkich lokatorów.
sum_all_tenants = []

# opcja czyszczenia pliku.
while True:
    clear_all_purchases = input("Aby wyczyścić plik wpisz 'tak',"
                                "w przeciwnym razie wciśnij 'enter'.")
    if clear_all_purchases == "tak":
        # końcowy zapis do pliku
        with open("AccountOAll.json", "w")  as my_file:
            json.dump(all_purchases, my_file)
        break
    else:
        break

read = recording_and_reading.RecordRead(json,register_tenants,all_purchases)

# Odczyt z pliku rejestracji
read.registerAccountO()

# Odczyt z pliku
read.read_all_purchases()


# Tworzę kategorię zakupów.
food_or_industrial = None



end = ""
while end != "0":

    food_or_industrial = {"spożywcze": {},
                          "przemysłowe": {}}

    tenats = register_and_login.RegisterLoginTenant(all_purchases, food_or_industrial, register_tenants)
    tenats.login_or_register(tenats)

    elements_add = add_elements.Add_AO(all_purchases,tenats.user,food_or_industrial)

    elements_add.more_products()
    # Wypisuję wszystkie dane
    elements_add.show_info()

    end = input("Aby dodać nowego lokatora wciśnij 'enter', aby zakończyć wpisz '0'.")

recording = recording_and_reading.RecordRead(json,register_tenants,all_purchases)


# końcowy zapis do pliku
recording.recording_file()

# końcowy zapis do pliku rejestracji
recording.recording_file_register()


for user in all_purchases:

    person_sum = user_sum.UserSum(user, all_purchases)
    # Sumowanie zakupów spożywczych.
    person_sum.food_count()
    # Sumowanie zakupów przemysłowych.
    person_sum.industrial_count()
    # Sumowanie wszystkich
    person_sum.all_sum()

def mechanism_sum_tenant():
    for user in all_purchases:

        tenant_sum = user_sum.TenantSum(user,all_purchases)
        tenant_sum.tenant_food_count()
        tenant_sum.tenant_industrial_count()
        tenant_sum.tenant_all_sum()
        for i in tenant_sum.shopping_list:
            sum_all_tenants.append(i)

    # dzielenie łącznych zakupów po równo na każdego lokatora
    one_tenant = sum(sum_all_tenants) /len(all_purchases)

    for user in all_purchases:

        tenant_sum = user_sum.TenantSum(user,all_purchases)
        tenant_sum.tenant_food_count()
        tenant_sum.tenant_industrial_count()
        tenant_sum.tenant_all_sum()
        for i in tenant_sum.shopping_list:
            sum_all_tenants.append(i)

            if one_tenant > i:
                print(f"{user}, wrzuć do skarbonki {one_tenant-i} zł.\n")
            elif one_tenant < i:
                print(f"{user}, weź ze skarbonki {i - one_tenant} zł.\n")
            else:
                print(f"{user}, jesteś rozliczony!\n")
    print("----------------------------------------------------")
    print(f"Średni koszt na lokatora  wynosi = {one_tenant}")


mechanism_sum_tenant()





# from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import *
#
#
# root = Tk()
#
# root.title("AccountOne")
#
# root.geometry("600x260")
#
# app = Label(root)
# app.pack()
#
# empty_fieled = Label(app)
# empty_fieled.grid(row=0,column=1)
#
# login_command = Label(app,text="Imię")
# login_command.grid(row=1,column=1)
#
#
# password_command = Label(app,text="Hasło")
# password_command.grid(row=2,column=1)
#
# login_field = Entry(app)
# login_field.grid(row = 1,column=2)
#
#
# password_field = Entry(app)
# password_field.grid(row=2,column=2)
#
# register_tenants = {"jan": {"jan": "12345678"}, "adam": {"adam": "12345678"}, "ola": {"ola": "123456789"}}
#
#
# all_purchases = {}
#
# food_or_industrial = {"spożywcze": {},
#                           "przemysłowe": {}}
#
# def _choice_categorys(choice_category, product, price,main_catalog,user):
#     if choice_category == "Spożywcze":
#         # spozywcze
#         if product in main_catalog[user]["spożywcze"]:
#             main_catalog[user]["spożywcze"][product].append(price)
#         else:
#             main_catalog[user]["spożywcze"].setdefault(product, [price])
#     elif choice_category == "Przemysłowe":
#         # przemysłowe
#         if product in main_catalog[user]["przemysłowe"]:
#             main_catalog[user]["przemysłowe"][product].append(price)
#         else:
#             main_catalog[user]["przemysłowe"].setdefault(product, [price])
#
#
#
# def add_products(name):
#     new_window = Label(root)
#
#     kontener = Listbox(new_window,width = 100, height = 50)
#     def x():
#
#
#
#         for user in all_purchases:
#             kontener.insert(END,(f"Lokator '{user}':"))
#             for category in all_purchases[user]:
#                 kontener.insert(END,"    ",("          -{}".format(category)))
#                 for product in all_purchases[user][category]:
#                     kontener.insert(END, ("                     - {}".format(product)))
#                     for price in all_purchases[user][category][product]:
#                         kontener.insert(END,("                                - {} zł".format(price)))
#
#
#     kontener.grid(row=5, column=2)
#
#
#
#     empty_field1 = Label(new_window)
#     empty_field1.grid(row=0, column=1)
#
#     product_field = Entry(new_window)
#     product_field.grid(row = 1,column=2)
#
#
#     product_command = Label(new_window, text="Produkt")
#     product_command.grid(row=1, column=1)
#
#     price_field = Entry(new_window)
#     price_field.grid(row=2,column=2)
#
#     price_command = Label(new_window,text="Cena")
#     price_command.grid(row=2,column=1)
#
#     suwak = Combobox(new_window)
#     suwak['values'] = ("Spożywcze", "Przemysłowe")
#     suwak.current(0)  # ustawienie co ma być wartością domyślną
#     suwak.grid(column=0, row=0)
#
#     user = name
#
#     def wybor():
#         category = suwak.get()
#         produkt = product_field.get()
#         price = price_field.get()
#
#         if price.isalpha():
#             messagebox.showinfo("Informacja","Nie poprawny typ danych, wpisz cyfrę!")
#         else:
#             _choice_categorys(category,produkt,float(price),all_purchases,user)
#             x()
#
#     add_product_button = Button(new_window,text="Dodaj produkt", command=wybor)
#     add_product_button.grid(row=3,column=2)
#
#
#     new_window.pack()
#
#
#
# def login_tenant():
#
#     name = login_field.get()
#     password = password_field.get()
#
#     if name not in register_tenants:
#         messagebox.showinfo('Informacja', f"Lokator {name} nie istnieje w katalogu, wpisz poprawny nick!")
#
#     elif password != register_tenants[name][name]:
#         messagebox.showinfo('Informacja', "Twoje hasło jest niepoprawne!")
#     else:
#         all_purchases[name] = food_or_industrial
#         app.destroy()
#         add_products(name)
#
#
#
#
#
# login_button = Button(app,text="Zaloguj się",command = login_tenant)
# login_button.grid(row=3,column=2)
#
# register_button = Button(app,text="Rejestracja")
# register_button.grid(row=4,column=2)
#
#
#
# root.mainloop()
#
#
#
















