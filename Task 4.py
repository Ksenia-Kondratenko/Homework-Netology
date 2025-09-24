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

    def average_grade(self, course=None):
        if course is None:
            # Средняя оценка по всем курсам
            all_grades = [grade for grades in self.grades_from_students.values() for grade in grades]
        else:
            # Средняя оценка по конкретному курсу
            all_grades = self.grades_from_students.get(course, [])
        if all_grades:
            return round(mean(all_grades), 1)
        return None

    # Представление информации о лекторе
    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade or 'Нет оценок'}"

    # Сравнение лекторов по средней оценке
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

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Представление информации о проверяющем
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

    def average_grade(self, course=None):
        if course is None:
            # Среднее по всем курсам
            all_grades = [grade for grades in self.grades.values() for grade in grades]
        else:
            # Среднее по конкретному курсу
            all_grades = self.grades.get(course, [])
        if all_grades:
            return round(mean(all_grades), 1)
        return None

    # добавление rate_lecture, выставление оценки лектору
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.add_grade(course, grade)
        else:
            return 'Ошибка'

    # Вывод информации о студенте
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

    # Сравнение студентов по средней оценке
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

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')

reviewer1 = Reviewer('Михаил', 'Сидоров')
reviewer2 = Reviewer('Анна', 'Кузнецова')

student1 = Student('Олег', 'Семёнов', 'Мужской')
student2 = Student('Кирилл', 'Романов', 'Мужской')

lecturer1.attach_course('Python')
lecturer2.attach_course('Python')

reviewer1.attach_course('Python')
reviewer2.attach_course('Python')

student1.courses_in_progress = ['Python']
student2.courses_in_progress = ['Python']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lecture(lecturer1, 'Python', 9.5)
student2.rate_lecture(lecturer2, 'Python', 8.5)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

print(lecturer1 > lecturer2)  # True
print(student1 > student2)    # True