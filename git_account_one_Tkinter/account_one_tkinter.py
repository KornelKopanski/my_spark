
import tkinter as tk
from git_account_one_Tkinter import register_login_user,button_account_one
from tkinter import messagebox


root = tk.Tk()
root.title("AccountOne")
root.geometry("700x600")

user_base = {"a":{"a":"1234567"}, "b":{"b":"7"}}

app = tk.Frame(root)
app.pack()

empty_space = tk.Label(app)
empty_space.grid(row=0,column=1)

login_info = tk.Label(app,text="Imię")
login_info.grid(row=1,column=1)

password_info = tk.Label(app,text="Hasło")
password_info.grid(row=2,column=1)

login_field = tk.Entry(app)
login_field.grid(row = 1,column=2)

password_field = tk.Entry(app,show="*")
password_field.grid(row=2,column=2)

# obiekt logowania
user_login = register_login_user.Login(login_field, password_field, user_base, messagebox, root, app, tk)

# obiekt rejestracji
user_register = register_login_user.Register(login_field, password_field, user_base, messagebox, root, app, tk)

# obiekt przycisków
buttons = button_account_one.CreateButtons(user_login,user_register,tk,app)


root.mainloop()