# Checks the validity of a University of Leeds student username

import re
import sys

# Usage: python username.py <username>

# UoL usernames for students starting in the 24/25 session should be of the form
#  [ 4 lower case letters + 4 numbers ]
# If you know about regular expressions you can use the re module to create one 

try:
    username = sys.argv[1]
except IndexError:
    sys.exit("Usage: python username.py <username>")

pattern = re.compile("^[a-z]{4}[0-9]{4}(@leeds\.ac\.uk)?$")

if pattern.match(username):
    print("This is a valid UoL username")
else:
    print("This is NOT a valid username for students who started in 2024-25")

# The output should be a validation that the string input is of the correct form  
