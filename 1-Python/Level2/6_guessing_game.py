#!/usr/bin/python3
# Create a basic number guessing game.
import random
number_to_guess = random.randint(0, 3)
chances = 10
guess_counter = 1
while guess_counter < chances:
    my_guess = int(input('plese enter your Guess number: '))
    if my_guess == number_to_guess:
        print(f'{my_guess} Is COOOOORRECT!!! in the {guess_counter} attempt')
        break
    else:
        print('You are guessing wrong!, Try Again')
        guess_counter += 1
