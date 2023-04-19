# Making sell comics button and having it command to a function
# The function should decrease the selected comic by the number of comics sold

# Created int variables and separate labels for each comic to show the stock
# number of each comics.

from tkinter import *

# Root Window - from 01_setup_interface_v5
root = Tk()
root.geometry("800x300")
root.title("Sales and Stock Level System")
root.configure(bg="gold")
root.resizable(False, False)


# Comic Class- from 02_setup_comics_v2
class Comic:
    def __init__(self, name, num_stock):
        self.name = name
        self.num_stock = num_stock
        comics.append(self)


# Generate the number of comic stocks from 02_set_up_comics_v2
def generate_comics_stock(name):
    for comic_details in comics:
        if comic_details.name == name:
            return comic_details.num_stock


# Change number in stock function
def change(comic_name, num):
    for comic_details in comics:
        if comic_name == comic_details.name:
            comic_details.num_stock -= num

    if comic_name == "Super Dude":
        super_dude_current.set(generate_comics_stock(super_dude_name))
    elif comic_name == "Lizard Man":
        lizard_man_current.set(generate_comics_stock(lizard_man_name))
    elif comic_name == "Water Woman":
        water_woman_current.set(generate_comics_stock(water_woman_name))


# Comics List and comic details from 02_setup_comics_v2
comics = []

super_dude_name = "Super Dude"
lizard_man_name = "Lizard Man"
water_woman_name = "Water Woman"

Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

super_dude_current = IntVar()
super_dude_current.set(generate_comics_stock(super_dude_name))

lizard_man_current = IntVar()
lizard_man_current.set(generate_comics_stock(lizard_man_name))

water_woman_current = IntVar()
water_woman_current.set(generate_comics_stock(water_woman_name))


# Left-side labels from 02_setup_comics_v2
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

# Sell Comics button - grid and font settings from 01_setup_interface_v5
sell_comics = Button(root, bg="gold", text="Sell comics: ",
                     font=("Arial", 16), command=lambda: change("Super "
                                                                "Dude", 1))
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)


root.mainloop()
