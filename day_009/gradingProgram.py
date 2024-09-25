student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def getGrade(number):
    grade = ""
    if 91 <= number <= 100:
        grade = "Outstanding"
    elif 81 <= number <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= number <= 80:
        grade = "Acceptable"
    elif 0 <= number <= 79:
        grade = "Fail"
    else:
        grade = "invalid grade"
    return grade

student_grades = {}

for i in student_scores:
    student_grades[i] = getGrade(student_scores[i])

