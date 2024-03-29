
import json


class Calc:
    data_quantity = {}
    all_shopping = {}
    _weight = {}
    _weight_quantity = {}

    #  POMOC DO METOD LICZĄCYCH ŁĄCZNĄ CENĘ PRODUKTU
    user_price_info = {}
    segreg_user_price = {}

    def segregation_quan(self):

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                self.all_shopping[key] = value

        self.data_quantity.clear()
        self._weight.clear()
        self._weight_quantity.clear()
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

                            elif info == "weight_product":

                                if user not in self._weight_quantity:
                                    self._weight_quantity[user] = {product: [float(data[info])]}
                                else:
                                    if product not in self._weight_quantity[user]:
                                        self._weight_quantity[user][product] = [float(data[info])]
                                    else:
                                        self._weight_quantity[user][product].append(float(data[info]))

                                for index in data:
                                    if index == "price_product":

                                        sum_weight_product = float(data[index]) * float(data[info])

                                        if user not in self._weight:
                                            self._weight[user] = {product: [sum_weight_product]}
                                        else:
                                            if product not in self._weight[user]:
                                                self._weight[user][product] = [sum_weight_product]
                                            else:
                                                self._weight[user][product].append(sum_weight_product)

        # Sumowanie ceny na podstawie wagi.
        for user in self._weight:
            for product in self._weight[user]:
                _all_sum = sum(self._weight[user][product])
                for tenant in self.all_shopping:
                    if tenant == user:
                        for category in self.all_shopping[tenant]:
                            for item in self.all_shopping[tenant][category]:
                                if item == product:
                                    for data in self.all_shopping[tenant][category][item]:
                                        for i in data:
                                            if i == "weight_sum_price":
                                                data[i] = _all_sum

        # Sumowanie ilości kg.
        for user in self._weight_quantity:
            for product in self._weight_quantity[user]:
                 _all_sum = sum(self._weight_quantity[user][product])
                 for tenant in self.all_shopping:
                    if tenant == user:
                        for category in self.all_shopping[tenant]:
                            for item in self.all_shopping[tenant][category]:
                                if item == product:
                                    for data in self.all_shopping[tenant][category][item]:
                                        for i in data:
                                            if i == "weight_sum_quantity":
                                                data[i] = _all_sum

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


    # METODY LICZĄCE ŁĄCZNĄ CENĘ PRODUKTU
    def sort_the_data(self):

        self.user_price_info.clear()
        self.segreg_user_price.clear()

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                self.all_shopping[key] = value

        for user in self.all_shopping:
            self.user_price_info[user] = []
            for category in self.all_shopping[user]:
                for product in self.all_shopping[user][category]:
                    for data in self.all_shopping[user][category][product]:
                        for item in data:
                            if item == "price_product":
                                price = data[item]
                                for i in data:
                                    if i == "quantity_product":
                                        quantity = data[i]
                                        self.user_price_info[user].append({product: {"cena": price, "ilość": quantity}})

    def calc_sum_price(self):

        for user in self.user_price_info:
            self.segreg_user_price[user] = {}
            for data in self.user_price_info[user]:
                for product in data:
                    for info in data[product]:
                        if info == "cena":
                            price = data[product][info]
                            for item in data[product]:
                                if item == "ilość":
                                    quantity = data[product][item]
                                    sum_price = float(quantity) * float(price)
                                    if product not in self.segreg_user_price[user]:
                                        self.segreg_user_price[user][product] = {"suma": []}
                                        self.segreg_user_price[user][product]["suma"].append(sum_price)
                                    else:
                                        self.segreg_user_price[user][product]["suma"].append(sum_price)

    def all_sum_and_save(self):

        for user in self.segreg_user_price:
            for product in self.segreg_user_price[user]:
                for suma in self.segreg_user_price[user][product]:
                    for login in self.all_shopping:
                        if user == login:
                            for category in self.all_shopping[login]:
                                for item in self.all_shopping[login][category]:
                                    if item == product:
                                        for data in self.all_shopping[login][category][item]:
                                            for info in data:
                                                if info == "sum_price":
                                                    data[info] = sum(self.segreg_user_price[user][product][suma])

        with open("AccountOAll.json", "w")  as my_file:
            json.dump(self.all_shopping, my_file, indent=2)

    def init_calc_price(self):

        self.sort_the_data()
        self.calc_sum_price()
        self.all_sum_and_save()

