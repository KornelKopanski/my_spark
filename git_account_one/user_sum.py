
class UserSum:

    def __init__(self ,user ,all_purchases):

        self.user = user
        self.sum_list_food = []
        self.sum_list_industrial = []
        self.all_purchases = all_purchases

    def food_count(self):

        category = self.all_purchases[self.user]["spożywcze"]
        for i in category.values():
            self.sum_list_food.append(sum(i))
        print("\nSuma zakupów spożywczych lokatora '{tenant}': {} zł".format(str(sum(self.sum_list_food)),tenant=self.user[0]))


    def industrial_count(self):

        category = self.all_purchases[self.user]["przemysłowe"]
        for i in category.values():
            self.sum_list_industrial.append(sum(i))
        print("\nSuma zakupów przemysłowych lokatora '{tenant}': {} zł".format(str(sum(self.sum_list_industrial)),tenant=self.user[0]))

    def all_sum(self):

        # Sumowanie wszystkich zakupow.
        shopping_list = [sum(self.sum_list_food) + sum(self.sum_list_industrial)]
        print("\nKoszt zakupów lokatora '{tenant}': {shopping_list} zł".format(tenant=self.user[0],
                                                                             shopping_list=str(sum(shopping_list))))
        print("-------------------------------------------------------------")





