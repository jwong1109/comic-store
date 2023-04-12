# Comic Book Store Label

from tkinter import *

# Root Window
root = Tk()
root.title("Sales and Stock Level System")
root.geometry("800x300")
root.configure(bg="gold")
root.resizable(False, False)

# Comic Book Store Label
title_label = Label(root, bg="gold", fg="black", text="Comic Book Store",
                    font=("Arial", 30, "bold"))
title_label.pack(ipady=10)

root.mainloop()
