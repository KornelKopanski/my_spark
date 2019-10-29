
import json

class SumCalc:

    all_shopping = {}
    _sum = []
    mid = None

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

        nu = 0
        for user in self.all_shopping:
            nu += 1
            for number in self.all_shopping[user]:
                self._sum.append(self.all_shopping[user][number])

        self.mid =sum(self._sum)/nu

    def done(self):

        self.read()
        self.calc()


s = SumCalc()
s.done()
print(s.mid)