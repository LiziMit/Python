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
    def sum_gr(self):
        lesson_type = input('Введите название лекции: ')
        grades = self.grades
        if lesson_type not in self.grades.keys():
            return ('Оценок по данному предмету нет')
        else:
            return sum(grades[lesson_type]) / len(grades[lesson_type])
    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            print('Требуется ввести одинаковое название лекции каждому сравниваемуму объекту'.upper())
            compare = self.sum_gr() < other_student.sum_gr()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            return compare
    def __str__(self):
        cours_prog = ', '.join(self.courses_in_progress)
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекцию: {self.sum_gr()}\n Курсы в процессе изучения: {cours_prog}\n Завершенные курсы: {" ".join(self.finished_curses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    grades = {}
    def sum_gr_lect(self):
        lesson_type = input('Введите название лекции: ')
        grades = self.grades
        if lesson_type not in self.grades.keys():
            return ('Оценок по данному предмету нет')
        else:
            return sum(grades[lesson_type]) / len(grades[lesson_type])
    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            print('Требуется ввести одинаковое название лекции каждому сравниваемуму объекту'.upper())
            compare = self.sum_gr_lect() < other_lecturer.sum_gr_lect()
            if compare:
                print(f'{self.name} {self.surname} ведёт хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{self.name} {self.surname} ведёт лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            return compare
    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за ведение лекции: {self.sum_gr_lect()}'

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
peter.finished_curses += ['Введение в программирование']
kris = Student('Кристина', 'Степанова', 'ж')
kris.courses_in_progress += ['Python']
kris.courses_in_progress += ['Git']
kris.finished_curses += ['Введение в программирование']

nik = Lecturer('Николай', 'Семёнович')
nik.grades = {}
nik.courses_attached += ['Python']
sam = Lecturer('Семён', 'Михайлович')
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
kris.rate_lect(sam, 'Git', 9)
kris.rate_lect(sam, 'Git', 9)

vladimir.rate_stud(peter, 'Python', 9)
vladimir.rate_stud(peter, 'Python', 8)
vladimir.rate_stud(kris, 'Python', 8)
vladimir.rate_stud(kris, 'Python', 8)
ivan.rate_stud(peter, 'Git', 10)
ivan.rate_stud(peter, 'Git', 9)
ivan.rate_stud(kris, 'Git', 10)
ivan.rate_stud(kris, 'Git', 8)
  
# print(peter < kris)
# print(nik < sam)
# print(peter)
# print(kris)
# print(nik)
# print(peter.sum_gr())
# print(sam.sum_gr_lect())
# print(nik.sum_gr_lect())
# print(sam.__dict__)
# print(peter.__dict__)

def hw_grade(student_list, course):
    counter = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                counter += sum(grades) / len(grades)
    return round(counter / len(student_list), 2)
# print(hw_grade([peter, kris], 'Python'))

def lec_grade(lector_list, course):
    counter = 0
    for lector in lector_list:
        for k, grades in lector.grades.items():
            if k == course:
                counter += sum(grades) / len(grades)
    return round(counter / len(lector_list), 2)
# print(lec_grade([nik, sam], 'Python'))

