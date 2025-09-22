# Adapt this code to use a match instead of an if statement
# you could also:
# - make the inputs more robust
# - try and add a loop to make the program repeat (if you have done python before)



# Display the menu
while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get user choice
    choice = int(input("Enter your choice (1-5): "))

    # Process the choice using if statements

    match choice:
        case 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(result)
        case 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print(result)
        case 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(result)
        case 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("The divisor cannot be zero!")
                continue
            result = num1 / num2
            print(result)
        case 5:
            break
        case _:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue