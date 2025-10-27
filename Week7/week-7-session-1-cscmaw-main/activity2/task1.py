# Define a Circle class with a single field named radius. The value for radius is passed
# when an instance of Circle is created. In this class, define the following methods:
# (1) get_radius to return the radius of the circle
# (2) perimeter to return the perimeter of the circle, perimeter = 2 * Pi * radius (you can set Pi = 3.142)
# (3) area to return the area of a circle, area = Pi * radius * radius
# (4) set_radius to set the radius of the circle, with validation (radius must be a non-negative number)

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        pi = 3.142
        return 2 * pi * self.radius

    def area(self):
        pi = 3.142
        return pi * self.radius * self.radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

# Once completed, create two instances of Circle with different radius, eg 4.5, 10.8
# and print the radius, perimeter, and area for both instances
circle1 = Circle(4.5)
circle2 = Circle(10.8)

print(f"Circle 1 - Radius: {circle1.get_radius()}, Perimeter: {circle1.perimeter()}, Area: {circle1.area()}")
print(f"Circle 2 - Radius: {circle2.get_radius()}, Perimeter: {circle2.perimeter()}, Area: {circle2.area()}")

# Did you create a setter for radius? Can the radius be a negative number?
# If you have not, create a setter for radius with validation.
# Yes, added set_radius with validation to prevent negative radius.
