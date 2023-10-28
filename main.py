from cls import Student, Lecturer, Reviewer
from random import randint


best_student = Student('Denis', 'Dorofeev', 'your_gender')
best_student.courses_in_progress.append("Python")
best_student.courses_in_progress.append("Git")
best_student.finished_courses.append("Введение в программирование")
worst_student = Student('Lera', 'Savkina', 'your_gender')
worst_student.courses_in_progress.append("Python")
worst_student.courses_in_progress.append("Git")
worst_student.finished_courses.append("Введение в программирование")

best_lecturer = Lecturer("Nikita", "Buddy")
best_lecturer.courses_attached.append("Python")
best_lecturer.courses_attached.append("Git")
worst_lecturer = Lecturer("Erik", "Lol")
worst_lecturer.courses_attached.append("Python")
worst_lecturer.courses_attached.append("Git")

best_reviewer = Reviewer("Some", "Buddy")
best_reviewer.courses_attached.append("Python")
best_reviewer.courses_attached.append("Git")

for i in range(11):
    best_student.rate_hw(best_lecturer, "Python", randint(-10, 10))
    best_student.rate_hw(worst_lecturer, "Python", randint(-10, 10))
    worst_student.rate_hw(best_lecturer, "Python", randint(-10, 10))
    worst_student.rate_hw(worst_lecturer, "Python", randint(-10, 10))

    best_student.rate_hw(best_lecturer, "Git", randint(-10, 10))
    best_student.rate_hw(worst_lecturer, "Git", randint(-10, 10))
    worst_student.rate_hw(best_lecturer, "Git", randint(-10, 10))
    worst_student.rate_hw(worst_lecturer, "Git", randint(-10, 10))

    best_reviewer.rate_hw(best_student, "Python", randint(-10, 10))
    best_reviewer.rate_hw(worst_student, "Python", randint(-10, 10))

    best_reviewer.rate_hw(best_student, "Git", randint(-10, 10))
    best_reviewer.rate_hw(worst_student, "Git", randint(-10, 10))


print(best_reviewer)
print()
print(best_lecturer)
print()
print(worst_lecturer)
print()
print(best_student)
print()
print(worst_student)
print()
print(f"Лектор {best_lecturer.name} лучше лектора {worst_lecturer.name}. И это {best_lecturer > worst_lecturer}")
print(f"Студент {best_student.name} лучше студента {worst_student.name}. И это {best_student > worst_student}")