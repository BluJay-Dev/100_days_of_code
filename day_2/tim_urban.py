# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# There are 365 days in a year, 52 weeks in a year and 12 months in a year. max 90
# You have 12410 days, 1768 weeks, and 408 months left.
max_age = 90
life = max_age - int(age)
fun_dict = {'days': 365, 'weeks': 52, 'months': 12}

days = fun_dict.get('days') * life
weeks = fun_dict.get('weeks') * life
months = fun_dict.get('months') * life


print(f"You have {days} days, {weeks} weeks, and {months} months left.")
