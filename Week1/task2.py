"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Hangming Hu
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

RATE = 0.008

try:
    #get the money saved every month
    money = int(input())
    
    total_money = money * 12
    #Calculate the interest
    interest = total_money * RATE
    #Calculate the total money
    final_money = total_money + interest

    print(total_money)
    print(f"£{final_money:.2f}")

except ValueError:
    print("Invalid amount")