def multiply():
    first = int(input("Pick a number: "))
    second = int(input("Pick a second number: "))
    return first * second


def format_name():
    first_name = str(input("First Name: "))
    second_name = str(input("Second Name: "))
    if first_name == "" or second_name == "":
        return "Stupid bitch"
    f_name = f"{first_name.title()} {second_name.title()}"
    return f_name


output = multiply()
print(output)
name = format_name()
print(name)
