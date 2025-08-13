import random
import time

isrunning = True
attempts = 0
correct_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
time.sleep(1)
print("I have selected a number between 1 and 100. Can you guess what it is?")
time.sleep(1)

while isrunning:
        number = input("Please enter a number between 1 and 100: ")
        if number < 1 or number > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            time.sleep(0.5)
            continue
        if number == correct_number:
            attempts += 1
            print(f"Well done! You guessed the number, {correct_number} in {attempts} attempts.")
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                attempts = 0
                correct_number = random.randint(1, 100)
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
            print("Invalid input! Please enter a number between 1 and 100.")
            time.sleep(1)