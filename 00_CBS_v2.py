# Added 01_setup_interface_v5

# Import Statements
from tkinter import *

# Root Window
root = Tk()
root.geometry("800x300")
root.title("Sales and Stock Level System")
root.configure(bg="gold")
root.resizable(False, False)

# Comic Class

# Functions go here

# Sell Comics Function

# Restock Comics Function

# ******** Main Routine ********

# Necessary Lists

# Add Comics to Class

# Labels
# Comic Book Store Label
title_label = Label(root, bg="gold", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=2, row=0, sticky=N, rowspan=2, padx=30,
                 pady=15)

super_dude_label = Label(root, bg="gold", text="Super Dude: number in stock: ",
                         font=("Arial", 16))
super_dude_label.grid(column=0, row=2, sticky=W, ipadx=15, ipady=10)
lizard_man_label = Label(root, bg="gold", text="Lizard Man: number in stock: ",
                         font=("Arial", 16))
lizard_man_label.grid(column=0, row=3, sticky=W, ipadx=15, ipady=10)
water_woman_label = Label(root, bg="gold", text="Water Woman: number in "
                                                "stock: ",
                          font=("Arial", 16))
water_woman_label.grid(column=0, row=4, sticky=W, ipadx=15, ipady=10)

# Total number of comics sold
comics_sold = Label(root, bg="gold", fg="blue", text="Total Comics sold "
                                                     "today: ",
                    font=("Arial", 16, "bold"))
comics_sold.grid(column=0, row=5, sticky=W, ipadx=15, ipady=15)

# Select comic title label
select_label = Label(root, bg="gold", text="Select comic title: ",
                     font=("Arial", 16))
select_label.grid(column=2, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics label
number_comics = Label(root, bg="gold", text="Number of comics: ",
                      font=("Arial", 16))
number_comics.grid(column=2, row=3, sticky=E, ipadx=10, ipady=15)

# Mini Form

# Dropdown - temporarily as a label for structuring purposes
select_dropdown = Label(root, bg="gold", text="Dropdown menu ",
                        font=("Arial", 16))
select_dropdown.grid(column=3, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics entry - temporarily as a label for structuring purposes
comics_entry = Label(root, bg="gold", text="Entry field ",
                     font=("Arial", 16))
comics_entry.grid(column=3, row=3, sticky=W, ipadx=10, ipady=15)

# Sell Comic Button - temporarily as a label for structuring purposes
sell_comics = Label(root, bg="gold", text="Sell comics: ",
                    font=("Arial", 16))
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)

# Restock Comic Button - temporarily as a label for structuring purposes
restock_comics = Label(root, bg="gold", text="Restock comics: ",
                       font=("Arial", 16))
restock_comics.grid(column=3, row=5, sticky=W, ipadx=10, ipady=15)

root.mainloop()
