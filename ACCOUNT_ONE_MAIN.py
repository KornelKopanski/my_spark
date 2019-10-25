
from root_windows_models import *
import json

all_tenants = {}

#Odczyt danych logowania
with open("AccountOLogin.json", "r")  as my_file:
    lista = json.load(my_file)

    for i in lista:
        key = i
        value = lista[i]
        all_tenants[key] = value

all_tenants_shopping = {}

root_login = Root_Login(all_tenants,all_tenants_shopping)

if root_login.app_login_panel.index_window == 1:

    root_product = Root_Product(all_tenants)


all_tenants_shopping = all_shopping

#zapis danych logowania lokatora
with open("AccountOLogin.json","w")  as file:
    json.dump(all_tenants,file,indent=2)
