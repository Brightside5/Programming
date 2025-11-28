
# Name:Hangming Hu
# Username: 

import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.
if len(sys.argv)!=2:
    print("Usage: python file_line_count.py <filename.txt>",file=sys.stderr)
    sys.exit(1)

# filename is a command line argument 
file_name=sys.argv[1]

# Error message: "Usage: python file_line_count.py <filename.txt>"

# Open the file and read its content

# Error message: "File not found: python file_line_count.py {file_name}"

# count number of lines that are not blank
number_of_lines = 0
try:
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():  # Check if the line is not empty
                number_of_lines += 1
    print(f"{file_name} has {number_of_lines} lines")
except FileNotFoundError:
    print(f"File not found: python file_line_count.py {file_name}", file=sys.stderr)
    sys.exit(1)

# success - report the number of lines

# Success message: "{file_name} has {number_of_lines} lines"

# Test on the 'text_example.txt' file. The answer should be 4.