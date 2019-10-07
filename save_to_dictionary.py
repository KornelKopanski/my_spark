

def save(category,name_product,category_shopping,quantity_product,weight_product,price_product,date_product):
    if category == "Spożywcze":
        if name_product not in category_shopping["Spożywcze"]:
            category_shopping["Spożywcze"][name_product] = [{"quantity_product": quantity_product,
                                                             "weight_product": weight_product,
                                                             "price_product": price_product,
                                                             "date_product": date_product}]
        else:
            category_shopping["Spożywcze"][name_product].append({"quantity_product": quantity_product,
                                                                 "weight_product": weight_product,
                                                                 "price_product": price_product,
                                                                 "date_product": date_product})
    else:
        if name_product not in category_shopping["Spożywcze"]:
            category_shopping["Przemysłowe"][name_product] = [{"quantity_product": quantity_product,
                                                               "weight_product": weight_product,
                                                               "price_product": price_product,
                                                               "date_product": date_product}]
        else:
            category_shopping["Przemysłowe"][name_product].append({"quantity_product": quantity_product,
                                                                   "weight_product": weight_product,
                                                                   "price_product": price_product,
                                                                   "date_product": date_product})








