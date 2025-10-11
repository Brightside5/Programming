# Week 4, Session 1: Task 4

# You are given an incomplete function count_occurences with docstring.
# Your task is to complete the function that takes two arguments:
#   (1) a list of string
#   (2) a string to search.

# This function returns the number of times a string appears in the list.
# This function is restricted to only accept positional arguments.
# Test the function with different list of strings and string to search


def count_occurences(l_strings, target, /):
    """
    Count how many times target appears in the list l_strings.

    Returns:
        int: number of occurences of target in l_strings.
    """

    # Complete your code here
    count = 0
    for item in l_strings:
        if item == target:
            count += 1
    return count


# Write code to call the function and check if 
# correct output is produced
print(count_occurences(["apple", "banana", "apple", "cherry"], "apple"))  # Expected: 2
print(count_occurences(["hello", "world", "hello"], "hello"))  # Expected: 2
print(count_occurences(["a", "b", "c"], "d"))  # Expected: 0
print(count_occurences("a", ["a", "b", "c"]))