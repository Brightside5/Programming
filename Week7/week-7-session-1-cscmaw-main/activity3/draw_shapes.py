# write code to import the shapes module
import shapes


# write code to create an instance of Circle and then a call the draw method
circle1 = shapes.Circle(2)
circle1.draw()

# write code to create an instance of Rectangle and then a call to the draw method
rectangle1 = shapes.Rectangle(5,2)
rectangle1.draw()

# write code to create an instance of Square and then a call to the draw method
square = shapes.Square(5)
square.draw()

# write code to create an instance of Triangle and then a call to the draw method
triangle1 = shapes.Triangle(3)
triangle1.draw()





# Notice how you have to use shapes.Circle, shapes.Rectangle, shapes.Square, etc...
# when you create instances of different classes from the shape module? Wouldn't
# it be nice if you don't need to do it that way and simply use Circle, Rectangle, etc...?

# The answer is yes, we can do that with "from ... import". In this example
# we can put "from shapes import Circle, Rectangle, Square, Triangle"
# and then proceed to use Circle, Rectangle, etc... when creating instances of those
# classes. 

# You can now update your code to reflect on this change.
