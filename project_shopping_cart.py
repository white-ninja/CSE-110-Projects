# Project: Shopping Cart
# Author: Emmanuel Adejare Ariyo
# Date: 10/8/25
# Description: This is a text based shopping cart application.
# P.S: Methods used in this project are append(), pop(), insert(), sum(), and format(f"{i + 1}") to get my user friendly count, was learnt online.
shopping_list = []
shopping_list_prices = []
while True:
    print("Welcome to the shopping cart application!")
    print("please select one of the following options:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter an item to add to your shopping list or type 'quit' to end: ")
        if item == "quit":
            break
        price = float(input("Enter the price of the item: "))
        shopping_list.append(item)
        shopping_list_prices.append(price)
        print(f"{item} has been added to the cart.")
    elif choice == "2":
        print("The items in your cart are:")
        for i in range(len(shopping_list)):
            print(f"{i + 1}. {shopping_list[i]} - ${shopping_list_prices[i]:.2f}")
    elif choice == "3":
        remove_item = int(input("Which item would you like to remove? Enter the number: "))
        if 1 <= remove_item <= len(shopping_list):
            removed_item = shopping_list.pop(remove_item - 1)
            removed_price = shopping_list_prices.pop(remove_item - 1)
            print(f"{removed_item} has been removed from the cart.")
        else:
            print("That item number is out of range.")
    elif choice == "4":
        total = sum(shopping_list_prices)
        print(f"The total price of the items in the cart is: ${total:.2f}")
    elif choice == "5":
        print("Thank you for shopping with us. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")












# Practice Exercise: Shopping Cart Application
# items = []
# prices = []

# while True:
#     item = input("Enter an item to add to your shopping list or type 'quit' to end:")
#     if item == "quit":
#         break


