import random

Game = ["Rock", "Paper", "Scissors"]
game_len = len(Game)

user_input = int(input("Select choice 0 - Rock, 1 - Paper, 2 - Scissors ----  "))

if user_input >= 3 or user_input < 0:
    print("INVALID INPUT")

else:
    user_choose = Game[user_input]
    print(user_choose)

    computer_input = random.randint(0, game_len - 1)

    comp_choose = Game[computer_input]
    print(f"Computer Choose ---- {comp_choose}")

    if user_choose == "Rock" and comp_choose == "Scissors":
        print("YOU WON")
    elif user_choose == "Scissors" and comp_choose == "Paper":
        print("YOU WON")
    elif user_choose == "Paper" and comp_choose == "Rock":
        print("YOU WON")
    elif user_choose == comp_choose:
        print("It's a TIE")
    else:
        print("YOU LOST!!!!!!!!!!!")

