import random


def get_computer_choice():
    """
    This functions generates the computer's choice in the rock-paper-scissors game.

    The purpose of this function is to return a random option 
    from the list of options provided in the options_list
    """
    options_list = ["scissors", "rock", "paper"]
    return random.choice(options_list)

def get_user_choice():
    """
    This functions stores the user's choice in the rock-paper-scissors game.

    The purpose of this function is to return the user's option 
    of the rock-paper-scissors game
    """
    return input("Enter your choice ")

def get_winner(computer_choice, user_choice):
    """
    This function determines the winner of the rock-paper-scissors round.

    The purpose of this function is to return the winner of the game based on the if-elif-statements.
    This is used to determine whether the comptuer won, user won or tied. The variables are made global so they be accessed 
    outside of the function as well (not limited to the scope of the function).
    """
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
    """
    This function runs the game logic

    The while loop runs for the duration of the game and the if else statements determine whether the end of the
    game has been reached or not. Inside the first if statement, the winner is determined or if there is a tie.
    """
    computer_choice = get_computer_choice()
    user_choice =  get_user_choice()
    get_winner(computer_choice, user_choice)

play()