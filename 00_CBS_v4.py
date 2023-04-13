# Added 03_mini_form_v3

# Import Statements
from tkinter import *

# Root Window
root = Tk()
root.geometry("800x300")
root.title("Sales and Stock Level System")
root.configure(bg="gold")
root.resizable(False, False)


# Comic Class
class Comic:
    def __init__(self, name, num_stock):
        self.name = name
        self.num_stock = num_stock
        comics.append(self)


# Generate Comics Stock
def generate_comics_stock(name):
    for comic_details in comics:
        if comic_details.name == name:
            return comic_details.num_stock


# Add the names to the comics dropdown
def comics_dropdown():
    comics_details = []
    for details in comics:
        comics_details.append(details.name)
    return comics_details


# Function to validate the entered number of comics ins an integer
def integer(entered):
    return entered.isdigit()


validation = root.register(integer)


# Sell Comics Function

# Restock Comics Function

# ******** Main Routine ********

# Necessary Lists and variables
comics = []
num_comics_sold = 0
super_dude_name = "Super Dude"
lizard_man_name = "Lizard Man"
water_woman_name = "Water Woman"


# Add Comics to Class
Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

# Labels
# Comic Book Store Title Label
title_label = Label(root, bg="gold", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=2, row=0, sticky=N, rowspan=2, padx=30,
                 pady=15)

# Comics Labels - added a number in stock
super_dude_label = Label(root, bg="gold",
                         text=f"Super Dude: number in stock: "
                              f"{generate_comics_stock(super_dude_name)}",
                         font=("Arial", 16))
super_dude_label.grid(column=0, row=2, sticky=W, ipadx=15, ipady=10)

lizard_man_label = Label(root, bg="gold",
                         text=f"Lizard Man: number in stock: "
                              f"{generate_comics_stock(lizard_man_name)}",
                         font=("Arial", 16))
lizard_man_label.grid(column=0, row=3, sticky=W, ipadx=15, ipady=10)

water_woman_label = Label(root, bg="gold",
                          text=f"Water Woman: number in stock: "
                               f"{generate_comics_stock(water_woman_name)}",
                          font=("Arial", 16))
water_woman_label.grid(column=0, row=4, sticky=W, ipadx=15, ipady=10)

# Total number of comics sold - added a number of comics sold
comics_sold = Label(root, bg="gold", fg="blue",
                    text=f"Total Comics sold today: {num_comics_sold}",
                    font=("Arial", 16, "bold"))
comics_sold.grid(column=0, row=5, sticky=W, ipadx=15, ipady=15)

# Mini Form
# Select comic title label
select_label = Label(root, bg="gold", text="Select comic title: ",
                     font=("Arial", 16))
select_label.grid(column=2, row=2, sticky=E, ipadx=10, ipady=15)

# Dropdown menu
clicked = StringVar()
comics_options = comics_dropdown()

# Initial menu text - dropdown from here
clicked.set("Select Comic...")

# Send dropdown menu to 'clicked' button - grid and font settings from
# 01_setup_interface_v5
select_dropdown = OptionMenu(root, clicked, *comics_options)
select_dropdown.config(bg="gold")
select_dropdown.grid(column=3, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics label
number_comics = Label(root, bg="gold", text="Number of comics: ",
                      font=("Arial", 16))
number_comics.grid(column=2, row=3, sticky=E, ipadx=10, ipady=15)

# Number of comics entry
comics_entry = Entry(root, validate='key',
                     validatecommand=(validation, '%S'), width=5)
comics_entry.grid(column=3, row=3, sticky=E)

# Sell Comic Button - temporarily as a label for structuring purposes
sell_comics = Label(root, bg="gold", text="Sell comics: ",
                    font=("Arial", 16))
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)

# Restock Comic Button - temporarily as a label for structuring purposes
restock_comics = Label(root, bg="gold", text="Restock comics: ",
                       font=("Arial", 16))
restock_comics.grid(column=3, row=5, sticky=W, ipadx=10, ipady=15)

root.mainloop()
