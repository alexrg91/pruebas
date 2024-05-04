from tkinterweb import HtmlFrame  #import the HtmlFrame widget
import tkinter as tk  #python3

root = tk.Tk()  #create the Tkinter window

# The important part: create the html widget and attach it to the window
myhtmlframe = HtmlFrame(root)  #create HTML browser
myhtmlframe.load_html("<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/XYqpZHbfHlY?si=jebHFHdVi0JHpPzp\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe>")  #Load some HTML code
myhtmlframe.pack(fill="both", expand=True)  #attach the HtmlFrame widget to the parent window

root.mainloop()
