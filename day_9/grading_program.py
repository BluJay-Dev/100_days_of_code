import pprint

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = student_scores

# TODO-2: Write your code below to add the grades to student_grades.👇
# 91 - 100: Grade = "Outstanding"
# 81 - 90: Grade = "Exceeds Expectations"
# 71 - 80: Grade = "Acceptable"
# 70 or lower: Grade = "Fail"
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif 80 < score < 91:
        student_grades[student] = 'Exceeds Expectations'
    elif 70 < score < 81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = 'Fail'
# 🚨 Don't change the code below 👇
pprint.pprint(student_grades)

