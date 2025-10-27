# Create an updated version of the Rectangle class from activity1/task2 with the following methods:
# (1) area method to return the area of a rectangle
# (2) perimeter method to return the perimeter of a rectangle

class Rectangle:
    def __init__(self, wid, high):
        if wid < 0 or high < 0:
            raise ValueError("Width and height cannot be negative")
        self.height = high
        self.width = wid

    def set_height(self, high):
        if high < 0:
            raise ValueError("Height cannot be negative")
        self.height = high

    def set_width(self, wid):
        if wid < 0:
            raise ValueError("Width cannot be negative")
        self.width = wid

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)




# Once completed, create 2 instances of Rectangles with:
# (1) first rectangle with width = 4 and height = 40
# (2) second rectangle with width = 3.5 and height=35.9
# After that, print the area and perimeter of both rectangle instances.

rectangle1 = Rectangle(4,40)
rectangle2 = Rectangle(3.5,35.9)

print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle2.area())
print(rectangle2.perimeter())

# Did you have setters with validation? Can the value of width and height be negative?
# If you have not, update the setters with validation for the width and height.
