# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
count = 0
total = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    n += 1
# 🚨 Don't change the code above 👆
x = 0
for item in student_heights:
    x += item

value = round(x / n)
print(value)
# Write your code below this row 👇
