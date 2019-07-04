


# Program zbiera dane o zakupach zrobionych przez współlokatorów,
# po czym dzieli je, na wszytkich mieszkańców.
# I sprawdza która osoba musi oddać pieniądze innym współlokatorom,
# a która sama powinna otrzymać zwrot pieniedzy.

from git_account_one import add_elements,user_sum,register_and_login
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

# Odczyt z pliku rejestracji
def registerAccountO():
    with open("registerAccountO.json","r")  as my_file:
        lista = json.load(my_file)

    for i in lista:
        key = i
        value = lista[i]
        register_tenants[key] = value

registerAccountO()

# Odczyt z pliku
def read_all_purchases():
    with open("AccountOAll.json","r")  as my_file:
        lista = json.load(my_file)

    for i in lista:
        key = i
        value = lista[i]
        all_purchases[key] = value

read_all_purchases()

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

# końcowy zapis do pliku
with open("AccountOAll.json","w")  as my_file:
    json.dump(all_purchases,my_file)

# końcowy zapis do pliku rejestracji
with open("registerAccountO.json","w")  as my_file:
    json.dump(register_tenants,my_file)


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



mechanism_sum_tenant()

# dzielenie łącznych zakupów po równo na każdego lokatora
one_tenant = sum(sum_all_tenants)//len(all_purchases)
print(one_tenant)










