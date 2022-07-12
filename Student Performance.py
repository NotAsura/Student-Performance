import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]

#Opens the JSON files the report cards are stored in
def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

#Gets and puts the averages of each student in a array and returns it
def report_cards():
    averages = []
    for i in range(1000):
        scores = 0
        report = load_report_card("students", i)
        for j in SUBJECTS:
            scores += report[j]
        scores /= len(SUBJECTS)
        averages.append(round(scores, 2))
    return averages

#Gets the grade of every subject and puts it in a dictionary
def subject_averages():
    sub = {}
    for i in SUBJECTS:
        sub[i] = 0
    for i in range(1000):
        report = load_report_card("students", i)
        for i in SUBJECTS:
            sub[i] += report[i]
    return sub

#Finds the average grade in every subject and puts it in an dictionary
def grade_averages():
    grade = {}
    num = {}
    for i in range(1000):
        average = 0
        card = load_report_card("students", i)
        for j in SUBJECTS:
            average += card[j]
        average /= len(SUBJECTS)
        gr = card["grade"]
        grade[gr] = grade.get(gr, 0) + average
        num[gr] = num.get(gr, 0) + 1
    keys = grade.keys()
    for i in keys:
        grade[i] = grade[i] / num[i]
    return grade

#Gets the average grade of all students
def get_student_average():
    averages = report_cards()
    total = sum(averages)
    return round(total / len(averages), 2)

#Outputs the best performing student
def best_student():
    averages = report_cards()
    highest = max(averages)
    return averages.index(highest)

#Outputs the worst performing student
def worst_student():
    averages = report_cards()
    lowest = min(averages)
    return averages.index(lowest)

#Outputs the hardest subject based on average grade
def hardest_subject():
    dic = subject_averages()
    return min(dic, key=dic.get)

#Outputs the easiest subject based on average grade
def easiest_subject():
    dic = subject_averages()
    return max(dic, key=dic.get)

#Outputs the grade that had the highest average grade
def best_grade():
    grade_average = grade_averages()
    return max(grade_average, key=grade_average.get)

#Outputs the grade that had the lowest average grade
def worst_grade():
    grade_average = grade_averages()
    return min(grade_average, key = grade_average.get)

average_student = get_student_average()
hard_sub = hardest_subject()
easy_sub = easiest_subject()
b_g = best_grade()
w_g = worst_grade()
best_stu = best_student()
worst_stu = worst_student()

print(f"""Average Student Grade: {average_student}
Hardest Subject: {hard_sub}
Easiest Subject: {easy_sub}
Best Performing Grade: {b_g}
Worst Performing Grade: {w_g}
Best Student ID: {best_stu}
Worst Student ID: {worst_stu}""")