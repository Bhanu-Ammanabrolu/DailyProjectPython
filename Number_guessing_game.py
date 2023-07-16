from random import randint
from art import number_guess_art

print(number_guess_art)

print("---- Welcome to number guessing game ----")
print(" --- computer thinking a number in range 1 - 100 - Can you guess? ----")
game_level = input("which level u want play - Easy or hard? ")
COMP_GUESS = randint(1, 100)
ATTEMPTS = 0


def guessing(user_input, computer_input, attempts):
    if user_input < computer_input:
        attempts -= 1
        return "Too Low. \n Guess again."
    elif user_input > computer_input:
        attempts -= 1
        return "Too High. \n Guess again."
    elif user_input == computer_input:
        return f"You guessed right - {user_input} is the Answer."


if game_level == "easy":
    ATTEMPTS = 5
    print(f"you have {ATTEMPTS} to guess.")
    user_guess = int(input("Make a guess - "))
    result = guessing(user_guess, COMP_GUESS, ATTEMPTS)
    print(result)

elif game_level == "hard":
    ATTEMPTS = 10
    print()
