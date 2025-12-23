# Project: Meal Price Calculator
# Description: This program calculates the total meal price including tax and.
# It prompts the user for the meal price, and tax rate, then computes and displays the final amount.
# Author: Emmanuel Ariyo
# Date: 2025-09-12

# Get user input for meal price and tax rate
childrens_meal_price = float(input("Enter the children's meal price: $"))
adults_meal_price = float(input("Enter the adult's meal price: $"))
number_of_children = int(input("Enter the number of children: "))
number_of_adults = int(input("Enter the number of adults: "))
childrens_meal_price *= number_of_children
adults_meal_price *= number_of_adults
meal_price = childrens_meal_price + adults_meal_price
print(f"The total meal price before tax is: ${meal_price:.2f}")

# Calculate total meal price including tax
tax_rate = float(input("Enter the tax rate (as a percentage): "))
tax_amount = meal_price * (tax_rate / 100)
total_price = meal_price + tax_amount
print(f"The total meal price including tax is: ${total_price:.2f}")

# Calculate change from payment
payment_amount = float(input("Enter the payment amount: $"))
change = payment_amount - total_price
print(f"Your change is: ${change:.2f}")
