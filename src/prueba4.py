from tkinter.ttk import Scale, Label

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()



# default Scale style
scale = Scale(bootstyle="info", orient="vertical")
scale.pack()

label = Label()

root.mainloop()
