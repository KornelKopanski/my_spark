
class Add_AO:

    def __init__(self ,main_catalog, user, category):

        self.main_catalog = main_catalog
        self.user = user
        self.category = category

    def _choice_categorys(self,choice_category, product, groceries, price, manufactured_goods):

        if choice_category == "1":
            # spozywcze
            if product in groceries:
                groceries[product].append(price)
            else:
                groceries.setdefault(product, [price])
        elif choice_category == "2":
            # przemysłowe
            if product in manufactured_goods:
                manufactured_goods[product].append(price)
            else:
                manufactured_goods.setdefault(product, [price])


    # Tworzę funkcję która umożliwi dodanie produktu do konta użytkownika,
    # uwzględniając wybór kategorii.
    def _add_product(self):
        print("")
        print("\t\t\t\tWybierz kategorię produktu!\n")
        print("Spożywcze wpisz: '1'\t\t\t\t\t\tPrzemysłowe wpisz: '2'")

        while True:
            choice_category = input()
            if choice_category != "1" and choice_category != "2":
                print("Nie poprawny wybór, wpisz '1' lub '2'!")
            else:
                break

        product = input("Produkt: ")

        while True:
            price = input("Cena: ")
            if price.isalpha():
                print("Nie poprawny typ danych, wpisz cyfrę!")
            else:
                break

        groceries = self.main_catalog[self.user]["spożywcze"]
        manufactured_goods = self.main_catalog[self.user]["przemysłowe"]

        Add_AO._choice_categorys(self,choice_category, product, groceries, float(price), manufactured_goods)

    # Tworzę funkcję z pętlą "while" aby móc dodać tyle produktów ilę chcę.
    def more_products(self):

        choice = ""
        while choice != "0":
            Add_AO._add_product(self)
            choice = input("Aby zakończyć wpisz '0' lub naciśnij 'enter' aby kontynuować!")

    def show_info(self):
        for user in self.main_catalog:
            print(f"Lokator '{user}':")
            for category in self.main_catalog[user]:
                print("\t\t\t\t- {}".format(category))
                for product in self.main_catalog[user][category]:
                    print("\t\t\t\t\t\t- {}".format(product))
                    for price in self.main_catalog[user][category][product]:
                        print("\t\t\t\t\t\t\t\t- {} zł".format(price))


class AdTenant:



    def __init__(self ,main_catalog, category):

        self.main_catalog = main_catalog
        self.category = category
        self.user = None

    # Tworzę funkcję która sprawdzi czy lokator którego chcę dodać,
    # jest już dodany. Jeśli nie jest zostanie dodany.
    def add_tenant(self):

        while True:
            user = input("Wprowadź imię: ")

            if user in self.main_catalog:
                print("Użytkownik o nazwie: '{user}' istnieje już w Katalogu Głównym!".format(user=user))
                print("Zmień login Użytkownika!")
            else:
                self.user = user
                self.main_catalog.setdefault(self.user, self.category)
                print("Pomyślnie utworzono konto o nazwie: {user}!".format(user=self.user))
                break

    def register(self):
        keys_tenant = []
        for you_key in self.main_catalog:
            keys_tenant.append(you_key[0])
        while True:
            user = input("Podaj nazwę użytkownika: ")
            if user in keys_tenant:
                print("Lokator o podanej nazwie już istnieje w katalogu,"
                      "zmień nazwę lokatora!")
            else:
                break

        while True:
            password = input("Podaj hasło: ")
            if len(password) < 8:
                print("Za krótkie hasło, podaj hasło!")
            else:
                break

        key_user = (user, password)
        self.main_catalog.setdefault(key_user, self.category)
        self.user = key_user



