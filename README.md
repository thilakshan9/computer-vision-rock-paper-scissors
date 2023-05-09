# Computer Vision RPS

# Milestone 1
Created a model using teachable machine and added it to the root folder.

# Milestone 2
Set up a conda virtual environment and installed packages: opencv-python, tensorflow and ipykernel.Dealt with the game logic in another function. Checked the model worked by using code given to me by AICore and got familiar with the code. Used opencv-python for computer vision and made sure my hand signs were being recognised. 

# Milestone 3
Created two functions 1. To handle with user input 2. To generate a random response as the CPU response. I randomised the CPU response from a list of options and made sure that the user input function allowed me to input a string. 

# Milestone 4
The game decided a winner based on the classic rules of rock-paper-scissors using if-elif-else statements. I also wrapped everything related to the game in function. 

# Milestone 5
Used opencv-python from the previous code to implement into the rock-paper-scissors game to play against the computer. Used a while loop to create a best of three rounds game and keep track of the wins of each player. I added a 3 second counter to allow the user to come to a final decision of their choice instead of reading the input from the cameras and comparing it to the computer's hand without stopping.

# Milestone 6
Created a class instead of using multiple functions to have all under one object - this improved readability and made the code a lot cleaner.

# Bugs and Fixes
Python and conda were in separate file paths which was giivng problems with the packages when running the file. I had to change the file path of the python it was using (multiple pythons on system).
Included rounds to make sure it accounts for when no player reaches 3 wins but win the best of three due to ties.

## By Thilakshan Balasubramaniam