import math


# Polymorphism
# Create a Python program that explores polymorphism using a hierarchy of shapes. Start with a base
# class Shape, and then create two or more derived classes (e.g., Circle, Rectangle, Triangle) that
# inherit from the Shape class. Each shape class should have its own implementation of methods like
# area() and perimeter(). These methods will calculate the area and perimeter of the respective shape.
# 1. Define the Shape base class with methods like area() and perimeter(). You can initialize any
# common attributes in the base class.
class Shape:
    pi = math.pi

    def __init__(self):
        pass

    def area(self):
        return "Area of"

    def perimeter(self):
        return "Perimeter of"


# 2. Create derived classes for different shapes, e.g., Circle, Rectangle, and Triangle. Each derived
# class should inherit from the Shape base class and implement its own version of the area()
# and perimeter() methods.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.areaOfCirle = self.radius * self.radius * Shape.pi
        print(f"{super().area()} Circle:{self.areaOfCirle:.2f}")

    def perimeter(self):
        self.perimeterOfCirle = 2 * self.radius * Shape.pi
        print(f"{super().perimeter()} Circle:{self.perimeterOfCirle:.2f}")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        self.areaOfRectangle = self.a * self.b
        print(f"{super().area()} Rectangle:{self.areaOfRectangle:.2f}")

    def perimeter(self):
        self.perimeterOfRectangle = (2 * self.a) + (2 * self.b)
        print(f"{super().perimeter()} Rectangle:{self.perimeterOfRectangle:.2f}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        self.areaOfTriangle = 1 / 2 * self.base * self.height
        print(f"{super().area()} Triangle:{self.areaOfTriangle:.2f}")

    def perimeter(self):
        self.perimeterOfTriangle = 3 * self.base
        print(f"{super().perimeter()} Triangle:{self.perimeterOfTriangle:.2f}")


# 3. Implement specific methods for each derived class. For example, the Circle class might have a
# method to calculate its area based on the radius, and the Rectangle class could have a
# method to calculate its area based on length and width.
# Create instances of each shape type and demonstrate the use of polymorphism by calling the
# area() and perimeter() methods on them

circle1 = Circle(4)
circle1.area()
circle1.perimeter()

rectangle1 = Rectangle(3, 4)
rectangle1.area()
rectangle1.perimeter()

circle1 = Triangle(4, 7)
circle1.area()
circle1.perimeter()
