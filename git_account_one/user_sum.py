

def food_count(main_catalog,user,sum_list):

    category = main_catalog[user]["spożywcze"]
    for i in category.values():
        sum_list.append(sum(i))
    print("Zakupy spożywcze suma: ", str(sum(sum_list)))


def industrial_count(main_catalog,user,sum_list):

    category = main_catalog[user]["przemysłowe"]
    for i in category.values():
        sum_list.append(sum(i))
    print("Zakupy przemysłowe suma: ", str(sum(sum_list)))

