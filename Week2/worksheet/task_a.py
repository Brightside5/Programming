#task_a
import sys

try:
    #Get the grade number
    grade = int(input())

#If grade is not a number
except ValueError:
    print("Error: Grade must be an integer between 0 and 100") #To display the error message
    sys.exit("Error!")

#If grade is not in the range
if not (0 <= grade <= 100):
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit("Error!")

#get the result
if grade >= 70:
    result = "Distinction"

elif 40 <= grade <70:
    result = "Pass"

else:
    result = "Fail"

print(f"{grade} is a {result}")