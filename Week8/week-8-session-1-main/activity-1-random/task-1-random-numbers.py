# We need to import the library in order to use in in Python
import random

# And you have a series of short tasks to complete - remember to run your program to check that they are working!

''' Task A

You have been given a little bit of unfinished code to complete and add to.

- Generate 3 random numbers between 0 and 100 and print them out
- Comment and uncomment 'random.seed(10)'
- Run your program with it commented and with it uncommented.
- Write a comment explaining what you think it is doing.
- confirm this by changing the value in the brackets.
'''

# random.seed(10) sets a seed for the random number generator, making the sequence reproducible for testing.
random.seed(10)

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
num3 = random.randint(0, 100)

print(f"{num1} ~ {num2} ~ {num3}")




''' Task B
- Ask the user to enter a positive integer, and generate that many random numbers.
- Optionally: save these into a file called 'random.txt'
'''

# Ask user for a positive integer
n = int(input("Enter a positive integer: "))

# Generate n random numbers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(n)]

# Print the numbers
print("Generated random numbers:", random_numbers)

# Optionally save to file
save_to_file = input("Do you want to save these to 'random.txt'? (y/n): ").lower()
if save_to_file == 'y':
    with open('random.txt', 'w') as f:
        for num in random_numbers:
            f.write(f"{num}\n")
    print("Numbers saved to 'random.txt'")



