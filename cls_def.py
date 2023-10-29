class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
            and grade >= 0 and grade <=10):
            
            if course in lecturer.grades_lections:
                lecturer.grades_lections[course] += [grade]
            else:
                lecturer.grades_lections[course] = [grade]
        else:
            return "Ошибка"
        
    def __gt__(self, other):
        return average_grade(self.grades) > average_grade(other.grades) 
       
    def __str__(self):
        result = (
            "Студент\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade(self.grades)} \n"
            f"Курсы в процессе прохождения: {', '.join(self.courses_in_progress)} \n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )
        return result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lections = {}

    def __str__(self):
        result = (
            "Лектор\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average_grade(self.grades_lections)}"
        )
        return result
    
    def __gt__(self, other):
        return average_grade(self.grades_lections) > average_grade(other.grades_lections)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) 
            and course in self.courses_attached
            and course in student.courses_in_progress
            and grade >= 0 and grade <=10):

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
                
    def __str__(self):
        result = (
            "Эксперт\n"
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )
        return result
 
    # Функция для нахождения средней оценки по всем курсам
def average_grade(dict_grades: dict):
    average_grades = []
    for list_grades in dict_grades.values():
        for grade in list_grades:
            average_grades.append(grade)
    return round((sum(average_grades)/len(average_grades)), 2)

    # Функция для нахождения средней оценки по всем домашним заданиям в пределах курса
def average_grade_homework(list_students: list, course: str):
    average_grades = []
    for student in list_students:
        for grade in student.grades[course]:
            average_grades.append(grade)
    return round((sum(average_grades)/len(average_grades)), 2)

    # Функция для нахождения средней оценки за лекции в пределах одного курса
def average_grade_lections(list_lecturer: list, course: str):
    average_grades = []
    for lecturer in list_lecturer:
        for grade in lecturer.grades_lections[course]:
            average_grades.append(grade)
    return round((sum(average_grades)/len(average_grades)), 2)

    



