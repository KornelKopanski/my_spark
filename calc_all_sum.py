
import json

class CalcAll:

    def __init__(self):

        self.all_shopping = {}
        self._sum_price = []


    def all_sum(self):

        with open("AccountOAll.json", "r")  as my_file:
            lista = json.load(my_file)

            for i in lista:
                key = i
                value = lista[i]
                self.all_shopping[key] = value

        for user in self.all_shopping:
            for category in self.all_shopping[user]:
                for product in self.all_shopping[user][category]:
                    for data in self.all_shopping[user][category][product]:
                        for info in data:
                            if info == "sum_price":
                                self._sum_price.append(data[info])
                            elif info == "weight_sum_price":
                                self._sum_price.append(data[info])
                            elif info == "all_sum_price":
                                data[info] = sum(self._sum_price)

                    self._sum_price.clear()


        with open("AccountOAll.json", "w")  as my_file:
            json.dump(self.all_shopping, my_file, indent=2)
