


class RecordRead:

    def __init__(self,json,register_tenants,all_purchases):

        self.json = json
        self.register_tenants = register_tenants
        self.all_purchases = all_purchases

    # Odczyt z pliku rejestracji
    def registerAccountO(self):
        with open("registerAccountO.json","r")  as my_file:
            lista = self.json.load(my_file)

        for i in lista:
            key = i
            value = lista[i]
            self.register_tenants[key] = value

    # Odczyt z pliku
    def read_all_purchases(self):
        with open("AccountOAll.json","r")  as my_file:
            lista = self.json.load(my_file)

        for i in lista:
            key = i
            value = lista[i]
            self.all_purchases[key] = value

