import random


def roll():
    min_value = 1
    max_value = 6

    dice = random.randint(min_value, max_value)

    return dice


players = True
while players:
    num_of_players = int(input("How many players today (2 - 4): "))
    if num_of_players < 2 or num_of_players > 4:
        print("Enter a valid Number. Try again.")
    else:
        players = False

max_score = 50
player_scores = [0 for _ in range(num_of_players)]


while max(player_scores) < max_score:
    for player_idx in range(num_of_players):
        print(f"\n{player_idx + 1} player's Turn.")
        print(f"Your total score is {player_scores[player_idx]}\n")
        current_score = 0
        while True:
            User_choice = input("Ready to roll the the dice - Y or N: ").upper()
            if User_choice != "Y":
                break

            dice_number = roll()
            print(f"you turned the dice_number: {dice_number}")
            if dice_number != 1:
                current_score += dice_number
                print(f"your current score is: {current_score}")

            else:
                current_score = 0
                print(f"your current score is: {current_score}")
                break
    player_scores[player_idx] += current_score
    print(f"Your score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"player {winning_idx + 1} is the WINNER!!!!!!!")