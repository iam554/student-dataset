import csv
import random

departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Economics"]
levels = [100, 200, 300, 400]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID", "Department", "Level", "Attendance Percentage", "Average Examination Score"])
    for i in range(1, 101):
        student_id = "STU" + str(i).zfill(4)
        department = random.choice(departments)
        level = random.choice(levels)
        attendance = random.randint(50, 100)
        score = round(random.uniform(35, 100), 1)
        writer.writerow([student_id, department, level, attendance, score])

print("students.csv created with 100 students")
