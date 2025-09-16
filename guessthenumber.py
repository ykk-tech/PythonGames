import random
import time

isrunning = True
attempts = 0
numto = 100

def askfornum():
    global numto
    que = int(input("Before we start, do you want to choose a number to go to or do go-to 100? (1/2): "))
    time.sleep(1)
    if que == 1:
        globalnumquestion = int(input("Please enter the number you want to go to: "))
        if globalnumquestion <= 0:
            print("Invalid Input. Please try again.")
            time.sleep(1)
            askfornum()
        else:
            numto = globalnumquestion
            print("The number has been chosen. You will not see this again.")
            time.sleep(1)
    elif que == 2:
        print("Okay! Going to 100.")
        time.sleep(1)
    else:
        print("Invalid Input. An error has occourred. Please try again.")
        time.sleep(1)
        askfornum()

askfornum()
print("You will not see this again unless you re-run the script.")
correct_number = random.randint(1, numto)
time.sleep(1)
print("Welcome to Guess the Number!")
time.sleep(1)
print(f"I have selected a number between 1 and {numto} Can you guess what it is?")
time.sleep(1)

while isrunning:
        number = int(input(f"Please enter a number between 1 and {numto}: "))
        if number < 1 or number > numto:
            print(f"Invalid input! Please enter a number between 1 and {numto}")
            time.sleep(0.5)
            continue
        if number == correct_number:
            attempts += 1
            print(f"Well done! You guessed the number, {correct_number} in {attempts} attempts.")
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                attempts = 0
                correct_number = random.randint(1, numto)
                print("A new number has been generated. Let's play again!")
                time.sleep(0.5)
            elif play_again == 'no':
                print("Thank you for playing! If you would like to play again, just restart the script.")
                time.sleep(0.5)
                isrunning = False
            else:
                print("Invalid input! Please respond with a 'yes' or a 'no'.")
                time.sleep(1)

        elif number < correct_number:
            attempts += 1
            print(f"Too low! You guessed {number}, but the correct number is higher. You have had {attempts} attempts.")
            time.sleep(1)
        elif number > correct_number:
            attempts += 1
            print(f"Too high! You guessed {number}, but the correct number is lower. You have had {attempts} attempts.")
            time.sleep(1)
        else:
            print(f"Invalid input! Please enter a number between 1 and {numto}.")
            time.sleep(1)
