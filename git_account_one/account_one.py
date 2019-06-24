

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


person_sum = user_sum.UserSum(all_purchases,tenant,food_sum,industrial_sum,all_purchases)

# Tworzę kategorię zakupów.
food_or_industrial = {"spożywcze":{},
                     "przemysłowe":{}}

elements_add = add_elements.Add_AO(all_purchases,tenant,food_or_industrial)

elements_add.add_tenant()

elements_add.more_products()

person_sum.show_info()

# Sumowanie zakupów spożywczych.
person_sum.food_count()
# Sumowanie zakupów przemysłowych.
person_sum.industrial_count()

# Sumowanie wszystkich zakupow.
shopping_list = [sum(food_sum) + sum(industrial_sum)]
print("Koszt zakupów lokatora: {tenant} = {shopping_list} zł".format(tenant=tenant,shopping_list=str(sum(shopping_list))))






