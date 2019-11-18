# This is Hangman Game
# The objective of the game is to guess a word before your man is hung
# You will get 6 total guesses

import random

# Create a list of words for user to guess
word_list = ["Nermin"]
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


# Display dash instead of the word
print(*display_dash, sep=" ")

print("You have 6 chances to guess correctly the word.")
print("The word is hiden by dashes.")
print("To guess the word, you must provide letter that is part of the word.")


while guess_count < 6:
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
        break

    if not letter_found:
        guess_count += 1
        letter_found = False
    print(display_dash)

