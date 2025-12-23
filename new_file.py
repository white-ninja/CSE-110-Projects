# Project: Adventure Game
# Author: Emmanuel Ariyo
# Date: 2025-09-18
# Description: A simple text-based adventure game where the player makes choices to navigate through a story.
# The game uses conditional statements to determine the outcome based on the player's decisions.
# Welcome message
print("Welcome to the Adventure Game!")

# Game introduction
print("You find yourself at a crossroads in a mysterious land.")

# First level (Scenario)
print("Do you want to go left towards the dark forest or right towards the sunny beach?")  
choice = input("Type 'LEFT' for the forest or 'RIGHT' for the beach: ").lower()

# Outcome based on first decision and nested choices.
if choice == "left":
    print("You venture into the dark forest and encounter a wild beast!")
    action = input("Do you want to 'FIGHT', 'RUN', 'SHOOT' the beast? ").lower()
    if action == "fight":
        print("You bravely fought off the beast and killed it!")
        next_action = input("Do you want to 'EXPLORE' deeper or 'RETURN' to the crossroads? ").lower()
        if next_action == "explore":
            print("You discover a hidden cave filled with treasure!")
        elif next_action == "return":
            print("You safely return to the crossroad.")
        else:
            print("Confused, you wander and get lost. Game Over.")
    elif action == "run":
        print("You ran up the mountain and found a shelter.")
        shelter_action = input("Do you want to 'REST' or 'CONTINUE' exploring? ").lower()
        if shelter_action == "rest":
            print("You recover your strenght and survive the night.")
        elif shelter_action == "continue":
            print("You stumble upon a friendly hermit who helps you.")
        else:
            print("You get caught in a storm. Game over.")
    elif action == "shoot":
        print("You shot the beast and the forest goes silent.")
        forest_action = input("Do you want to 'SEARCH' the area or 'LEAVE'? ").lower()
        if forest_action == "search":
            print("You find a magical amulet on the beast!")
        elif forest_action == "leave":
            print("You leave the forest safely.")
        else:
            print("You trip and fall. Game Over.")
    else:
        print("Invalid choice. You're killed by the beast. Game over. ")

# Outcome based on second decision and nested choices.
elif choice == "right":
    print("You walk towards the sunny beach and find a treasure chest!")
    rightside_action = input("Do you want to 'OPEN' the chest, or 'LEAVE' it, or 'BURY' it? ").lower()
    if rightside_action == "open":
        print("You open the chest and find a map to a hidden island!")
        map_action = input("Do you want to 'FOLLOW' the map or 'IGNORE' it? ").lower()
        if map_action == "follow":
            print("You sail to the island and discover ancient ruins filled with gold!")
        elif map_action == "ignore":
            print("You relax on the beach and enjoy the sunshine.")
        else:
            print("You get lost in thought and miss your chance. Game over.")
    elif rightside_action == "leave":
        print("You decide to leave the chest untouched and walk along the shore.")
        shore_action = input("Do you want to 'SWIM' in the ocean or 'BUILD' a sandcastle? ").lower()
        if shore_action == "swim":
            print("You find beautiful seashells while swimming!")
        elif shore_action == "build":
            print("You build an impressive sandcastle and attract friendly locals.")
        else:
            print("You get sunburned and have to leave. Game over.")
    elif rightside_action == "bury":
        print("You bury the chest for safekeeping.")
        bury_action = input("Do you want to 'MARK' the spot or 'LEAVE' it unmarked? ").lower()
        if bury_action == "mark":
            print("You mark the spot and plan to return with friends.")
        elif bury_action == "leave":
            print("You forget where you buried the chest. Game over.")
        else:
            print("A crab steals your marker. Game over.")
    else:
        print("Confused, you wander off and get lost. Game over.")

#End of game message
else:
    print("You made made a wrong choice game over!")
    print("Thank you for playing the Adventure Game!")