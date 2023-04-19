# Making sell comics button and having it command to a function
# The function should decrease the selected comic by the number of comics sold

# For this first version, only use Super Dude and make Super Dude
# decrease by 1 when the button is pressed.

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


# Comics List and comic details from 02_setup_comics_v2
comics = []

super_dude_name = "Super Dude"
Comic("Super Dude", 8)

super_dude_current = IntVar()
super_dude_current.set(generate_comics_stock(super_dude_name))

# Super Dude label from 02_setup_comics_v2
super_dude_label = Label(root, bg="gold",
                         text=f"Super Dude: number in stock: ",
                         font=("Arial", 16))
super_dude_label.grid(column=0, row=2, sticky=W, ipadx=15, ipady=10)
super_dude_num = Label(root, bg="gold", textvariable=super_dude_current,
                       font=("Arial", 16))
super_dude_num.grid(column=1, row=2, sticky=W)

# Sell Comics button - grid and font settings from 01_setup_interface_v5
sell_comics = Button(root, bg="gold", text="Sell comics: ",
                     font=("Arial", 16), command=lambda: change("Super "
                                                                "Dude", 1))
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)


root.mainloop()
