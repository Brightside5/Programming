import math

class Shape:
    def __init__(self):
        self.shape = 'shape'
        


# define a Circle class that inherits from Shape class.
# this class has the following field and methods:
# (1) radius
# (2) __init__(self, radius) - initialise the radius and update the value of shape to "circle"
# (3) area(self) - returns the area of a circle based on the radius
#     area = math.pi * radius * radius
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.shape = 'circle'

    def area(self):
        return math.pi * self.radius * self.radius




# define a Rectangle class that inherits from Shape class.
# this class has the following fields and methods:
# (1) width
# (2) height
# (3) __init__(self, width, height) - initialise width and height and update the value of shape to "rectangle"
# (4) area(self) - returns the area of a rectangle
#     area = width * height
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape = 'rectangle'

    def area(self):
        return self.width * self.height




# once done, create an instance of Circle and Rectangle and 
# print the area for both instances
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")
