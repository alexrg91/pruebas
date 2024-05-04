# Import tkinter and webview libraries
from tkinter import *
import webview

# define an instance of tkinter
tk = Tk()

#  size of the window where we show our website
tk.geometry("800x450")

# Open website
webview.create_window('Geeks for Geeks', 'https://youtu.be/gv2NvQJ4abY?si=63cUEMTMXGoWTm8u')
webview.start()
