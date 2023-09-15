#!/usr/bin/env python3

# Part 1: Write a number-guessing game
# Keep track of number of guesses - stop when # guesses = num_to_guess


largest_guess_possible = 100
num_to_guess = 45
max_num_of_guesses = 5

while input("Wanna play the number guessing game? (y or n) ==> ").upper() == "Y":

    num_guessed = False
    num_of_guesses = 0

    while (not num_guessed and num_of_guesses < max_num_of_guesses):
        # max_num_of_guesses = max_num_of_guesses - 1
        # Store users guess in variable
        my_guess = int(input(f"Guess a number between 0 and {largest_guess_possible} ==> "))
        # if the user's guess is not greater than 0 or less than biggest_num continue
        if (my_guess < 0 and my_guess > largest_guess_possible):
            print(f"{my_guess} is an invalid entry...  try again\n")
            # Don't count this iteration
            continue

        # Guess was valid if we reach this point
        num_of_guesses += 1
        if (my_guess > num_to_guess):
            # Let the user know their guess is too high
            print(f"Your guess of {my_guess} is too high")
            print(f"You have {max_num_of_guesses - num_of_guesses} guesses left")

        elif (my_guess < num_to_guess):
            # Let the user know their guess is too low
            print(F"Your guess of {my_guess} is too low")
            print(f"You have {max_num_of_guesses - num_of_guesses} guesses left")

        elif (my_guess == num_to_guess):
            num_guessed = True
            print(f"You found the number {num_to_guess}\nAnd it took you {num_of_guesses} guesses to get it")

        if (num_of_guesses == max_num_of_guesses):
            print(f"You have ran out of guesses")
        