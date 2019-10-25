
from login_and_register_model import *
from products_window_model import *

class Root_Login:

    def __init__(self,all_tenats,all_tenants_shoping):

        self.all_tenats = all_tenats
        self.all_tenants_shoping = all_tenants_shoping
        self.app_login_panel = None
        self.main_login_window()

    def main_login_window(self):

        root = Tk()
        root.title("Panel użytkownika")
        root.geometry("280x150+600+400")

        self.app_login_panel = Login(root, self.all_tenats,self.all_tenants_shoping)

        root.mainloop()

class Root_Product:

    def __init__(self,all_tenats=None):

        self.all_tenats = all_tenats
        self.app_product_panel = None
        self.main_product_window()

    def main_product_window(self):

        self.root_two = Tk()
        self.root_two.title("Panel produktów")
        self.root_two.geometry("800x530")

        self.app_product_panel = Products(self.root_two)


        self.root_two.mainloop()

    def root_destroy(self):

        self.root_two.destroy()


