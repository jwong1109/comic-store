# From 01_setup_interface_v5
# Associate the number in stock for each comic stored in the comics list with
# the labels in the interface so the number in stock
# is displayed on the interface

from tkinter import *

# Root Window - from 01_setup_interface_v5
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


def generate_comics_stock(name):
    for comic_details in comics:
        if comic_details.name == name:
            return comic_details.num_stock


comics = []
num_comics_sold = 0
super_dude_name = "Super Dude"
lizard_man_name = "Lizard Man"
water_woman_name = "Water Woman"

Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

# Left-side labels from 01_setup_interface_v5 - also added a number in stock
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

# Total number of comics sold from 01_setup_interface_v5 - also added a
# number of comics sold
comics_sold = Label(root, bg="gold", fg="blue",
                    text=f"Total Comics sold today: {num_comics_sold}",
                    font=("Arial", 16, "bold"))
comics_sold.grid(column=0, row=5, sticky=W, ipadx=15, ipady=15)

root.mainloop()
