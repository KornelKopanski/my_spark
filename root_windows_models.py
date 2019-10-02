

from login_and_register_model import *
from products_window_model import *

class Root_Login:

    def __init__(self,all_tenats):

        self.all_tenats = all_tenats
        self.app_login_panel = None
        self.main_login_window()

    def main_login_window(self):

        root = Tk()
        root.title("Panel użytkownika")
        root.geometry("280x150+600+400")

        self.app_login_panel = Login(root, self.all_tenats)

        root.mainloop()

class Root_Product:

    def __init__(self,all_tenats):

        self.all_tenats = all_tenats
        self.app_product_panel = None
        self.main_product_window()

    def main_product_window(self):

        root_two = Tk()
        root_two.title("Panel produktów")
        root_two.geometry("800x530")

        self.app_product_panel = Products(root_two)

        root_two.mainloop()
