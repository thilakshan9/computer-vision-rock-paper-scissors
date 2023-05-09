import random


def get_computer_choice():
    options_list = ["scissors", "rock", "paper"]
    return random.choice(options_list)

def get_user_choice():
    return input("Enter your choice ")

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    if user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    else:
        print("You lost")

def play():
    computer_choice = get_computer_choice()
    user_choice =  get_user_choice()
    get_winner(computer_choice, user_choice)

play()