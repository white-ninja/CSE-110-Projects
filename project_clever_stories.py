# Emmanuel Ariyo
# CSE110 - 001
# 2025-09-09
# Project: Clever Stories
# Description: A program that generates a clever story based on user input.

# Get user inputs
adjective1 = input("Enter an adjective: ")
animal_noun = input("Enter a name of an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")

# Generate and print the story
story = print(f"""The other day, I was really in trouble.
 It all started when I saw a very {adjective1} {animal_noun} {verb1} down the hallway.    
"{exclamation.capitalize()}!" I yelled. But all i could think to do was to {verb2} over and over.
Miraculosly, that caused it to stop, but not before it tried to {verb3} right in front of my family.""")