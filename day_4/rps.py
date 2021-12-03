import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Write your code below this line 👇
# rock beats scissors
# paper beats rock
# scissors beats paper
# Rock = 0, paper = 1, scissors = 2
choice = int(input(f"Rock Paper Scissors\n"
                   f"0: Rock \n"
                   f"1: Paper\n"
                   f"3: Scissors\n"))
choice2 = random.randint(0, 2)
bot = [rock, paper, scissors]
print(bot[choice])
print(bot[choice2])

if choice == choice2:
    print('Draw pick again')

if choice == 0 and choice2 == 2:
    print("Rock beats paper you win!")
elif choice == 0 and choice2 == 1:
    print("Paper beats rock you lose :(")

if choice == 1 and choice2 == 2:
    print("Scissors beats Paper you lose! :(")
elif choice == 1 and choice2 == 0:
    print("Paper beats Rock you win!")

if choice == 2 and choice2 == 0:
    "Rock beats Scissors you lose! :("
elif choice == 2 and choice2 == 1:
    "Scissors beats paper you win!"
