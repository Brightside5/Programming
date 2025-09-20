#task_c
import sys
from util import read_numbers

#Get the numbers
numbers = read_numbers()

#If no number in the list
if not numbers:
    sys.exit("Error: no numbers provided")

#Calculte
min_value = min(numbers)
max_value = max(numbers)
mean_value = sum(numbers) / len(numbers)

#Get the median
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)

if n%2 == 1:
    median_value = sorted_numbers[n // 2]

else:
    median_value1 = sorted_numbers[n // 2]
    median_value2 = sorted_numbers[n // 2 - 1]
    median_value = (median_value1 + median_value2) / 2

#print out the result
print(f"Minimum = {min_value}")
print(f"Maximum = {max_value}")
print(f"Mean    = {mean_value}")
print(f"Median  = {median_value}")