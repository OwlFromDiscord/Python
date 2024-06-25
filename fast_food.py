menu_options = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookies"]
order_complete = "No"

def get_item(x):
    print(menu_options[x-1])

def welcome():
    print("Hello, and welcome to Food! What can we code fresh for you today?")
    print("")
    print("1 - Cheeseburger")
    print("")
    print("2 - Fries")
    print("")
    print("3 - Soda")
    print("")
    print("4 - Ice Cream")
    print("")
    print("5 - Cookies")

welcome()
while order_complete == "No" or order_complete == "no":
    get_item(int(input("Please type the menu item of the number you would like to order!")))
    print("Does this complete Your order?")
    order_complete = input("Please type 'Yes' or 'No'")
    if order_complete == "No" or order_complete == "no":
        print("What else would you like?")
        print("")
        print("1 - Cheeseburger")
        print("")
        print("2 - Fries")
        print("")
        print("3 - Soda")
        print("")
        print("4 - Ice Cream")
        print("")
        print("5 - Cookies")
    