# This is Hangman Game
# The objective of the game is to guess a word before your man is hung
# You will get 6 total guesses

import random

# Create a list of words for user to guess
word_list = ["Nermin", "Sanja", "apple", "house"]
# Shuffle the list each time the scrip is run
random.shuffle(word_list)
# Variable to track guesses
guess_count = 0
# User guess
user_gueess = ""
# Extract word for guessing
word = list(word_list[0])


print(word)
