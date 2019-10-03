
from root_windows_models import *


g = []

all_tenats = {}

all_tenants_shoping = {}

root_login = Root_Login(all_tenats,all_tenants_shoping)



if root_login.app_login_panel.index_window == 1:

    root_product = Root_Product(all_tenats)
    g.append(root_product.product)


print(g)




