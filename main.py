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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lections = {}

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
 

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
best_lecturer = Lecturer("Some", "Buddy")
best_lecturer.courses_attached += ['Python']

best_reviewer = Reviewer("Some", "Buddy")
best_reviewer.courses_attached += ['Python']


best_reviewer.rate_hw(best_student, "Python", 4)
best_reviewer.rate_hw(best_student, "Python", -4)

best_student.rate_hw(best_lecturer, "Python", 10)
best_student.rate_hw(best_lecturer, "Python", 112)


print(best_student.grades)
print(best_lecturer.grades_lections)