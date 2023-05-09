import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
import random
import time

def get_computer_choice():
    options_list = ["scissors", "rock", "paper"] 
    # List of all the options the computer can choose
    return random.choice(options_list)
    # Returns a random option from the list of options

def get_prediction():
    time_passed = time.time() + 3
    options_list = ["rock", "scissors", "paper", "nothing"]
    while time.time() < time_passed: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        index = np.argmax(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return options_list[int(index)]

def get_user_choice():
    user_choice = get_prediction()
    print(f"You choose {user_choice}")
    return user_choice


computer_wins = 0
user_wins = 0
def get_winner(computer_choice, user_choice):
    global computer_wins, user_wins
    if computer_choice == user_choice:
        print("It is a tie!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won this round !")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won this round!")
        user_wins += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won this round!")
        user_wins += 1
    else:
        print("You lost this round")
        computer_wins += 1
    # The above prints a message according to the condition that it meets

def play():
    while computer_wins <3 and user_wins < 3:
        computer_choice = get_computer_choice()
        user_choice =  get_user_choice()
        get_winner(computer_choice, user_choice)
        print(computer_wins)
        print(user_wins)
    if computer_wins == 3:
        print("You lost the game")
    else:
        print("You won the game")

play()
