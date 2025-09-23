# Основной класс преподавателя
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Закрепленные курсы

    def attach_course(self, course):
        """Метод добавляет курс к списку прикрепленных курсов."""
        self.courses_attached.append(course)

# Класс лектора (читается лекции, но не проверяет задания)
class Lecturer(Mentor):
    pass  # Ничего дополнительного не добавляем пока

# Класс эксперта-проверяющего (ставит оценки студентам)
class Reviewer(Mentor):
    pass  # Ничего дополнительного не добавляем пока

# Создаем объекты
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

# Проверяем принадлежность к классу Mentor
print(isinstance(lecturer, Mentor))  # Должно вывести True
print(isinstance(reviewer, Mentor))  # Должно вывести True

# Показываем прикрепленные курсы (их изначально нет)
print(lecturer.courses_attached)     # Должно вывести пустой список []
print(reviewer.courses_attached)     # Должно вывести пустой список []