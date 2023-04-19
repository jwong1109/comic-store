# Resetting the mini-form after sell and restock button pushed
# Apply the maximum 10 to the selling part of the form too
# Commenting the program


from tkinter import *
from tkinter import messagebox

# Root Window
root = Tk()
root.geometry("800x300")  # Screen size 800px width, 300px height
root.title("Sales and Stock Level System")  # Title of the Window
root.configure(bg="gold")  # Background of the colour gold
root.resizable(False, False)  # Cannot resize the window


# Comic Class
class Comic:
    def __init__(self, name, num_stock):
        self.name = name
        self.num_stock = num_stock
        comics.append(self)  # add these details into the comics list


# Generate Comics Stock
def generate_comics_stock(name):  # generate the number of comics stock
    # based on the comic name given
    for comic_details in comics:  # for each comic_details in all the comics
        if comic_details.name == name:  # if the name of comic_details
            # matches the comic name given
            return comic_details.num_stock  # return the number of comics
            # associated with the comic name


# Add the names to the comics dropdown
def comics_dropdown():
    comics_details = []  # List to contain each comic name
    for details in comics:  # for each comic
        comics_details.append(details.name)  # add its name to the comic
        # details list
    return comics_details  # return the comic details list


# Function to validate the entered number of comics ins an integer
def integer(entered):
    return entered.isdigit()  # Use isdigit to only allow integers


validation = root.register(integer)  # validate the integer


# Create a successful message based on the successful action, comic name,
# and number of stock change
def successful_message(successful_num, successful_name, action):
    success = Label(root, text=f"{successful_num} {successful_name} "
                               f"{action} successfully!", font=("Arial", 16,
                                                                "bold"))
    success.grid(column=2, row=4, sticky=W+E)
    success.after(3000, success.destroy)


# Change number in stock function for both sell and restock
def change(action):
    # get the comic name chosen from the clicked dropdown
    comic_name = clicked.get()
    num = comics_entry.get()  # get the number from the comic entry field
    int_num_comics = int(num)  # convert the 'string' number into an integer

    if int_num_comics <= 0:  # if the number of comics is less than zero
        # Open an error message asking for comics greater than zero
        messagebox.showerror('ERROR', 'You must enter a '
                                      'number of comics greater than zero!')
        return None  # to stop the function
    # If the number of comics is beyond the 10 max limit, open an
    # error message, only allowing for a max of 10
    elif int_num_comics > 10:
        messagebox.showerror(f'10 {action} MAX',
                             f'You are only allowed to {action} a '
                             'maximum of 10 comics per round!')
        return None  # to stop the function
    for comic_details in comics:  # in each comic
        # if the comic name matches the name of the comic in the list
        if comic_name == comic_details.name:
            # Selling comics
            if action == "Sell":  # If the function was called to sell
                # if there's enough in stock for the number of comics to be
                # sold
                if int_num_comics <= comic_details.num_stock:
                    # decrease the number in stock by the sold number of comic
                    comic_details.num_stock -= int_num_comics
                    # get the current number of comics sold
                    get_comics_sold = num_comics_sold.get()
                    # convert the 'string' number of comics sold to integer
                    int_num_comics_sold = int(get_comics_sold)
                    # add the amount of comics sold in the round to the
                    # current amount of comics sold today
                    num_comics_sold.set(int_num_comics_sold+int_num_comics)
                    # create a successful message to show the comics have
                    # been sold successfully
                    successful_message(int_num_comics, comic_name, "sold")
                # If there's not enough in stock for the number of comics to
                # be sold
                else:
                    # Open an error message notifying users of insufficient
                    # stock and ask them to recheck their stocks
                    messagebox.showerror('ERROR', 'There is not enough '
                                                  'in stock '
                                                  f'to sell {int_num_comics} '
                                                  f'{comic_name}. '
                                                  f'Please recheck '
                                                  f'{comic_name}  '
                                                  'stock and try again!')
            # Restocking comics
            else:  # if the function was called to restock
                comic_details.num_stock += int_num_comics  # add restock
                # amount to the current amount of stock
                # create a successful message to show the comics have
                # been restocked successfully
                successful_message(int_num_comics, comic_name, "restocked")

    if comic_name == super_dude_name:  # if comic name chosen is Super Dude
        # update the current stock of Super Dude to the updated stored number
        # of Super Dude comics
        super_dude_current.set(generate_comics_stock(super_dude_name))
    elif comic_name == lizard_man_name:  # if comic name chosen is Lizard Man
        # update the current stock of Lizard Man to the updated stored number
        # of Lizard Man comics
        lizard_man_current.set(generate_comics_stock(lizard_man_name))
    elif comic_name == water_woman_name:  # if comic name chosen is Water Woman
        # update the current stock of Water Woman to the updated stored number
        # of Water Woman comics
        water_woman_current.set(generate_comics_stock(water_woman_name))

    clicked.set("Select Comic...")  # Reset comics dropdown
    comics_entry.delete(0, END)  # Reset number of comics entry field


# ******** Main Routine ********

# Necessary Lists and variables
comics = []  # Comics list to store all the details from the Comics class
# Variables for each comic name
super_dude_name = "Super Dude"
lizard_man_name = "Lizard Man"
water_woman_name = "Water Woman"


# Add Comics to Class
Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

# Making the current amount of Super Dude comics an integer variable
super_dude_current = IntVar()
# Set the current amount of Super Dude from the generate comics stock
# function based on the name of Super Dude
super_dude_current.set(generate_comics_stock(super_dude_name))

# Making the current amount of Lizard Man comics an integer variable
lizard_man_current = IntVar()
# Set the current amount of Lizard Man from the generate comics stock
# function based on the name of Lizard Man
lizard_man_current.set(generate_comics_stock(lizard_man_name))

# Making the current amount of Water Woman comics an integer variable
water_woman_current = IntVar()
# Set the current amount of Water Woman from the generate comics stock
# function based on the name of Water Woman
water_woman_current.set(generate_comics_stock(water_woman_name))

# Labels
# Comic Book Store Title Label
title_label = Label(root, bg="gold", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=2, row=0, sticky=N, rowspan=2, padx=30,
                 pady=15)

# Comics Labels - separated number in stock label with the comic name label
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

# Total number of comics sold
# Making the number of comics sold an integer variable
num_comics_sold = IntVar()
num_comics_sold.set(0)  # Setting the number of comics sold to zero
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
clicked = StringVar()  # Setting the dropdown to a string variable
comics_options = comics_dropdown()  # list of the name of comics

# Initial menu text - dropdown from here
clicked.set("Select Comic...")

# Send dropdown menu to 'clicked' button - grid and font settings from
# 01_setup_interface_v5
# Lists out the options for the name of comics
select_dropdown = OptionMenu(root, clicked, *comics_options)
select_dropdown.config(bg="gold")
select_dropdown.grid(column=3, row=2, sticky=E, ipadx=10, ipady=15)

# Number of comics label
number_comics = Label(root, bg="gold", text="Number of comics (max 10): ",
                      font=("Arial", 16))
number_comics.grid(column=2, row=3, sticky=E, ipadx=10, ipady=15)

# Number of comics entry - validates the entry, only allowing integer input
# to appear in the entry field
comics_entry = Entry(root, validate='key',
                     validatecommand=(validation, '%S'), width=5)
comics_entry.grid(column=3, row=3, sticky=E)

# Sell Comic Button - calls the change stock function with the action to sell
sell_comics = Button(root, bg="gold", text="Sell comics: ",
                     font=("Arial", 16), command=lambda: change("Sell"))
sell_comics.grid(column=2, row=5, sticky=E, padx=15, ipady=15)

# Restock Comic Button - calls the change function with the action to restock
restock_comics = Button(root, bg="gold", text="Restock comics: ",
                        font=("Arial", 16), command=lambda: change("Restock"))
restock_comics.grid(column=3, row=5, sticky=W, ipadx=10, ipady=15)

root.mainloop()
