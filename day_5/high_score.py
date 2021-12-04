# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
x = 0
for i in student_scores:
    count = i
    if i > x:
        x = i

print(i)
