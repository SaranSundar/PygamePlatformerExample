"""
  An array is a variable type, it holds a list of information. The information type such as String, int,
  float.

  # This is how you make an array
  array = []

  # This is how you add to an array
  array.append("data")

"""

print("Welcome to target")
print("-----------------")

# [   "Milk",     "Shirts",     "Shoes"        ]
# [       0,          1,           2         ]

target = []
target.append("Milk")
target.append("Shirts")
target.append("Shoes")
target.append("Goldfish")
target.append("Socks")

cart = []
cart.append("Socks")
cart.append("Shirts")


def show_inventory():
    for i in range(0, len(target)):
        print(target[i])


def print_options():
    print("1. Show Inventory")
    print("2. Show Shopping Cart")
    print("3. Add to Inventory")
    print("4. Add to Shopping Cart")
    print("5. Exit Target")


option = 0
while option != 5:
    print_options()
    option = input("Enter Option Number (1-5): ")
    # Convert string from input into type int
    option = int(option)
    if option == 1:
        show_inventory()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        print("Thanks for shopping, come again soon!")
    else:
        print("Please enter an option 1-5")
    print("")
