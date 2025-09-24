from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_course(self, course):
        self.courses_attached.append(course)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def add_grade(self, course, grade):
        if course in self.grades_from_students:
            self.grades_from_students[course].append(grade)
        else:
            self.grades_from_students[course] = [grade]

    def average_grade(self):
        # средняя оценка по всем курсам
        all_grades = [grade for grades in self.grades_from_students.values() for grade in grades]
        if all_grades:
            return round(mean(all_grades), 1)
        return None

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade or 'Нет оценок'}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

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

    def average_grade(self):
        # средняя оценка по всем курсам
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return round(mean(all_grades), 1)
        return None

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade or 'Нет оценок'}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    # добавление rate_lecture для выставления оценки лектору
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.add_grade(course, grade)
        else:
            return 'Ошибка'

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')

student1 = Student('Ольга', 'Иванова', 'Женский')
student2 = Student('Кирилл', 'Романов', 'Мужской')

lecturer1.attach_course('Python')
lecturer2.attach_course('Python')

student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python']
student2.finished_courses = ['Основы программирования']

# Студент Ольга Иванова ставит оценку лектору Ивану Иванову
student1.rate_lecture(lecturer1, 'Python', 9.5)

# Студент Кирилл Романов ставит оценку лектору Петру Петрову
student2.rate_lecture(lecturer2, 'Python', 8.5)

print(lecturer1.grades_from_students)  # {'Python': [9.5]}
print(lecturer2.grades_from_students)  # {'Python': [8.5]}

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

# Сравнение
print(lecturer1 > lecturer2)  # True
print(student1 > student2)    # Нет оценок, поэтому сравнение невозможно