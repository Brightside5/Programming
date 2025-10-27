class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Given a Point class, define the __str__ and __repr__ methods
    def __str__(self):
        return f"x:{self.x},y:{self.y}"
    
    def __repr__(self):
        return f"Point('x:{self.x},y:{self.y}')"