class Student:
    name="456"
    def __init__(self, name, age):
        self.__name = name
        self.age = age


def print_student_details(self):
    print(self.__name)
    print(self.age)


s = Student(“Rohan”, 20)
print(Student.name)
