import math

# Define a class Coordinate with fields x and y. The value to these fields
# are passed to the __init__ method when an instance of Coordinate is created.
# Define a setter method for x and for y, which only accept numbers.
# Then, define a method called distance. The distance method should take
# another instance of Coordinate as an argument and returns the distance between 
# the two coordinates. The formula to find the distance between the two coordinates,
# distance = √((x2 – x1)² + (y2 – y1)²). You can use math.sqrt() function for the square root

class Coordinate:
    def __init__(self,x,y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("x and y must be numbers")
        self.x = x
        self.y = y

    def set_x(self,x):
        if not isinstance(x, (int, float)):
            raise ValueError("x must be a number")
        self.x = x

    def set_y(self,y):
        if not isinstance(y, (int, float)):
            raise ValueError("y must be a number")
        self.y = y

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def slope(self, other):
        if other.x == self.x:
            raise ValueError("Slope is undefined (vertical line)")
        return (other.y - self.y) / (other.x - self.x)

# Once completed, create two instances of Coordinates:
# coordinate1 with x = 3, y = 4
# coordinate2 with x = 9, y = 12
# and print the distance between coordinate1 and coordinate2
# with the distance method in both coordinates. Are they the same?
coordinate1 = Coordinate(3, 4)
coordinate2 = Coordinate(9, 12)

print(f"Distance from coordinate1 to coordinate2: {coordinate1.distance(coordinate2)}")
print(f"Distance from coordinate2 to coordinate1: {coordinate2.distance(coordinate1)}")  # They are the same

# Once you have completed with the distance method, update the class definition with
# another method called slope to calculate the slope between the two coordinates.
# The formula for slop is (y2 - y1) /( x2 - x1). Then, print the slopes between the two coordinates
# you have created previously.
print(f"Slope from coordinate1 to coordinate2: {coordinate1.slope(coordinate2)}")
print(f"Slope from coordinate2 to coordinate1: {coordinate2.slope(coordinate1)}")  # Note: slope is negative reciprocal
