

class AddProduct:

    def __init__(self,user,shopping,category=None):

        self.shopping = shopping
        self.category = category
        self.user = user
        self.food_shopping = None
        self.industrial_shopping = None
        self.creation()

    def creation(self):

        self.shopping[self.user] = self.category
        tenant = self.shopping[self.user]

        tenant["Spożywcze"] = {}
        self.food_shopping = tenant["Spożywcze"]

        tenant["Przemysłowe"] = {}
        self.industrial_shopping =  tenant["Przemysłowe"]

    def add_product(self,product,category_window,price,mark="",quantity=1,date=""):

        data = {"price":price,"info":{"mark":mark,"quantity":quantity,"date":date}}

        if category_window == "Spożywcze":
            if product not in self.food_shopping:
                self.food_shopping[product] = []
                add = self.food_shopping[product]
                add.append(data)
            else:
                self.food_shopping[product].append(data)

        elif category_window == "Przemysłowe":
            if product not in self.industrial_shopping:
                self.industrial_shopping[product] = []
                add = self.industrial_shopping[product]
                add.append(data)
            else:
                self.industrial_shopping[product].append(data)
