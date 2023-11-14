import random
from art_GTN import logo

EASY_TURNS = 10
HARD_TURNS = 5

def number_guess_generator():

    random_number = random.randint(1,100)
    return random_number

def user_guess(choice, guess):
    guessed_right = False
    user_choice = input("Make a Guess")

    if user_choice > guess:
        print ("Too High, guess again")
    elif user_choice == guess:
        guessed_right = True
        print ("that is the right answer, good job")
    else:
        print("Too low, try again")

