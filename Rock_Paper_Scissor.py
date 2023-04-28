import random


user_win = 0
computer_win = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input("Rock, Paper, Scissor or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Helps computer determine what answer is what. Rock = 0, Paper = 1, Scissor = 2

    computer_pick = options[random_number]
    print("Computer picked" , computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You win!")
        user_win += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Win!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_win += 1

    else:
        print("You Lose!")
        computer_win += 1

print("You won", user_win, "times.")
print("Computer won", computer_win, "times.")

