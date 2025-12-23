# Project: Word Puzzle Game
# Author: Emmanuel Adejare Ariyo
# Date: 9/28/25 
# Description: This is a text based word puzzle game.
import random
keep_playing = "yes"
while keep_playing == "yes":
    words = ["apple", "banana", "cherry", "lion", "elephant", "giraffe", "zebra", "kangaroo", "dolphin", "eagle", "crocodile", "panda", "chimpanzee", "mango", "pineapple", "orange", "watermelon", "papaya", "strawberry", "grapes", "coconut"]
    secret_word = random.choice(words)
    guess_count = 0

# Welcome message!
    print("Welcome to the word puzzle game!")
    print("This game uses a hint function along with an upper(A), lower(b), & an underscore(_) to suggest the positions, availability, or unavailability of the letters of your word guess in the game.")
# Generate initial hint: first letter, rest underscores
    initial_hint = ""
    for i, letter in enumerate(secret_word):
        if i == 0:
            initial_hint += letter.upper() + " "
        else:
            initial_hint += "_ "
    print(f"Hint: {initial_hint.strip()}")

#OR, Generate initial hint: No first letter, all underscore.

    # initial_hint = "_ " * len(secret_word)
    # print(f"Hint: {initial_hint.strip()}")

    while True:
        guess = input("What is your guess? ").lower()
        guess_count += 1
        
        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long.")
            continue


# Generate hint for this guess
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "
            else:
                hint += "_ "
        print(f"Hint: {hint.strip()}")

        if guess == secret_word:
            break
        else:
            print("Incorrect guess. Try again!")

    print(f"You guessed it right! The puzzle word was {secret_word.capitalize()}.")
    print(f"It took you {guess_count} guesses.")
    keep_playing = input("Would you like to play again (yes/no)? ")
    print("Thanks for playing. Goodbye!")



# while guess != secret_word:
#     print("Incorrect guess. Try again!")
#     guess = input("What is your guess? ").lower()

# print(f"You guessed it right! The puzzle word was {secret_word}.")
# print(f"It took you {guess_count} guesses. ")
