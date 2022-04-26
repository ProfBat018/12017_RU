
# num = int()     # int - это тоже конструктор

# <editor-fold desc="Clicker">
# import tkinter as tk

# HEIGHT = 500
# WIDTH = 500
#
# root = tk.Tk()  # Tk - конструктор моего класса Tkinter
# root.title("Clicker")
# root.geometry(f"{WIDTH}x{HEIGHT}")
# root.resizable(False, False)
# root.config(bg='#000000')
# # bg = background
# # fg = foreground
#
# count = 0
#
#
# def click():
#     global count
#
#     count += 1
#     counter['text'] = count
#
#
# tk.Label(root, text="Welcome to CLICKER game😊", fg="#d02829", bg="#7ED0C2").pack()
# tk.Button(root, text="Click Me", command=click).pack()
#
# counter = tk.Label(root, text='0', font=("Arial", 48), fg="#d02829", bg="#7ED0C2")
# counter.place(relheight=0.3, relwidth=0.3, relx=0.35, rely=0.2)
#
#
# root.mainloop()

# </editor-fold>

# <editor-fold desc="Color picker">

from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color picker")
root.geometry("350x350")


def choose():
    result = colorchooser.askcolor()
    print(result)


red = 0
green = 0
blue = 0
hexadecimal = 0

app_title = Label(root, text="Welcome to Color-Picker", font=("Roboto", 21))
app_title.pack()

choose_color = Button(root, text="Choose", font=("Roboto", 12), command=choose)
choose_color.pack()

red_label = Label(root, text=f"Red: {red}")
red_label.pack()

green_label = Label(root, text=f"Green: {green}")
green_label.pack()

blue_label = Label(root, text=f"Blue: {blue}")
blue_label.pack()

hex_label = Label(root, text=f"Hex: {hexadecimal}")
hex_label.pack()


root.mainloop()



# </editor-fold>