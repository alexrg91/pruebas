import tkinter as tk
from tkinter.ttk import Scale, Label

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()


def update_value(val):
    text_var.set(val)


# default Scale style
#scale = Scale(bootstyle="info", orient="vertical", command=update_value, from_=0, to=10)
scale = tk.Scale(root, orient="vertical", command=update_value, from_=0, to=10)
scale.pack()

text_var = tk.StringVar()
text_var.set("0,1")

label = Label(root, textvariable=text_var)
label.pack()

#scale.config(state=tk.DISABLED)


def action_update():
    scale.config(state=tk.DISABLED)


# Botón para ejecutar la función
button = tk.Button(root, text="Get Scale Value", command=action_update)
button.pack(anchor="center")


root.mainloop()
