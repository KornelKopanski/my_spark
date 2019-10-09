import json

class Calc:

    _sum_info = {}

    def __init__(self,all_shopping):

        self.all_shopping = all_shopping

    def _quantity(self):

        for user in self.all_shopping:
            for category in self.all_shopping[user]:
                for product in self.all_shopping[user][category]:
                    for data in self.all_shopping[user][category][product]:
                        for info in data:
                            if info == "quantity_product":
                                if user not in self._sum_info:
                                    self._sum_info[user] = {product: [int(data[info])]}
                                else:
                                    if product in self._sum_info[user]:
                                        self._sum_info[user][product].append(int(data[info]))
                                    else:
                                        self._sum_info[user][product] = [int(data[info])]

    def _assign(self):

        for user in self.all_shopping:
            for login in self._sum_info:
                if user == login:
                    for category in self.all_shopping[user]:
                        for product in self.all_shopping[user][category]:
                            for data in self.all_shopping[user][category][product]:
                                for info in data:
                                    if info == "sum_shopping":
                                        if info in data:
                                            for quantity_product in self._sum_info[login]:
                                                if quantity_product == product:
                                                    data[info] = sum(self._sum_info[login][quantity_product])

        with open("AccountOAll.json", "w")  as my_file:
            json.dump(self.all_shopping, my_file, indent=2)

    def calc_quantity_product(self):

        self._quantity()
        self._assign()


