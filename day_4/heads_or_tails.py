import random

i = input("Heads or tails? \n")

chance = random.randint(0, 1)
if chance == 0:
    x = True
    print(f"Your answer is heads")
else:
    x = False
    print("Your answer is tails")

