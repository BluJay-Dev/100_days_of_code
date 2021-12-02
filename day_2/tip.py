import os

def tip_calculator():
    print("Welcome to the tip calculator!")
    bill = input("What was the total bill $")
    peeps = input("How many people split the bill? ")
    percent = input("What percentage tip would you like to give? 10, 12 or 15: ")
    total = float(bill)/float(peeps)
    tip = total / float(percent)
    final = total + tip
    print(f"Each person should pay: {final}")


tip_calculator()

