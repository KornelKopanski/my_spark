
class UserSum:

    def __init__(self ,main_catalog ,user ,sum_list_food,sum_list_industrial,all_purchases):

        self.main_catalog = main_catalog
        self.user = user
        self.sum_list_food = sum_list_food
        self.sum_list_industrial = sum_list_industrial
        self.all_purchases = all_purchases

    def food_count(self):

        category = self.main_catalog[self.user]["spożywcze"]
        for i in category.values():
            self.sum_list_food.append(sum(i))
        print("Zakupy spożywcze suma: {} zł".format(str(sum(self.sum_list_food))))


    def industrial_count(self):

        category = self.main_catalog[self.user]["przemysłowe"]
        for i in category.values():
            self.sum_list_industrial.append(sum(i))
        print("Zakupy przemysłowe suma: {} zł".format(str(sum(self.sum_list_industrial))))

    def show_info(self):
        for user in self.all_purchases:
            print(f"Lokator '{user}':")
            for category in self.all_purchases[user]:
                print("\t\t\t\t- {}".format(category))
                for product in self.all_purchases[user][category]:
                    print("\t\t\t\t\t\t- {}".format(product))
                    for price in self.all_purchases[user][category][product]:
                        print("\t\t\t\t\t\t\t\t- {} zł".format(price))




