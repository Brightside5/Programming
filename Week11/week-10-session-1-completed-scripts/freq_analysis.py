import matplotlib.pyplot as plt

import sys

try:
    filename = sys.argv[1]
except:
    print("Error: Need a filename")
    exit(1)

# count letters in the file using a dictionary
letters = {}
try:
    with open(filename) as f:
        for row in f:
            for letter in row:
                if letter.isalpha():
                    letter = letter.upper()
                    try:
                        letters[letter] += 1
                    except:
                        letters[letter] = 1
except:
    print(f"Error: could not open file {filename}")

# Extract letters and their frequencies
lets = list(letters.keys())
frequencies = list(letters.values())

# Plot the histogram
plt.bar(lets, frequencies, color='purple')

# Saving it into filename.png
plt.savefig(f"{filename.split(".")[0]}.png")  # you can view the png image in the folder
