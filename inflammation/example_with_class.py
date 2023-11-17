import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius
    

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

my_circle = Circle(10)
print(my_circle.get_area())

your_rectangle = Rectangle(20, 20)
print(your_rectangle.get_area())

shapes = [my_circle, your_rectangle]

for shape in shapes:
    print(shape.get_area())