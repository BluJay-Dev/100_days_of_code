from art import logo

print(logo)
f_num = input("First number: ")
print(f"+\n-\n/\n*")
device = input(f"Pick an operator: ")
s_num = input(f"Second number: ")
should_continue = True


def calculator(f_number, thing, s_number):
    while should_continue:
        expression = f_number + thing + s_number
        answer = eval(expression)
        keep_going = input(f"Should we keep going with {answer} Y / N\n")
        if keep_going == 'N':
            return should_continue == False
        elif keep_going == 'Y':
            return answer


calculator(f_num, device, s_num)
