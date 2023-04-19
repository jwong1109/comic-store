# Added 04_sell_comics_v4

# Import Statements
from tkinter import *
from tkinter import messagebox

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


# Successful Message
def successful_message(successful_num, successful_name, action):
    if action == "sold":
        success = Label(root, text=f"{successful_num} {successful_name} has "
                                   f"been {action} successfully!")
        success.grid(column=2, row=4, sticky=W, ipadx=15, ipady=10)
        success.after(3000, success.destroy)


# Sell Comics Function

# Change number in stock function
def change():
    comic_name = clicked.get()
    num = comics_entry.get()
    int_num_comics = int(num)

    for comic_details in comics:
        if comic_name == comic_details.name:
            if 0 < int_num_comics <= comic_details.num_stock:
                comic_details.num_stock -= int_num_comics
                get_comics_sold = num_comics_sold.get()
                int_num_comics_sold = int(get_comics_sold)
                num_comics_sold.set(int_num_comics_sold+int_num_comics)
                successful_message(int_num_comics, comic_name, "sold")
            elif int_num_comics <= 0:
                messagebox.showerror('ERROR', 'You must enter a number of '
                                              'comics greater than zero!')
            else:
                messagebox.showerror('ERROR', 'There is not enough in stock '
                                              'to sell these comics'
                                              '. Please recheck your '
                                              'stock and try again!')

    if comic_name == "Super Dude":
        super_dude_current.set(generate_comics_stock(super_dude_name))
    elif comic_name == "Lizard Man":
        lizard_man_current.set(generate_comics_stock(lizard_man_name))
    elif comic_name == "Water Woman":
        water_woman_current.set(generate_comics_stock(water_woman_name))


# Restock Comics Function

# ******** Main Routine ********

# Necessary Lists and variables
comics = []
super_dude_name = "Super Dude"
lizard_man_name = "Lizard Man"
water_woman_name = "Water Woman"


# Add Comics to Class
Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

super_dude_current = IntVar()
super_dude_current.set(generate_comics_stock(super_dude_name))

lizard_man_current = IntVar()
lizard_man_current.set(generate_comics_stock(lizard_man_name))

water_woman_current = IntVar()
water_woman_current.set(generate_comics_stock(water_woman_name))

# Labels
# Comic Book Store Title Label
title_label = Label(root, bg="gold", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=2, row=0, sticky=N, rowspan=2, padx=30,
                 pady=15)

# Comics Labels - separated number in stock label with the comic label
super_dude_label = Label(root, bg="gold",
                         text=f"Super Dude: number in stock: ",
                         font=("Arial", 16))
super_dude_label.grid(column=0, row=2, sticky=W, ipadx=15, ipady=10)
super_dude_num = Label(root, bg="gold", textvariable=super_dude_current,
                       font=("Arial", 16))
super_dude_num.grid(column=1, row=2, sticky=W)

lizard_man_label = Label(root, bg="gold",
                         text=f"Lizard Man: number in stock: ",
                         font=("Arial", 16))
lizard_man_label.grid(column=0, row=3, sticky=W, ipadx=15, ipady=10)
lizard_man_num = Label(root, bg="gold", textvariable=lizard_man_current,
                       font=("Arial", 16))
lizard_man_num.grid(column=1, row=3, sticky=W)

water_woman_label = Label(root, bg="gold",
                          text=f"Water Woman: number in stock: ",
                          font=("Arial", 16))
water_woman_label.grid(column=0, row=4, sticky=W, ipadx=15, ipady=10)
water_woman_num = Label(root, bg="gold", textvariable=water_woman_current,
                        font=("Arial", 16))
water_woman_num.grid(column=1, row=4, sticky=W)

# Total number of comics sold from 02_setup_comics_v2
num_comics_sold = IntVar()
num_comics_sold.set(0)
comics_sold = Label(root, bg="gold", fg="blue",
                    text=f"Total Comics sold today:",
                    font=("Arial", 16, "bold"))
comics_sold.grid(column=0, row=5, sticky=W, ipadx=15, ipady=15)
comics_sold_num = Label(root, bg="gold", fg="blue",
                        textvariable=num_comics_sold,
                        font=("Arial", 16, "bold"))
comics_sold_num.grid(column=1, row=5, sticky=W)

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

# Sell Comic Button
sell_comics = Button(root, bg="gold", text="Sell comics: ",
                     font=("Arial", 16), command=change)
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)

# Restock Comic Button - temporarily as a label for structuring purposes
restock_comics = Label(root, bg="gold", text="Restock comics: ",
                       font=("Arial", 16))
restock_comics.grid(column=3, row=5, sticky=W, ipadx=10, ipady=15)

root.mainloop()
