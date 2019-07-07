class RegisterLoginTenant:

    def __init__(self, main_catalog, category, register_tenants):

        self.main_catalog = main_catalog
        self.category = category
        self.register_tenants = register_tenants
        self.user = None

    def _registration_panel(self):
        while True:
            name = ""
            while not name:
                name = input("Podaj imię: ")
            if name in self.register_tenants:
                print("Lokator o podanej nazwie istnieje już w katalogu. Zmień nazwę!")
            else:
                break

        while True:
            password = input("Podaj hasło: ")
            if len(password) < 8:
                print("Hasło musi zawierać co najmniej 8 znaków!")
            else:
                break

        self.register_tenants[name] = {name: password}
        self.main_catalog[name] = self.category

    def _login_panel(self):
        while True:
            while True:
                name = ""
                while not name:
                    name = input("Podaj imię: ")
                break

            while True:
                password = input("Podaj hasło: ")
                if len(password) < 8:
                    print("Hasło musi zawierać co najmniej 8 znaków!")
                else:
                    break

            if name not in self.register_tenants:
                print(f"Lokator {name} nie istnieje w katalogu, wpisz poprawny nick!")
                continue
            else:
                if password != self.register_tenants[name][name]:
                    print("Twoje hasło jest niepoprawne!")
                else:
                    self.user = name
                    self.main_catalog[name] = self.category
                    break

    def login_or_register(self,object):

        print("Aby się zalogować wpisz '1'.\t\t\tAby dokonać rejestracji wpisz '2'.")

        choice = input()
        if choice == "1":
            object._login_panel()
        elif choice == "2":
            object._registration_panel()
            print("Należy się zalogować.")
            object._login_panel()
        else:
            print("Nie poprawny wybór, wpisz '1' lub '2'. ")





