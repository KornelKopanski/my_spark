import json


class Calc:
    data_quantity = {}

    all_shopping = {}

    def segregation_quan(self):

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                self.all_shopping[key] = value

        self.data_quantity.clear()
        for user in self.all_shopping:
            for category in self.all_shopping[user]:
                for product in self.all_shopping[user][category]:
                    for data in self.all_shopping[user][category][product]:
                        for info in data:
                            if info == 'quantity_product':
                                if user not in self.data_quantity:
                                    self.data_quantity[user] = {product: [int(data[info])]}
                                else:
                                    if product not in self.data_quantity[user]:
                                        self.data_quantity[user][product] = [int(data[info])]
                                    else:
                                        self.data_quantity[user][product].append(int(data[info]))

    def assign(self):


        for user in self.data_quantity:
            for product in self.data_quantity[user]:
                for login in self.all_shopping:
                    if user == login:
                        for category in self.all_shopping[login]:
                            for item_product in self.all_shopping[login][category]:
                                if product == item_product:
                                    for data in self.all_shopping[login][category][item_product]:
                                        for info in data:
                                            if info == "sum_shopping":
                                                data[info] = sum(self.data_quantity[user][product])

        with open("AccountOAll.json", "w")  as my_file:
            json.dump(self.all_shopping, my_file, indent=2)


    def done(self):

        self.segregation_quan()
        self.assign()

