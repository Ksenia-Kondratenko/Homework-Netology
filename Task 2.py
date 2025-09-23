# Родительский класс преподавателя
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Закрепленные курсы

    def attach_course(self, course):
        """Метод добавляет курс к списку прикрепленных курсов."""
        self.courses_attached.append(course)

# Класс лектора (получает оценки от студентов)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки от студентов

# Класс проверяющего (ставит оценки студентам)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Поставить оценку студенту за выполненное домашнее задание.
        Проверяется, что студент находится на курсе и курс прикреплен к данному эксперту.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Класс студента (ставит оценки лекторам и проходит обучение)
class Student:
    def __init__(self, last_name, first_name, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # Оценки от проверяющих

    def rate_lecture(self, lecturer, course, grade):
        """
        Метод для выставления оценки лектору.
        Проверяются условия: студент должен учиться на указанном курсе,
        а лектор должен вести указанный курс.
        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Тестовые данные
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# Курсы, которыми занимается студент и прикреплены к преподавателям
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Выполнение тестов
print(student.rate_lecture(lecturer, 'Python', 7))   # Допустимая оценка, вернет None
print(student.rate_lecture(lecturer, 'Java', 8))     # Недоступный курс для лектора, ошибка
print(student.rate_lecture(lecturer, 'C++', 8))      # Курс не изучается студентом, ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Неправильный тип преподавателя, ошибка

# Проверка оценок лектора
print(lecturer.grades)  # {'Python': [7]}