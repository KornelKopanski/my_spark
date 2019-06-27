


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

# Tworzę kategorię zakupów.
food_or_industrial = None


end = ""
while end != "0":

    # Tworzę kategorię zakupów.
    food_or_industrial = {"spożywcze": {},
                          "przemysłowe": {}}

    tenant = add_elements.AdTenant(all_purchases, food_or_industrial)

    tenant.add_tenant()

    person_sum = user_sum.UserSum(all_purchases,tenant.user,food_sum,industrial_sum,all_purchases)

    elements_add = add_elements.Add_AO(all_purchases,tenant.user,food_or_industrial)

    elements_add.more_products()

    person_sum.show_info()

    # Sumowanie zakupów spożywczych.
    person_sum.food_count()
    # Sumowanie zakupów przemysłowych.
    person_sum.industrial_count()

    # Sumowanie wszystkich zakupow.
    shopping_list = [sum(food_sum) + sum(industrial_sum)]
    print("Koszt zakupów lokatora '{tenant}': {shopping_list} zł".format(tenant=tenant.user,shopping_list=str(sum(shopping_list))))

    end = input("Aby zakonczyc wpisz '0' w przeciwnym razie wciśnij 'enter'.")






