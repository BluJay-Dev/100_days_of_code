# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_names = len(names - 1)
num = random.randint(0, total_names)

print(f"{names[num]} is paying the bill")
