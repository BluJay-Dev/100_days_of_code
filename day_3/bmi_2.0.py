# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(int(weight) / (float(height) ** 2))
bmi_sent = f"Your BMI is {bmi}, "
if bmi < 18.5:
    print(f"{bmi_sent}you are underweight")
elif 18.5 < bmi < 25:
    print(f"{bmi_sent}you have a normal weight")
elif 25 < bmi < 30:
    print(f"{bmi_sent}you are slightly overweight.")
elif 30 < bmi < 35:
    print(f"{bmi_sent}you are obese.")
elif bmi < 35:
    print(f"{bmi_sent}you are clinically obese.")
