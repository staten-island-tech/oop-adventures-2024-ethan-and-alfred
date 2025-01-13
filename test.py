class Student:
    def __init__(self, name, age, grades):
        self.name = name        # str
        self.age = age          # int
        self.grades = grades    # list of grades

# Creating an instance
student = Student(name="Alice", age=20, grades=[85, 90, 78])

print(student)
Student()