from statistics import mean

# Родительский класс преподавателя
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_course(self, course):
        self.courses_attached.append(course)

# Класс лектора (получает оценки от студентов)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def add_grade(self, course, grade):
        if course in self.grades_from_students:
            self.grades_from_students[course].append(grade)
        else:
            self.grades_from_students[course] = [grade]

    def average_grade(self, course=None):
        if course is None:
            # Среднее по всем курсам
            all_grades = [grade for grades in self.grades_from_students.values() for grade in grades]
        else:
            # Среднее по указанному курсу
            all_grades = self.grades_from_students.get(course, [])
        if all_grades:
            return round(mean(all_grades), 1)
        return None

# Класс проверяющего (ставит оценки студентам)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Класс студента (ставит оценки лекторам и получает оценки от проверяющих)
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def average_grade(self, course=None):
        if course is None:
            # Среднее по всем курсам
            all_grades = [grade for grades in self.grades.values() for grade in grades]
        else:
            # Среднее по указанному курсу
            all_grades = self.grades.get(course, [])
        if all_grades:
            return round(mean(all_grades), 1)
        return None

# Функция подсчета средней оценки за домашние задания по всем студентам на одном курсе
def average_home_work_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return round(mean(grades), 1)
    return None

# Функция подсчета средней оценки за лекции всех лекторов на одном курсе
def average_lecture_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades_from_students:
            grades.extend(lecturer.grades_from_students[course])
    if grades:
        return round(mean(grades), 1)
    return None

# Экземпляры классов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')

reviewer1 = Reviewer('Михаил', 'Сидоров')
reviewer2 = Reviewer('Анна', 'Кузнецова')

student1 = Student('Руой', 'Еман', 'Мужской')
student2 = Student('Кирилл', 'Романов', 'Мужской')

# Привяжем курсы
lecturer1.attach_course('Python')
lecturer2.attach_course('Python')

reviewer1.attach_course('Python')
reviewer2.attach_course('Python')

student1.courses_in_progress = ['Python']
student2.courses_in_progress = ['Python']

# Проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)

# Студенты оценивают лекции
student1.add_grade('Python', 9.5)
student2.add_grade('Python', 8.5)

lecturer1.add_grade('Python', 9.5)
lecturer2.add_grade('Python', 8.5)

# Подсчёт средней оценки за домашние задания и лекции
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

hw_avg = average_home_work_grade(students, 'Python')
lecture_avg = average_lecture_grade(lecturers, 'Python')

print(hw_avg)          # Средняя оценка за домашнюю работу
print(lecture_avg)     # Средняя оценка за лекции