# Your task is to:
# - add support for squares (area = side length * side length)
# - add support for some other 2D polygon and test it (trapezoid, rhombus, etc)
# CHALLENGE - only if you finish all tasks - create a version of this code which asks users to enter their own shape,
#             and based on what they enter, ask for the needed dimensions to calculate area.


while True:
    shape_name = input("Enter the shape (circle, rectangle, triangle, square, trapezoid) or 'quit' to exit: ").lower()
    if shape_name == 'quit':
        break
    match shape_name:
        case "circle":
            radius = float(input("Enter the radius: "))
            area = 3.14 * radius ** 2
            print(f"The area of the circle with radius {radius} is {area:.2f}")
        case "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            area = width * height
            print(f"The area of the rectangle with width {width} and height {height} is {area:.2f}")
        case "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            area = 0.5 * base * height
            print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")
        case "square":
            side_length = float(input("Enter the side length: "))
            area = side_length * side_length
            print(f"The area of the square with side length {side_length} is {area:.2f}")
        case "trapezoid":
            upper_base = float(input("Enter the upper base: "))
            bottom_base = float(input("Enter the bottom base: "))
            height = float(input("Enter the height: "))
            area = (upper_base + bottom_base) * height / 2
            print(f"The area of the trapezoid with upper base {upper_base} and bottom base {bottom_base} and height {height} is {area:.2f}")
        case _:
            print("Unknown shape.")
