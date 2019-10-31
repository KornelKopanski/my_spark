
from tkinter import *
import json

class SumCalc:

    all_shopping = {}
    _sum = []
    mid_price = None

    def read(self):

        with open("AccountSumUser.json", "r")  as my_file:
            _list= json.load(my_file)

            for i in _list:
                key = i
                value = _list[i]
                self.all_shopping[key] = value

    def write(self):

        with open("AccountSumUser.json", "w")  as my_file:
            json.dump(self.all_shopping, my_file, indent=2)

    def calc(self):

        if self.all_shopping:
            nu = 0
            for user in self.all_shopping:
                nu += 1
                for number in self.all_shopping[user]:
                    self._sum.append(self.all_shopping[user][number])

            self.mid_price =sum(self._sum)/nu

    def done(self):

        self.all_shopping.clear()
        self._sum.clear()
        self.mid_price = None
        self.read()
        self.calc()

    def show_calc_user(self,info_window):

        self.done()

        info_window.insert(END, f"ŚREDNIA CENA ZAKUPÓW NA LOKATORA: {self.mid_price}zł")
        for user in self.all_shopping:
            for sum_price_user in self.all_shopping[user]:
                if self.mid_price > self.all_shopping[user][sum_price_user]:
                    x = float(self.mid_price) - float(self.all_shopping[user][sum_price_user])
                    info_window.insert(END, f"")
                    info_window.insert(END,
                                       f"Zakupy lokatora {user} wynoszą: {self.all_shopping[user][sum_price_user]}zł")
                    info_window.insert(END,f"{user}, włóż do 'pudełka':  {x}zł ")
                elif self.mid_price < self.all_shopping[user][sum_price_user]:
                    y = float(self.all_shopping[user][sum_price_user]) - float(self.mid_price)
                    info_window.insert(END, f"")
                    info_window.insert(END,
                                       f"Zakupy lokatora {user} wynoszą: {self.all_shopping[user][sum_price_user]}zł")
                    info_window.insert(END, f"{user}, weź z 'pudełka':  {y}zł ")
                else:
                    info_window.insert(END, f"")
                    info_window.insert(END,
                                       f"Zakupy lokatora {user} wynoszą: {self.all_shopping[user][sum_price_user]}zł")
                    info_window.insert(END, f"{user}, jesteś rozliczony")




