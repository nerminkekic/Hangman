# This is Hangman Game
# The objective of the game is to guess a word before your man is hung
# You will get 6 total guesses

import random

# Instruction for player
rules_for_player = """
        ################################################################################################
        #   Welcome to Hangman game!                                                                   #
        #   The rules of the game are as fallowng:                                                     #
        #       1. To win you must guess the secret word correctly.                                    #
        #       2. You will be given chance to enter one letter at the time.                           #
        #       3. Two or more letters entered, will count as wrong asnwer.                            #
        #       4. You have 6 chances to guess wrong, before game ends.                                #
        #       5. If you guess the word incorrect, game will subtract 1 point from 6 trys.            # 
        #       6. If you guess the word correctly, you will be able to continue without penalty.      #
        ################################################################################################
        """

# Create a list of words for user to guess
word_list = ["Nermin", "Sanja", "Nusret", "Fikra", "Zenaida", "Amira"]
# Shuffle the list each time the scrip is run
random.shuffle(word_list)
# Variable to track guesses
guess_count = 0
# User guess
player_guess = ""
# Flag to makre ture if letter is part of the word
letter_found = False
# Extract word for list
# Then index each letter in word
# Make all letters lowercase
word = list(word_list[0])
word = "".join(word)
word = word.lower()
# Replace each letter in word with dash
display_dash = []
for i in range(len(word)):
    display_dash.append("_")

# Disply instructions for player
print(rules_for_player)
# Display dash instead of the word
print("The secret word is:")
print(*display_dash, sep=" ")

while guess_count < 6:
    letter_found = False
    # Get the letter from player
    player_guess = input("To proceed, enter letter that is part of the word: ")
    player_guess = player_guess.lower()
    # Check if the player guess exist in the secret word
    for i, letter_in_word in enumerate(word):
        if player_guess == letter_in_word:
            display_dash[i] = player_guess
            letter_found = True
    # Check if the display has no dash, means the word has been guessed player has won
    if display_dash.count("_") == 0:
        print("You WON!!! Good job, you guessed the word correctly!")
        print(*display_dash, sep=" ")
        break
    elif not letter_found:
        print("You have entered letter that does not exist in the word.")
        guess_count += 1
        if guess_count == 6:
            print("You have used all your guesses, better luck next time!")
            print(f"You have guessed: {' '.join(display_dash)}")
            print(f"Correct word is: {' '.join(word)}")
        continue
    
    print(*display_dash, sep=" ")

wait = input("Press ENTER to end game.")