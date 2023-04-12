# Using .pack, have the left-side labels on the interface

from tkinter import *

# Root Window
root = Tk()
root.geometry("800x300")
root.title("Sales and Stock Level System")
root.configure(bg="gold")
root.resizable(False, False)

# Comic Book Store Label
title_label = Label(root, bg="gold", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.pack(ipady=10)

super_dude_label = Label(root, bg="gold", text="Super Dude: number in stock: ",
                         font=("Arial", 16))
super_dude_label.pack(side=LEFT)
lizard_man_label = Label(root, bg="gold", text="Lizard Man: number in stock: ",
                         font=("Arial", 16))
lizard_man_label.pack(side=LEFT)
water_woman_label = Label(root, bg="gold", text="Water Woman: number in "
                                                "stock: ",
                          font=("Arial", 16))
water_woman_label.pack(side=LEFT)

# Total number of comics sold
comics_sold = Label(root, bg="gold", fg="blue", text="Comics sold today: ",
                    font=("Arial", 16))
comics_sold.pack(side=LEFT)

root.mainloop()
