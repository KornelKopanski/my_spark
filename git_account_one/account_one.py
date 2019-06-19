





# Program zbiera dane o zakupach zrobionych przez współlokatorów,
# po czym dzieli je, na wszytkich mieszkańców.
# I sprawdza która osoba musi oddać pieniądze innym współlokatorom,
# a która sama powinna otrzymać zwrot pieniedzy.


from git_account_one import add_elements,user_sum


# Lista sumująca spozywcze.
food_sum = []

# Lista sumująca przemysłowe.
industrial_sum = []


# Tworzę słownik w którym będą gromadzone zakupy wszystkich współlokatorów.
all_purchases = {}

# Lokator jest proszony o podanie imienia, w celu przypisania w póżniejszym czasie,
# jego prywatnej listy zakupów do jego imienia.
tenant = input("Wprowadź imię: ")

# Tworzę kategorię zakupów.
food_or_industrial = {"spożywcze":{},
                     "przemysłowe":{}}



# Uruchamiam funkcję "dodaj_Lokatora".
add_elements.add_tenant(all_purchases,tenant,food_or_industrial)

#Tworzę funkcję z pętlą "while" aby móc dodać tyle produktów ilę chcę.
def more_products(all_purchases,name_tenant):

    choice = ""

    while choice != "0":

        add_elements.add_product(all_purchases, name_tenant)

        choice = input("Aby zakończyć wpisz '0' lub naciśnij 'enter' aby kontynuować!")

# Uruchamiam funkcję "more_products".
more_products(all_purchases,tenant)

# Wypisuję do konsoli zawartość katalogu głównego.
print(all_purchases)

# Sumowanie zakupów spożywczych.
user_sum.food_count(all_purchases, tenant, food_sum)
# Sumowanie zakupów przemysłowych.
user_sum.industrial_count(all_purchases,tenant,industrial_sum)

# Cala lista.
# Sumowanie wszystkich zakupow.
shopping_list = [sum(food_sum) + sum(industrial_sum)]
print("Koszt zakupów lokatora ", tenant," : ", str(sum(shopping_list)))






