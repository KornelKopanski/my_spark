
class UserSum:

    def __init__(self ,main_catalog ,user ,sum_list_food,sum_list_industrial):

        self.main_catalog = main_catalog
        self.user = user
        self.sum_list_food = sum_list_food
        self.sum_list_industrial = sum_list_industrial

    def food_count(self):

        category = self.main_catalog[self.user]["spożywcze"]
        for i in category.values():
            self.sum_list_food.append(sum(i))
        print("Zakupy spożywcze suma: ", str(sum(self.sum_list_food)))


    def industrial_count(self):

        category = self.main_catalog[self.user]["przemysłowe"]
        for i in category.values():
            self.sum_list_industrial.append(sum(i))
        print("Zakupy przemysłowe suma: ", str(sum(self.sum_list_industrial)))


