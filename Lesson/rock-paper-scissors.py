import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("\n\nComputer: ",computer)
        print("Player: ",player)
        print("\n\nTie!")
    elif player == "rock":
        if computer == "paper":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou lose!")
        if computer == "scissors":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou win!")
    elif player == "scissors":
        if computer == "paper":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou win!")
        if computer == "rock":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou Lose!")
    elif player == "paper":
        if computer == "scissors":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou lose!")
        if computer == "rock":
            print("\n\nComputer: ",computer)
            print("Player: ",player)
            print("\n\nYou win!")

    play_again = input("Wanna play again?(yes/no): ").lower()

    if play_again != "yes":
        break

print("BYE!")