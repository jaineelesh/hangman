# Hangman Algo
# 1. Welcome logo
# 2. random animal is selected from animal names
# 3. Equal length dashes is printed for user to guess
# 4. user is asked to guess a letter
# 5. the letter is checked if it is present in the animal name or not.
# 6. if present, hangman pic remains same, letters are printed instead of dashes
# 7. if not present, hangman pic is updated while dashes remain as it is
# 8. if the abc pic reaches last, game is over and the user looses
# 9. if all the dashes are removed => user guesses all the letters, user wins.

from resource import HANGMANPICS, words, welcome_image
import os
import random

print(welcome_image)
animal = random.choice(words)

dash_list = []
for _ in animal:
    dash_list += "_"

counter = 0
while True:
    os.system("cls")
    print(" ".join(dash_list))
    choice = input("please guess a letter: ")
    if choice in animal:
        for i in range(len(animal)):
            if animal[i] == choice:
                dash_list[i] = choice
    else:
        counter += 1
    print(HANGMANPICS[counter])

    if counter == len(HANGMANPICS) - 1:
        print(f"you lost, the animal was-  {animal}")
        break
    elif "_" not in dash_list:
        print(f"you won, animal - {animal}")
        break
