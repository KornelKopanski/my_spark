
from root_windows_models import *




all_tenants = {}

all_tenants_shopping = {}

root_login = Root_Login(all_tenants,all_tenants_shopping)



if root_login.app_login_panel.index_window == 1:

    root_product = Root_Product(all_tenants)


name = data["name_product"]

if name in all_tenants_shopping:

    data.pop("name_product")
    all_tenants_shopping[name].append(data)

else:
    all_data = data
    all_data.pop("name_product")

    all_tenants_shopping[name] = [all_data]

print(all_tenants_shopping)