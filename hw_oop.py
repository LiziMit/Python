class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_curses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def sum_gr(self, grades, lesson_type):
        return sum(grades[lesson_type]) / len(grades[lesson_type])
    def __str__(self):
        lesson_type = input('Введите название лекции: ')
        cours_prog = ', '.join(self.courses_in_progress)
        if lesson_type in self.courses_in_progress:
            res = f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.sum_gr(self.grades, lesson_type)}\n Курсы в процессе изучения: {cours_prog}\n Завершенные курсы: Введение в программирование'
            return res
        else:
            return print(self)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    grades = {}
    def sum_gr(self, grades, lesson_type):
        return sum(grades[lesson_type]) / len(grades[lesson_type])
    # return sum(sum(value) for value in grades.values()) / len(grades[lesson_type])
    def __str__(self):
        lesson_type = input('Введите название лекции: ')
        if lesson_type in self.courses_attached:
            res = f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.sum_gr(self.grades, lesson_type)}'
            return res
        else:
            return print(self)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}'
        return res
    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


peter = Student('Пётр', 'Павлов', 'м')
peter.courses_in_progress += ['Python']
peter.courses_in_progress += ['Git']
kris = Student('Кристина', 'Степанова', 'ж')
kris.courses_in_progress += ['Python']
kris.courses_in_progress += ['Git']

nik = Lecturer('Николай', 'Семёнович')
nik.grades = {}
nik.courses_attached += ['Python']
sam = Lecturer('sam', 'sam')
sam.grades = {}
sam.courses_attached += ['Python']
sam.courses_attached += ['Git']

vladimir = Reviewer ('Владимир', 'Иванович')
vladimir.courses_attached += ['Python']
ivan = Reviewer ('Иван', 'Иванович')
ivan.courses_attached += ['Git']


peter.rate_lect(nik, 'Python', 9)
peter.rate_lect(nik, 'Python', 10)

peter.rate_lect(sam, 'Python', 9)
peter.rate_lect(sam, 'Python', 10)
kris.rate_lect(nik, 'Git', 9)
kris.rate_lect(nik, 'Git', 9)

vladimir.rate_stud(peter, 'Python', 9)
vladimir.rate_stud(peter, 'Python', 8)
ivan.rate_stud(kris, 'Git', 10)
ivan.rate_stud(kris, 'Git', 10)
  

# print(peter)
# print(kris)
# print(peter.sum_gr(sam.grades, 'Git'))
# print(nik.sum_gr(nik.grades, 'Python'))

# print(nik.__dict__)
# print(peter.__dict__)
# print(vladimir.checking_hw('peter', 'Python', 'дз1'))