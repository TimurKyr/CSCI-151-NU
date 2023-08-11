playing = True
player_1, player_2 = "", ""
valid_answers = ['R', 'P', 'S']
answers = ""
result = ""
play_again = ""
player_1_win_options = ["RS", "PR", "SP"]
player_2_win_options = ["RP", "PS", "SR"]

def check_round(answers):
    if answers in player_1_win_options:
        return 1
    if answers in player_2_win_options:
        return 2
    return 0

while True:
    player_1 = input("Enter Player 1 choice ('R','P','S')\n")
    if player_1 not in valid_answers:
        print("Not a valid input!")
        continue
    while True:
        player_2 = input("Enter Player 2 choice ('R','P','S')\n")
        if player_2 not in valid_answers:
            print("Not a valid input!")
            continue
        answers = player_1 + player_2
        result = check_round(answers)
        if result != 0:
            break
        print("Your input is the same as Player 1. Please select another choice!")
    if result == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    play_again = input("Do you want to play again?(Enter 'Y' or 'y' for YES)\n")
    if play_again != 'Y' and play_again != 'y':
        break
