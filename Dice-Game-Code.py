import random


def throw_dice():
    return random.randint(1, 6)


target_score = 0

while True:
    num_players_str = input("Select players (2 - 4): ")
    if num_players_str.isdigit():
        num_players = int(num_players_str)
        if 2 <= num_players <= 4:
            break
        else:
            print("Choose between 2 - 4 players.")
    else:
        print("Invalid input, please choose between 2-4 players.")

while True:
    input_score = input("Please enter the final target score: ")
    if input_score.isdigit():
        target_score = int(input_score)
        if target_score < 20:
            print('Please choose a valid target score, at least 20')
        else:
            break
    else:
        print("Invalid input, please enter a numerical value.")

scores = [0] * num_players

while max(scores) < target_score:
    for player_index in range(num_players):
        print(f"\nPlayer {player_index + 1}, it's your turn!")
        print(f"Your current score: {scores[player_index]}\n")
        turn_score = 0

        while True:
            roll_choice = input("Do you want to roll the dice (y/n)? ")
            if roll_choice.lower() != "y":
                break

            dice_value = throw_dice()
            if dice_value == 1:
                print("You rolled a 1! Your turn is over.")
                turn_score = 0
                break
            else:
                turn_score += dice_value
                print(f"You rolled a: {dice_value}")

            print(f"Your turn score is: {turn_score}")

        scores[player_index] += turn_score
        print(f"Your total score is now: {scores[player_index]}")

winning_player = scores.index(max(scores))
print(f"\nPlayer {winning_player + 1} wins with a score of {max(scores)}! Congratulations!")