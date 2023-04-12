# Change the labels to .grid

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
title_label.grid(column=1, columnspan=2, row=0, rowspan=2, padx=30, pady=15)

super_dude_label = Label(root, bg="gold", text="Super Dude: number in stock: ",
                         font=("Arial", 16))
super_dude_label.grid(column=0, row=2, ipady=10)
lizard_man_label = Label(root, bg="gold", text="Lizard Man: number in stock: ",
                         font=("Arial", 16))
lizard_man_label.grid(column=0, row=3, ipady=10)
water_woman_label = Label(root, bg="gold", text="Water Woman: number in "
                                                "stock: ",
                          font=("Arial", 16))
water_woman_label.grid(column=0, row=4, ipady=10)

# Total number of comics sold
comics_sold = Label(root, bg="gold", fg="blue", text="Total Comics sold "
                                                     "today: ",
                    font=("Arial", 16))
comics_sold.grid(column=0, row=5, ipady=30)

root.mainloop()
