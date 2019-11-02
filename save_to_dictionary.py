
from login_and_register_model import user_login
import json


def save(all_shopping, category_get, name_product, quantity_product,
         weight_product, price_product, date_product):

    login = user_login[0]

    with open("AccountOAll.json", "r")  as my_file:
        lista = json.load(my_file)

        for i in lista:
            key = i
            value = lista[i]
            all_shopping[key] = value

    if category_get == "Spożywcze":
        if name_product not in all_shopping[login]["Spożywcze"]:
            all_shopping[login]["Spożywcze"][name_product] = [{"quantity_product": quantity_product,
                                                                    "weight_product": weight_product,
                                                                    "price_product": price_product,
                                                                    "date_product": date_product},{"sum_shopping":{}},
                                                              {"sum_price":None},{"weight":None}]
        else:
            all_shopping[login]["Spożywcze"][name_product].append({"quantity_product": quantity_product,
                                                                        "weight_product": weight_product,
                                                                        "price_product": price_product,
                                                                        "date_product": date_product})
    elif category_get == "Przemysłowe":
        if name_product not in all_shopping[login]["Przemysłowe"]:
            all_shopping[login]["Przemysłowe"][name_product] = [{"quantity_product": quantity_product,
                                                                      "weight_product": weight_product,
                                                                      "price_product": price_product,
                                                                      "date_product": date_product},{"sum_shopping":{}},
                                                                {"sum_price":None},{"weight":None}]
        else:
            all_shopping[login]["Przemysłowe"][name_product].append({"quantity_product": quantity_product,
                                                                          "weight_product": weight_product,
                                                                          "price_product": price_product,
                                                                          "date_product": date_product})




