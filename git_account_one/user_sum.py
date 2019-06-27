
class UserSum:

    def __init__(self ,main_catalog ,user ,all_purchases):

        self.main_catalog = main_catalog
        self.user = user
        self.sum_list_food = []
        self.sum_list_industrial = []
        self.all_purchases = all_purchases

    def food_count(self):

        category = self.main_catalog[self.user]["spożywcze"]
        for i in category.values():
            self.sum_list_food.append(sum(i))
        print("Suma zakupów spożywczych lokatora '{tenant}': {} zł".format(str(sum(self.sum_list_food)),tenant=self.user))


    def industrial_count(self):

        category = self.main_catalog[self.user]["przemysłowe"]
        for i in category.values():
            self.sum_list_industrial.append(sum(i))
        print("Suma zakupów przemysłowych lokatora '{tenant}': {} zł".format(str(sum(self.sum_list_industrial)),tenant=self.user))

    def all_sum(self):

        # Sumowanie wszystkich zakupow.
        shopping_list = [sum(self.sum_list_food) + sum(self.sum_list_industrial)]
        print("Koszt zakupów lokatora '{tenant}': {shopping_list} zł".format(tenant=self.user,
                                                                             shopping_list=str(sum(shopping_list))))





