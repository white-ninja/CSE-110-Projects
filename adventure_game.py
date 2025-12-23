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
choice1 = input("Type 'LEFT' for the forest or 'RIGHT' for the beach: ").lower()

# Outcome based on first decision and nested choices
if choice1 == "left":
    print("You venture into the dark forest and encounter a wild beast!")
    action = input("Do you want to 'FIGHT' the beast or get a 'WEAPON' or 'RUN' away? ").lower()
    if action == "fight":
        print("You bravely fight the beast and emerge victorious!")
        print("The beast happens to be super ferocious!")
    action2 = input("would you fight the beast with a 'WEAPON'?").lower()
    if action2 == "weapon":
        print("You fought the super ferocious beast with your weapon")
        print("You emerged victorious! And skinned the best alive with the weapon")
    elif action2 == "withold":
        print("Withold fighting with a weapon and end up getting devoured alive!")
    else:
        print("Invalid choice! Game Over.")
        print("The beast seems to overpower you!")
    action3 = input("Would you like to 'RUN' a way?")
    if action3 == "run":
        print("You run away and hide up a tree")
    else:
        print("Invalid choice. The beast catches you. Game over!")
elif choice1 == "right":
    print("You walk towards the sunny beach and find a treasure chest!")
    action = input("Do you want to 'OPEN' the chest or 'LEAVE' it alone or 'BURY' it? ").lower()
    if action == "open":
        print("You open the chest and find gold and jewels!")
        print("Oh no! You seem not to find the keys to the lock!")
    action2 = input("Would you 'LEAVE' it there? ")
    if action2 == "leave":
        print("You leave the chest alone and enjoy a peaceful day at the beach.")
        print("Sometimes, the best treasure is a moment of peace.")
    elif action2 == "find key":
        print("Find key until you're exhuasted")
    action3 = input("Would you like to 'BURY' chest?")
    if action3 == "bury":
        print("You resolved to burying the chest.")
    else:
        print("Invalid choice. A wave sweeps you away. Game over!")
    print("Congratulations! You have completed your adventure.")
# # End of game message
print("Thank you for playing the Adventure Game!")

# Outcome based on second decision and nested choices
# choice2 = input("Do you want to 'CONTINUE' your adventure or 'STOP' here? ").lower()
# if choice2 == "continue":
#     print("You decide to continue your adventure.")
#     print("You walk deeper into the forest and find a hidden cave.")
#     action = input("Do you want to 'ENTER' the cave or 'RETURN' to the crossroads? ").lower()
#     if action == "enter":
#         print("You enter the cave and discover ancient artifacts!")
#         print("Congratulations! You have completed your adventure.")
#     elif action == "return":
#         print("You return to the crossroads safely but miss out on a great discovery.")
#         print("Maybe next time you'll be more adventurous!")
#     else:
#         print("Invalid choice. You get lost in the forest. Game over!")

# # Outcome based on third decision and nested choices
# choice3 = input("Do you want to 'SELL' the cave or 'WILL' your discoveries? ").lower()
# if choice3 == "sell":
#     action = input("Do you want to 'SELL' the discoveries or 'WILL' them to a museum? ").lower()
#     if action == "sell":
#         print("You decide to sell your discoveries.")
#         print("You make a fortune and live happily ever after!")
# elif choice3 == "will":
#     action = input("Do you want to 'WILL' your discoveries to a friend or a museum? ").lower()
#     if action == "will":    
#         print("You decide to will your discoveries to a friend.")
#         print("Your friend goes on to make great discoveries and thanks you!")
# else:
#     print("Invalid choice. You miss out on a great opportunity. Game over!")

# Second level (Nested Scenario)
# print("You find a mysterious map leading to another hidden treasure.")
# direction = input("Do you want to go 'NORTH' into the mountains or 'SOUTH' into the desert? ").lower()
# if direction == "north":
#     print("You trek into the mountains and find a hidden temple!")
#     action = input("Do you want to 'EXPLORE' the temple or 'CAMP' outside? ").lower()
#     if action == "explore":
#         print("You explore the temple and find priceless artifacts!")
#         print("Congratulations! You have completed your adventure.")
#     elif action == "camp":
#         print("You camp outside and enjoy the beautiful mountain scenery.")
#         print("Sometimes, the best treasure is a moment of peace.")
#     else:
#         print("Invalid choice. You get lost in the mountains. Game over!")
# elif direction == "south":
#     print("You venture into the desert and find an oasis!")
#     action = input("Do you want to 'DRINK' from the oasis or 'REST' under a palm tree? ").lower()
#     if action == "drink":
#         print("You drink from the oasis and feel rejuvenated!")
#         print("Congratulations! You have completed your adventure.")
#     elif action == "rest":
#         print("You rest under a palm tree and enjoy the peaceful desert.")
#         print("Sometimes, the best treasure is a moment of peace.")
#     else:
#         print("Invalid choice. You get lost in the desert. Game over!")

# # Outcome based on second decision and nested choices
# pawn_map = input("Do you want to 'PAWN' the map for quick cash or 'KEEP' it for future adventures? ").lower()
# if pawn_map == "pawn":
#     action = input("Do you still want to 'PAWN' the map or 'KEEP' it? ").lower()
#     if action == "pawn":
#         print("You decide to pawn the map for quick cash.")
#         print("You get some money but miss out on a great adventure.")
# elif pawn_map == "keep":
#     action = input("Do you still want to 'KEEP' the map or 'SELL' it? ").lower()
#     if action == "keep":
#         print("You decide to keep the map for future adventures.")
#         print("You embark on many exciting journeys with the map!")
#     else:
#         print("Invalid choice. You miss out on a great opportunity. Game over!")

# # Outcome based on third decision and nested choices
# will_map = input("Do you want to 'WILL' the map to a friend or 'SELL' it to a collector? ").lower()
# if will_map == "will":
#         print("You decide to will the map to a friend.")
#         print("Your friend goes on to make great discoveries and thanks you!")
# elif will_map == "sell":
#     action = input("Do you still want to 'SELL' the map or 'WILL' it? ").lower()
#     if action == "sell":    
#         print("You decide to sell the map to a collector.")
#         print("You make a good profit and live happily ever after!")
# else:
#     print("Invalid choice. You miss out on a great opportunity. Game over!")

# # Third level (Final Scenario)
# print("You reach the final leg of your adventure and find a dragon guarding a treasure!")   
# action = input("Do you want to 'TALK' to the dragon or 'FIGHT' it? ").lower()
# if action == "talk":
#     print("You talk to the dragon and discover it's friendly!")
#     print("The dragon shares its treasure with you!")
#     print("Congratulations! You have completed your adventure.")    
# elif action == "fight":
#     print("You bravely fight the dragon and win!")
#     print("You claim the treasure as your own!")
#     print("Congratulations! You have completed your adventure.")
# else:
#     print("Invalid choice. The dragon incinerates you. Game over!")

# # Outcome based on second decision and nested choices.
# final_choice = input("Do you want to 'CONTINUE' your adventure or 'STOP' here? ").lower()
# if final_choice == "continue":
#     print("You decide to continue your adventure.")
#     print("You find a secret passage leading to an underground city.")
#     action = input("Do you want to 'EXPLORE' the city or 'RETURN' to the dragon's lair? ").lower()
#     if action == "explore":
#         print("You explore the city and find advanced technology!")
#         print("Congratulations! You have completed your adventure.")
#     elif action == "return":
#         print("You return to the dragon's lair safely but miss out on a great discovery.")
#         print("Maybe next time you'll be more adventurous!")
#     else:
#         print("Invalid choice. You get lost in the underground city. Game over!")
        
# # Outcome based on third decision and nested choices.
# treasure_choice = input("Do you want to 'SELL' the treasure or 'WILL' it to a museum? ").lower()
# if treasure_choice == "sell":
#     print("You decide to sell the treasure.")
#     print("You make a fortune and live happily ever after!")
# elif treasure_choice == "will":
#     print("You decide to will the treasure to a museum.")
#     print("Your name goes down in history as a great adventurer!")
# else:
#     print("Invalid choice. You miss out on a great opportunity. Game over!")
