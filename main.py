
from login_panel import *



all_tenats = {"jan":"123"}

root = Tk()
root.title("Panel użytkownika")
root.geometry("280x150+600+400")

app_login_panel = Login(root,all_tenats)

root.mainloop()

if app_login_panel.index_window == 1:

    root_two= Tk()
    root_two.title("Panel produktów")
    root_two.geometry("400x200")
    root_two.mainloop()









