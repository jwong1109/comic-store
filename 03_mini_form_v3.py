# Only allow an integer value for the number of comics entry

# Make the entry field size smaller by setting a width of 5

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

# Comics List and comic details from 02_setup_comics_v2
comics = []

Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

# Select comic title label - from 01_setup_interface_v5
select_label = Label(root, bg="gold", text="Select comic title: ",
                     font=("Arial", 16))
select_label.grid(column=2, row=2, sticky=E, ipadx=10, ipady=15)


clicked = StringVar()
comics_options = comics_dropdown()

# Initial menu text - dropdown from here
clicked.set("Select Comic...")

# Send dropdown menu to 'clicked' button - grid and font settings from
# 01_setup_interface_v5
select_dropdown = OptionMenu(root, clicked, *comics_options)
select_dropdown.config(bg="gold")
select_dropdown.grid(column=3, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics label - from 01_setup_interface_v5
number_comics = Label(root, bg="gold", text="Number of comics: ",
                      font=("Arial", 16))
number_comics.grid(column=2, row=3, sticky=E, ipadx=10, ipady=15)

# Number of comics entry - initial grid and font settings from
# 01_setup_interface_v5, removed the ipadx and ipady
comics_entry = Entry(root, validate='key',
                     validatecommand=(validation, '%S'), width=5)
comics_entry.grid(column=3, row=3, sticky=E)


root.mainloop()
