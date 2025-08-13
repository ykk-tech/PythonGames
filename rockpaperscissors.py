# Libraries
import random
import time

# Game Variables
ans = random.randint(1, 3)
isrunning = True
print("Welcome to Rock, Paper, Scissors!")

while isrunning:
    # Player's choice
    time.sleep(2)
    player_choice = input("Choose rock (1), paper (2), or scissors (3): ").strip().lower()
    if player_choice not in ["rock", "paper", "scissors", "1", "2", "3"]:
        print("Invalid input! Please choose rock (1), paper (2), or scissors (3).")
        time.sleep(0.5)
        continue
    
    # Convert player's choice to a number
    if player_choice == "rock" or player_choice == "1":
        player_choice = 1
    if player_choice == "paper" or player_choice == "2":
        player_choice = 2
    if player_choice == "scissors" or player_choice == "2":
        player_choice = 3

    time.sleep(1)
    # Decide if player's choice beats AI
    if player_choice == ans:
        print("It is a draw! Nobody won.")
    if player_choice == 1 and ans == 2:
        print("You chose Rock, and the AI chose Paper! You lose.")
    if player_choice == 2 and ans == 1:
        print("You chose Paper, and the AI chose Rock! You won.")
    if player_choice == 1 and ans == 3:
        print("You chose Rock, and the AI chose scissors! You won.")
    if player_choice == 3 and ans == 1:
        print("You chose Scissors, and the AI chose Rock! You lose.")
    if player_choice == 3 and ans == 2:
        print("You chose Scissors, and the AI chose Paper! You win.")
    if player_choice == 2 and ans == 3:
        print("You chose Paper, and the AI chose Scissors! You lose.")

    # Asks the user if they would like to play again.
    time.sleep(1)
    play_again = input("Would you like to play again? (yes / no): ").strip().lower()
    if play_again == "yes":
        print("Okay! Taking you back to play again.")
    if play_again == "no":
        print("Okay! Have a great day!")
        isrunning = False
    else:
        print("Invalid Input. Please answer with a yes or a no.")