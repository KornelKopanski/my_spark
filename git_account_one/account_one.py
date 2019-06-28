


# Program zbiera dane o zakupach zrobionych przez współlokatorów,
# po czym dzieli je, na wszytkich mieszkańców.
# I sprawdza która osoba musi oddać pieniądze innym współlokatorom,
# a która sama powinna otrzymać zwrot pieniedzy.

from git_account_one import add_elements,user_sum

# Tworzę słownik w którym będą gromadzone zakupy wszystkich współlokatorów.
all_purchases = {}

# Tworzę kategorię zakupów.
food_or_industrial = None

end = ""
while end != "0":

    food_or_industrial = {"spożywcze": {},
                          "przemysłowe": {}}

    tenant = add_elements.AdTenant(all_purchases, food_or_industrial)

    tenant.add_tenant()

    elements_add = add_elements.Add_AO(all_purchases,tenant.user,food_or_industrial)

    elements_add.more_products()
    # Wypisuję wszystkie dane
    elements_add.show_info()

    end = input("Aby dodać nowego lokatora wciśnij 'enter', aby zakończyć wpisz '0'.")

for user in all_purchases:

    person_sum = user_sum.UserSum(all_purchases,user, all_purchases)
    # Sumowanie zakupów spożywczych.
    person_sum.food_count()
    # Sumowanie zakupów przemysłowych.
    person_sum.industrial_count()
    # Sumowanie wszystkich
    person_sum.all_sum()








