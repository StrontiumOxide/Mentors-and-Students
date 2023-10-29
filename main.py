from cls_def import Student, Lecturer, Reviewer, average_grade_homework, average_grade_lections
from random import randint


list_students = [
    Student("Denis", "Dorofeev", "Male"),
    Student("Lera", "Savkina", "Female")
]

list_lecturers = [
    Lecturer("Nikita", "Lol"),
    Lecturer("Sergey", "Zorin")
]

list_reviewers = [
    Reviewer("Albert", "Cool"),
    Reviewer("Dima", "Good")
    ]

list_courses = ["Python", "Git", "JavaScript"]

    # Циклы для добавления студентов на курсы и выставление  случайных оценок студентам и лекторам
for reviewer in list_reviewers:
    for student in list_students:
        for lecturer in list_lecturers:
            for course in list_courses:
                if course not in student.courses_in_progress:
                    student.courses_in_progress.append(course)
                if course not in reviewer.courses_attached:
                    reviewer.courses_attached.append(course)
                if course not in lecturer.courses_attached:
                    lecturer.courses_attached.append(course)
                
                reviewer.rate_hw(student, course, randint(1,10))
                student.rate_hw(lecturer, course, randint(1,10))


for course in list_courses:
    print(f"Средняя оценка по домашним заданиям по курсу {course} равна {average_grade_homework(list_students, course)}")
    print(f"Средняя оценка за лекции по курса {course} равна {average_grade_lections(list_lecturers, course)}")
    print()