# Making sell comics button and having it command to a function
# The function should decrease the selected comic by the number of comics sold

# Add the mini form and when the button is pressed, the selected comic will
# decrease by the number of comics sold

# Add the number of comics sold to the total number for the day

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


# Add the names to the comics dropdown - from 03_mini_form_v3
def comics_dropdown():
    comics_details = []
    for details in comics:
        comics_details.append(details.name)
    return comics_details


# Generate the number of comic stocks from 02_set_up_comics_v2
def generate_comics_stock(name):
    for comic_details in comics:
        if comic_details.name == name:
            return comic_details.num_stock


# Change number in stock function
def change():
    comic_name = clicked.get()
    num = comics_entry.get()
    int_num_comics = int(num)

    for comic_details in comics:
        if comic_name == comic_details.name:
            comic_details.num_stock -= int_num_comics

    if comic_name == "Super Dude":
        super_dude_current.set(generate_comics_stock(super_dude_name))
    elif comic_name == "Lizard Man":
        lizard_man_current.set(generate_comics_stock(lizard_man_name))
    elif comic_name == "Water Woman":
        water_woman_current.set(generate_comics_stock(water_woman_name))

    get_comics_sold = num_comics_sold.get()
    int_num_comics_sold = int(get_comics_sold)
    num_comics_sold.set(int_num_comics_sold+int_num_comics)


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

# From 03_mini_form_v3
clicked = StringVar()
comics_options = comics_dropdown()

# Initial menu text - dropdown from here
clicked.set("Select Comic...")

# Send dropdown menu to 'clicked' button from 03_min_form_v3
select_dropdown = OptionMenu(root, clicked, *comics_options)
select_dropdown.config(bg="gold")
select_dropdown.grid(column=3, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics entry - from 03_min_form_v2
comics_entry = Entry(root)
comics_entry.grid(column=3, row=3, sticky=W)

# Sell Comics button - grid and font settings from 01_setup_interface_v5
sell_comics = Button(root, bg="gold", text="Sell comics: ",
                     font=("Arial", 16), command=change)
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)

root.mainloop()
