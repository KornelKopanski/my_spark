



# Tworzę funkcję która doda kolejnego lokatora.
def add_tenant(main_catalog,user,category):

    # Instrukcja warunkowa "if" sprawdza czy w zbiorze głównym istnieje już lokator,
    # o loginie wprowadzonym przez użytkownika. Jeśli tak, program informuje,
    # aby zmienić login. Jeżeli taki użytkownik nie istnieje, zostanie zwrócona informacja
    # o utworzeniu nowego konta.
    if user in main_catalog:
        print("Użytkownik o nazwie: ", "'",user,"'", " istnieje już w Katalogu Głównym!")
        print("Zmień login Użytkownika!")
    else:
        print("Pomyślnie utworzono konto o nazwie: ", user,"!")

    # Używając wbudowanej metody "setdefault" dodaję nowego użytkownika.
    # Jeżeli dany użytkownik już znajduje się w głownym katalogu,
    # funkcja pozostawi go bez zmian.
    main_catalog.setdefault(user,category)


# Tworzę funkcję która umożliwi dodanie produktu do konta użytkownika,
# uwzględniając wybór kategorii.
def add_product(main_catalog,user):
    # Tworzę polecenie wyboru kategori produktu.
    print("")
    print("Wybierz kategorię produktu!")
    print("Spożywcze wpisz: '1'")
    print("Przemysłowe pwisz: '2'")
    choice_category = input()

    # Polecenie wpisania produktu oraz jego ceny.
    product = input("Produkt: ")
    price = float(input("Cena: "))

    # Używając obiektu lokatora, tworzę obiekty poszczególnych kategorii artykułów.
    groceries = main_catalog[user]["spożywcze"]
    manufactured_goods = main_catalog[user]["przemysłowe"]




    # Tworzę instrukcję warunkową "if" która zapisze produkt w kategorii,
    # która wcześniej została określona przez użytkownika.
    if choice_category == "1":
        # spozywcze
        if product in groceries:

            # Dodaję cenę produktu do produktu znajdującego się już w bazie.
            groceries[product].append(price)
        else:
            # Tworzę nowy produkt, jeśli nie istnieje jeszcze w zbiorze.
            groceries.setdefault(product, [price])

    elif choice_category == "2":
        # przemysłowe
        if product in manufactured_goods:

            # Dodaję cenę produktu do produktu znajdującego się już w bazie.
            manufactured_goods[product].append(price)
        else:
            # Tworzę nowy produkt, jeśli nie istnieje jeszcze w zbiorze.
            manufactured_goods.setdefault(product, [price])

    else:
        # Informacja o nie poprawnym wyborze.
        print("Nie poprawny wybór, wpisz: '1' lub '2'!")