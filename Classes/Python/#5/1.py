# 1.Define a Student Class:
# Define a class named Student with the following attributes:
# name: Name of the student (string).
# age: Age of the student (int).
# grade: Grade level of the student (int).
class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

    # 2.Add Methods:
    # Add the following methods to the Student class:
    # get_info( ): Method to display the student's information.
    # promote ( ): Method to promote the student to the next grade level.
    def get_info(self):
        print(f"Student name:{self.name} Age:{self.age} Grade:{self.grade}")

    def promote(self):
        self.grade += 1


# 3.Test the Class:
# Create instances of the Student class and test its methods:
# Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
# Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information.

student_anna = Student("Anna", 15, 9)
student_anna.get_info()
student_anna.promote()
student_anna.get_info()
