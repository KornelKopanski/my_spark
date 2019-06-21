

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

person = user_sum.UserSum(all_purchases,tenant,food_sum,industrial_sum)

# Tworzę kategorię zakupów.
food_or_industrial = {"spożywcze":{},
                     "przemysłowe":{}}

add_elements.add_tenant(all_purchases,tenant,food_or_industrial)

add_elements.more_products(all_purchases,tenant)

print(all_purchases)



# Sumowanie zakupów spożywczych.
person.food_count()
# Sumowanie zakupów przemysłowych.
person.industrial_count()

# Sumowanie wszystkich zakupow.
shopping_list = [sum(food_sum) + sum(industrial_sum)]
print("Koszt zakupów lokatora ", tenant," : ", str(sum(shopping_list)))





