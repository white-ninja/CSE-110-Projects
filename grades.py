# Ask the user for their grade
grade = float(input("Enter your grade (0-100): "))

letter = ""

# Figure out if they passed or failed
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Get the last digit

last_digit = grade % 10

sign = ""
# Determine the sign

if last_digit >= 7:
    sign = "+"
elif last_digit <3:
    sign = "-"
# else:
#     sign = ""

# Handle Exception (A+, F+, F-)

if letter == "A" and sign == "+":
    sign = ""

if letter == "F":
    sign = ""

# Print out an appropriate message
print(f"you've earned the grade {letter}{sign}")
   
if grade >= 70:
    print("Congratulations! You've passed the course!")
else:
    print("Sorry, please try the course again!")