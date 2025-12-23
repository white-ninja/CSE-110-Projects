# Project: Adventure Game
# Author: Emmanuel Ariyo
# Date: 2025-09-18
# Description: A simple text-based adventure game.

import sys

def get_choice(prompt, options):
    """Prompt the user until they type one of the allowed options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Try again.")

def dark_forest():
    print("You venture into the dark forest and encounter a wild beast!")
    action = get_choice("Do you want to 'fight', 'weapon', or 'run'? ", 
                        ["fight", "weapon", "run"])

    if action == "fight":
        print("You bravely fight the beast and emerge victorious!")
    elif action == "weapon":
        print("You fought the super ferocious beast with your weapon and won!")
    elif action == "run":
        print("You run away and hide up a tree. You live to fight another day!")

def sunny_beach():
    print("You walk towards the sunny beach and find a treasure chest!")
    action = get_choice("Do you want to 'open', 'leave', or 'bury' it? ", 
                        ["open", "leave", "bury"])

    if action == "open":
        print("You open the chest and find gold and jewels!")
    elif action == "leave":
        print("You leave the chest alone and enjoy a peaceful day at the beach.")
    elif action == "bury":
        print("You bury the chest safely for later. Smart move!")

def main():
    print("Welcome to the Adventure Game!")
    print("You find yourself at a crossroads in a mysterious land.")

    first_choice = get_choice(
        "Type 'left' for the forest or 'right' for the beach: ", 
        ["left", "right"]
    )

    if first_choice == "left":
        dark_forest()
    else:
        sunny_beach()

    print("Thank you for playing the Adventure Game!")

if __name__ == "__main__":
    main()
