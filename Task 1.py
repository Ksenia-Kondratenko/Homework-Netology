class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_course(self, course):
        self.courses_attached.append(course)

class Lecturer(Mentor):
    pass  

class Reviewer(Mentor):
    pass  

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True

print(lecturer.courses_attached)     # пустой список []
print(reviewer.courses_attached)     # пустой список []