
from login_panel import *



all_tenats = {"jan":"123"}

root = Tk()
root.title("Panel logowania")
root.geometry("280x150+600+400")

app_login_panel = Login(root,all_tenats)


root.mainloop()

print(app_login_panel.password)

