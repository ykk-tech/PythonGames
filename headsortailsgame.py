import random
import time

# ask player for guess
guess = input("heads or tails? (heads = 1, tails = 2): ").strip().lower()

# convert '1' or 'heads' to 1, '2' or 'tails' to 2
if guess in ["1", "heads"]:
    guess_num = 1
elif guess in ["2", "tails"]:
    guess_num = 2
else:
    print("invalid choice! please choose heads (1) or tails (2).")
    exit()

# show the coin flip message
print("flipping the coin...")
time.sleep(2)

# randomly decide the result
result = random.randint(1, 2)

# announce if they got it right or wrong
if guess_num == result:
    print(f"correct, the answer was indeed {'heads' if result == 1 else 'tails'}!")
else:
    print(f"incorrect, the answer was {'heads' if result == 1 else 'tails'}.")