from art import logo
import random


def number_gen():
    num = random.randint(0, 100)
    return num


def guess(lives):
    print(lives)
    random_num = number_gen()
    while lives > 0:
        g_num = int(input("Pick a number between 1 and 100: "))
        if g_num == random_num:
            print(f"You win! Number was {random_num} and you guessed {g_num}")
            end_of_game = True
            return end_of_game
        elif g_num > random_num:
            print("Too high!")
            lives -= 1
        elif g_num < random_num:
            print("Too low")
            lives -= 1
    if lives == 0:
        print('Game over biatch')


difficulty = input("Would you like to play easy 'e' or hard 'h': ")
if difficulty == 'e':
    print(logo)
    guess(lives=10)
elif difficulty == 'h':
    print(logo)
    guess(lives=5)
