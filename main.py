
from root_windows_models import *

all_tenants = {}

all_tenants_shopping = {}

root_login = Root_Login(all_tenants,all_tenants_shopping)

if root_login.app_login_panel.index_window == 1:

    root_product = Root_Product(all_tenants)


login = user_login[0]
all_tenants_shopping[login] = category_shopping

print(all_tenants_shopping)