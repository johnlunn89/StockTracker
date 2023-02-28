# import numpy module for use of argmin and argmax functions

import numpy

# ========Class Definition========== #
# class defined and initialised
# methods created for returning price, quantity and for formatting object print out


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    def get_cost(self, list):
        for i in range(len(list)):
            shoe_price = list[i].cost
            return shoe_price

    def get_quantity(self, list):
        for i in range(len(list)):
            stock_level = list[i].quantity
            return stock_level

    def __str__(self):
        return f"Country: {self.country}\n" \
               f"Code: {self.code}\n" \
               f"Product: {self.product}\n" \
               f"Cost: {self.cost}\n" \
               f"Quantity: {self.quantity}\n"


# =============Empty List Store=========== #

shoe_list = []
most_stock_count = []
most_stock_product = []
least_stock_count = []
least_stock_product = []

# =========Functions outside the class============== #

# Function reads inventory.txt, cleans up data, creates objects and adds to list
# also uses a counter to keep track of which line is being read, handles errors such as missing lines
# or unfulfilled object attributes, indicates to user which line has an issue so they can fix it


def read_shoes_data(textfile, accessmode):
    counter = 1
    with open(textfile, accessmode) as file:
        for lines in range(1):
            next(file)
        for lines in file:
            temp = lines.strip(" ")
            temp = temp.strip("\n")
            temp = temp.split(",")
            counter += 1
            try:
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
            except IndexError:
                print(f"Notice: error in file on line {counter}")
                continue

# function establishes empty variables for all attributes of object and for new_shoe
# takes user input, concatenates the variables and appends to shoe_list
# added error handling so only INT values can be added for cost and quantity


def capture_shoes(list):
    country = ()
    code = ()
    product = ()
    cost = ()
    quantity = ()
    new_shoe = Shoe(country, code, product, cost, quantity)
    while True:
        try:
            new_shoe.country = input("Please enter country: ")
            new_shoe.code = input("Please enter the shoe code (SKU#####): ")
            new_shoe.product = input("Please enter the product name: ")
            new_shoe.cost = int(input("Please enter the cost of the shoe: "))
            new_shoe.quantity = int(input("Please enter quantity of this shoe in stock: "))
            break
        except ValueError:
            print("Incorrect entry type, please try again...")
    new_shoe = (Shoe(new_shoe.country, new_shoe.code, new_shoe.product, new_shoe.cost, new_shoe.quantity))
    list.append(new_shoe)
    print("\nNew shoe information added:\n")
    print(list[-1])
    return new_shoe

# view_all prints out the whole list


def view_all(list):
    for i in range(len(list)):
        print(list[i])
    return list

# re_stock creates two lists, one with all quantities then cast as integer, and another with all product names
# it then checks the index position of the lowest quantity, returns as shoe_list_position
# prints out quantity and product name from the two lists using the shoe_list_position
# asks user if they want to re-stock, takes input, updates object
# clears list_2 and list_3


def re_stock(list, list_2, list_3):
    stock_level = ()
    shoe_type = ()
    shoe_list_position = ()
    for i in range(len(list)):
        stock_level = list[i].quantity
        list_2.append(stock_level)
        for j in range(len(list_2)):
            list_2[j] = int(list_2[j])
        shoe_type = list[i].product
        list_3.append(shoe_type)
    shoe_list_position = numpy.argmin(list_2)
    print(f"\nLowest stock count is for {list_3[shoe_list_position]}, with a total of"
          f" {list_2[shoe_list_position]} in stock\n")
    update_stock = input("Would you like to update stock levels? Enter 'y' for yes or 'n' for no: ")
    while True:
        if update_stock == "y":
            new_stock_lvl = int(input("What is the new stock count for this item?: "))
            list[shoe_list_position].quantity = new_stock_lvl
            print("\nStock levels have been updated:\n")
            print(list[shoe_list_position])
            list_2.clear()
            list_3.clear()
            break
        elif update_stock == "n":
            break
        else:
            print("incorrect input, please choose again:")
            break

# takes user input. If SKU code matches it returns a print out of the item. if no match found user input taken again
# uses recursion of method on line 149 and 151
# gives user option to quit, so they don't get stuck in the loop


def search_shoe(list):
    user_choice = input("Please enter shoe code to (SKU#####), or enter 'q' to return to menu: ").upper()
    if user_choice == "Q":
        return
    for i in range(len(list)):
        if list[i].code == user_choice:
            print(f"\n{list[i]}")
            return search_shoe(list)
    print("That code doesn't match any in the system, please try again...")
    return search_shoe(list)

# defines empty variables, uses loop to find cost and quantity for every shoe and converts to int
# multiples cost_int by quantity_int to get value, prints for each line


def value_per_item(list):
    value = ()
    cost_int = ()
    quantity_int = ()
    for i in range(len(list)):
        cost_int = int(list[i].cost)
        quantity_int = int(list[i].quantity)
        value = cost_int * quantity_int
        print(f"The total value of {list[i].product} stock is ${value}.")


# works in similiar way to re-stock function, uses numpy argm.max to return index position of highest quantity in list
# uses this index ref to find name of highest quantity product and print


def highest_qty(list, list_2, list_3):
    stock_level = ()
    shoe_type = ()
    shoe_list_position = ()
    for i in range(len(list)):
        stock_level = list[i].quantity
        list_2.append(stock_level)
        for j in range(len(list_2)):
            list_2[j] = int(list_2[j])
        shoe_type = list[i].product
        list_3.append(shoe_type)
    shoe_list_position = numpy.argmax(list_2)
    print(f"\nHighest stock count is for {list_3[shoe_list_position]}, with a total of"
          f" {list_2[shoe_list_position]} in stock\n")

# main body of code starts now with function call to read inventory.txt

(read_shoes_data("inventory.txt", "r"))
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''\nSelect one of the following Options below:
    a  - Add a new product
    vp  - View all products
    s - Search for shoe
    cv - Check value of all stock
    h - View product with highest quantity in stock
    r - View lowest quantity stock and update stock amount
    e  - Exit: ''').lower()

# function calls listed below

    if menu == "a":
        capture_shoes(shoe_list)

    if menu == "vp":
        view_all(shoe_list)

    if menu == "s":
        search_shoe(shoe_list)

    if menu == "cv":
        value_per_item(shoe_list)

    if menu == "h":
        highest_qty(shoe_list, most_stock_count, most_stock_product)

    if menu == "r":
        re_stock(shoe_list, least_stock_count, least_stock_product)

    if menu == "e":
        break
