from dicts import drinks, money


def get_drinks():
    choice = input(f'What would you like? (espresso/latte/cappuccino): ')
    print(f"A {choice} costs ${drinks.get(choice)['Price']}")
    total = 0
    for key in money:
        money_accepted = float(input(f"How many {key}?:"))
        new_money = money_accepted * money[key]
        total += new_money
        change = total - drinks.get(choice)['Price']
    if total < drinks.get(choice)['Price']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change")
        print(f"Here is your {choice}. Enjoy!")


get_drinks()
