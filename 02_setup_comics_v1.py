# Creating Comics as a class with comic name
# and comic number in stock as objects

# Create a variable to store the number of comics sold

class Comic:
    def __init__(self, name, num_stock):
        self.name = name
        self.num_stock = num_stock
        comics.append(self)


comics = []
comics_sold = 0

Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)
